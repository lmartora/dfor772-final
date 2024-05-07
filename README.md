# Final Project for DFOR 772

This is a repository for my final project of DFOR 772, in which I expanded on the capabilities of the netArchae plugin for Autopsy (original here: https://github.com/thePidge/netArchae)

## About 
### netArchae
netArchae is originally a plugin that searches an image for files ending in ".pcap", sorts those files under the "Interesting Files" section of "Data artifacts" with the label "Text Files". These pcaps are also able to be parsed for the keyword search function in Autopsy
### netArchaeFinal
netArchaeFinal is an expansion of netArchae which does all of what the base plugin can do. My expansion also finds .pcapng files, and can find both .pcap and .pcapng files from all of their respective magic numbers. And instead of labeling the found pcaps/pcapngs under "Text Files", they are labeled under "Packet Captures". 

#### These are significant changes because pcapng is a more up to date format for pcaps literally meaning "packet capture new generation" that is being more widely used, and is what one of the most popular packet capturing program Wireshark defaults to for saving captures; and because finding files based on magic numbers can find pcaps with mismatched file extensions that were attempted to be hidden by purposefully changing the extension.

## Usage Directions
1. Run Autopsy and close the ```Welcome``` box
2. On the ```Tools``` toolbar, click ```Python Plugins```
3. Create a new folder named ```NetArchaeFinal```
4. Download ```netArchaeFinal.py``` and place it in that folder
5. On the ```Case``` toolbar, click ```New Case```
6. Fill in any name and information for it, click ```Finish```
7. For ```Select Host```, click next
8. For ```Select Data Source Type```, click ```Disk Image or VM File```
9. Select disk image of choice for analysis, click next
10. For ```Configure Ingest```, leave all checked boxes checked, then ensure ```NetArchaeFinal``` is checked and click next
11. Wait until the ```Add Data Source``` window says ```Data source has been added to the local database. Files are being analyzed.```, and then click finish
12. After the module is done running and the image is completely analyzed, the blue loading bar at the bottom will disappear.
13. The ```Interesting Items``` category of ```Data Artifacts``` will show a subcategory called ```Packet Captures```, showing every pcap, pcapng, and mismatched file type that is a packet capture
14. The ```Ingest Messages``` toolbar (the blue envelope with a number on the top right) will show a message from NetArchaeFinal that reports on the number of packet captures it found.
