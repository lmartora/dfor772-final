# Final Project for DFOR 772

This is a repository for my final project of DFOR 772, in which I expanded on the capabilities of the [netArchae](https://github.com/thePidge/netArchae) plugin for Autopsy.

## About 
### netArchae
netArchae is originally a plugin that searches an image for files ending in ".pcap" and sorts those files under the "Interesting Files" section of "Data artifacts" with the label "Text Files". These packet captures are also able to be parsed for the keyword search function in Autopsy
### netArchaeFinal
netArchaeFinal is an expansion of netArchae which does all of what the base plugin can do. My expansion also finds .pcapng files, and can find both .pcap and .pcapng files from all of their respective magic numbers. And instead of labeling the found pcaps/pcapngs under "Text Files", they are labeled under "Packet Captures". 

#### These are significant changes because .pcapng (packet capture new generation) is a more modern and up-to-date format of .pcap that is being more widely used, and is what one of the most popular packet-capturing programs Wireshark defaults to for saving captures; and because finding files based on magic numbers can find packet captures with mismatched file extensions that were attempted to be hidden by purposefully changing the extension.

### How it works
The program works first by importing several Autopsy-provided libraries that every plugin needs to function. With one of the imports, `IngestModuleFactoryAdapter`, a "factory" is created to provide the module with basic information on it as well as the ability to make ingest modules that work on the files in the image. The type of ingest module implemented in this plugin is a file ingest module, which examines every file from within a data source. The examination we perform in our file ingest module is checking for the following: 
- Files ending in `.pcap`
- Files ending in `.pcapng`
- Files with a magic header `A1 B2 C3 D4`
- Files with a magic header `D4 C3 B2 A1`
- Files with a magic header `A1 B2 CD 34`
- Files with a magic header `34 CD B2 A1`
- Files with a magic header `A1 B2 3C 4D`
- Files with a magic header `4D 3C B2 A1`
- Files with a magic header `0A 0D 0D 0A`

Once a file matching this critera is found, a "blackboard artifact" is created so that the found packet capture is sorted under the `Data Artifacts > Interesting Files > Packet Captures` of the results tree. The artifact is also indexed so that if a user wants to use keyword search later in the case to find packet captures, they will be able to see them in keyword search. Finally, once the plugin is done going through every file, it prints a message in the `Ingest Messages` tool of how many packet captures were found.
#### Source code is viewable in `netArchaeFinal.py`

### Requirements
- Autopsy 4.19.3 or later
- Python 3.x
- A disk image that contains packet capture files ([Sample](https://drive.google.com/file/d/1i1Cm7Jk7j1BNvLYjlJLubs0TD4ravh3-/view?usp=sharing))

## Usage Directions
1. ***(Optional, for testing)*** Begin the download on the sample disk image provided
2. Run Autopsy and close the `Welcome` box
3. On the `Tools` toolbar, click `Python Plugins`
4. Create a new folder named `NetArchaeFinal`
5. Download `netArchaeFinal.py` and place it in that folder
6. On the `Case` toolbar, click `New Case`
7. Fill in any name and information for it, click `Finish`
8. For `Select Host`, click next
9. For `Select Data Source Type`, click `Disk Image or VM File`
10. Select disk image of choice for analysis, click next
11. For `Configure Ingest`, leave all checked boxes checked, then ensure `NetArchaeFinal` is checked and click next
12. Wait until the `Add Data Source` window says `Data source has been added to the local database. Files are being analyzed.`, and then click finish
13. After the module is done running and the image is completely analyzed, the blue loading bar at the bottom will disappear.
14. The `Interesting Items` category of `Data Artifacts` will show a subcategory called `Packet Captures`, showing every pcap, pcapng, and mismatched file type that is a packet capture
15. The `Ingest Messages` toolbar (the blue envelope with a number on the top right) will show a message from NetArchaeFinal that reports on the number of packet captures it found
16. The `Keyword Search` tool can be used to search for names of files or contents of metadata in files, which can yield our found packet captures
