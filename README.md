# Final Project for DFOR 772

This is a repository for my final project of DFOR 772, in which I expanded on the capabilities of the netArchae plugin for Autopsy (original here: https://github.com/thePidge/netArchae)

## About 
### netArchae
netArchae is originally a plugin that searches an image for files ending in ".pcap", sorts those files under the "Interesting Files" section of "Data artifacts" with the label "Text Files". These pcaps are also able to be parsed for the keyword search function in Autopsy
### netArchaeFinal
netArchaeFinal is an expansion of netArchae which does all of what the base plugin can do. My expansion also finds .pcapng files, and can find both .pcap and .pcapng files from all of their respective magic numbers. And instead of labeling the found pcaps/pcapngs under "Text Files", they are labeled under "Packet Captures". 

These are significant changes because pcapng is a more up to date format for pcaps literally meaning "packet capture new generation" that is being more widely used, and is what one of the most popular packet capturing program Wireshark defaults to for saving captures; and because finding files based on magic numbers can find pcaps with mismatched file extensions that were attempted to be hidden by purposefully changing the extension.
