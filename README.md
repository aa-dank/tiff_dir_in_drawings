# tiff_dir_in_drawings
The problem that this script is trying to solve is that our windows file server has folder of blueprints scanned into tiff files that are not correctly identified.  
 The script crawls a windows folder system looking for directories that only contain tiff files. The script then searches the path to see if this folder of tiffs is within folder that includes one of UCSC construction records flags in the folder name. <br/>  
 The flags used are 'F - ' and 'F5 - ' as all drawings files should be nested somewhere in a folder with one of these flags according to UCSC PPDO protocols.





