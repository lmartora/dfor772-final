import jarray
import inspect
from java.lang import System
from java.util.logging import Level
from org.sleuthkit.datamodel import SleuthkitCase
from org.sleuthkit.datamodel import AbstractFile
from org.sleuthkit.datamodel import ReadContentInputStream
from org.sleuthkit.datamodel import BlackboardArtifact
from org.sleuthkit.datamodel import BlackboardAttribute
from org.sleuthkit.datamodel import TskData
from org.sleuthkit.autopsy.ingest import IngestModule
from org.sleuthkit.autopsy.ingest.IngestModule import IngestModuleException
from org.sleuthkit.autopsy.ingest import DataSourceIngestModule
from org.sleuthkit.autopsy.ingest import FileIngestModule
from org.sleuthkit.autopsy.ingest import IngestModuleFactoryAdapter
from org.sleuthkit.autopsy.ingest import IngestMessage
from org.sleuthkit.autopsy.ingest import IngestServices
from org.sleuthkit.autopsy.ingest import ModuleDataEvent
from org.sleuthkit.autopsy.coreutils import Logger
from org.sleuthkit.autopsy.casemodule import Case
from org.sleuthkit.autopsy.casemodule.services import Services
from org.sleuthkit.autopsy.casemodule.services import FileManager

#module information
class NetArchaeologist(IngestModuleFactoryAdapter):

    moduleName = "NetArchaeFinal"

    def getModuleDisplayName(self):
        return self.moduleName

    def getModuleDescription(self):
        return "FOR DFOR 772. Extracts packet captures."

    def getModuleVersionNumber(self):
        return "1.0"

    def isFileIngestModuleFactory(self):
        return True

    def createFileIngestModule(self, ingestOptions):
        return netArchae()

#module functionality
class netArchae(FileIngestModule):

    _logger = Logger.getLogger(NetArchaeologist.moduleName)

    def log(self, level, msg):
        self._logger.logp(level, self.__class__.__name__, inspect.stack()[1][3], msg)

    def startUp(self, context):
        self.filesFound = 0
        pass

    def process(self, file):
        if ((file.getType() == TskData.TSK_DB_FILES_TYPE_ENUM.UNALLOC_BLOCKS) or 
            (file.getType() == TskData.TSK_DB_FILES_TYPE_ENUM.UNUSED_BLOCKS) or 
            (file.isFile() == False)):
            return IngestModule.ProcessResult.OK

        #find .pcap and .pcapng files
        if file.getName().lower().endswith(".pcap") or file.getName().lower().endswith(".pcapng") or file[0:4] == b'\xA1\xB2\xC3\xD4' or file[0:4] == b'\xD4\xC3\xB2\xA1' or file[0:4] == b'\xA1\xB2\xCD\x34' or file[0:4] == b'\x34\xCD\xB2\xA1' or file[0:4] == b'\xA1\xB2\x3C\x4D' or file[0:4] == b'\x4D\x3C\xB2\xA1' or file[0:4] == b'\x0A\x0D\x0D\x0A':

            self.log(Level.INFO, "Found PCAP: " + file.getName())
            self.filesFound+=1

            #make artifact on the blackboard.
            art = file.newArtifact(BlackboardArtifact.ARTIFACT_TYPE.TSK_INTERESTING_FILE_HIT)
            att = BlackboardAttribute(BlackboardAttribute.ATTRIBUTE_TYPE.TSK_SET_NAME, 
                              NetArchaeologist.moduleName, "Packet Captures")            
            art.addAttribute(att)

            try:
            #index artifact for keyword search.
                blackboard.indexArtifact(art)
            except Blackboard.BlackboardException as e:
                self.log(Level.SEVERE, "Error indexing artifact " + art.getDisplayName())

            #new artifact notification
            IngestServices.getInstance().fireModuleDataEvent(
                ModuleDataEvent(NetArchaeologist.moduleName, 
                    BlackboardArtifact.ARTIFACT_TYPE.TSK_INTERESTING_FILE_HIT, None));

            artifactList = file.getArtifacts(BlackboardArtifact.ARTIFACT_TYPE.TSK_INTERESTING_FILE_HIT)
            for artifact in artifactList:
                attributeList = artifact.getAttributes();
                for attrib in attributeList:
                    self.log(Level.INFO, attrib.toString())

        return IngestModule.ProcessResult.OK

    def shutDown(self):
        #report number of pcap files found in ingest messages
        message = IngestMessage.createMessage(
            IngestMessage.MessageType.DATA, NetArchaeologist.moduleName, 
                str(self.filesFound) + " packet captures found")
        ingestServices = IngestServices.getInstance().postMessage(message)