import json
import csv
import glob
import os
import ast

#create and open output file
if not os.path.exists("json_merged/"):
        os.makedirs("json_merged/")
outfile_name = "json_merged/halftime_show_merged.json"
print "Merging jsons"

with open(outfile_name, "a") as outfile:
    
    path = "F:\Superbowl Stats\Data\*.json"
    for json_file in glob.glob(path):
        
        #open json file and parse data while writing into output file
        with open(json_file, 'r') as open_json_file:
            outfile.write(open_json_file.read())
            
            
            
            
                
        
          
                
            
            
    
