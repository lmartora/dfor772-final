# Final Project for DFOR 772

This is a repository for my final project of DFOR 772, in which I expanded on the capabilities of the netArchae plugin for Autopsy (original here: https://github.com/thePidge/netArchae)

## About 
### netArchae
netArchae is originally a plugin that searches an image for files ending in ".pcap", sorts those files under the "Interesting Files" section of "Data artifacts" with the label "Text Files". These pcaps are also able to be parsed for the keyword search function in Autopsy
### netArchaeFinal
netArchaeFinal is an expansion of netArchae which does all of what the base plugin can do. My expansion also finds .pcapng files, and can find both .pcap and .pcapng files from all of their respective magic numbers. And instead of labeling the found pcaps/pcapngs under "Text Files", they are labeled under "Packet Captures". 

#### These are significant changes because pcapng is a more up to date format for pcaps literally meaning "packet capture new generation" that is being more widely used, and is what one of the most popular packet capturing program Wireshark defaults to for saving captures; and because finding files based on magic numbers can find pcaps with mismatched file extensions that were attempted to be hidden by purposefully changing the extension.

### How it works
The program works first by importing several Autopsy-provided libraries that every plugin needs to function. With one of the imports, `IngestModuleFactoryAdapter`, a "factory" is created to provide the module with basic information on it as well as the ability to make ingest modules that work with the files in the image. 
#### Source code is viewable in `NetArchaeFinal.py`


## Usage Directions
1. (Optional, for testing) Begin the download on the provided `sample.E01` disk image which contains several packet captures for the program to find
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
15. The `Ingest Messages` toolbar (the blue envelope with a number on the top right) will show a message from NetArchaeFinal that reports on the number of packet captures it found.
