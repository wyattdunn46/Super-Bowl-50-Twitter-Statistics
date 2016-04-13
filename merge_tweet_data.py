import json
import csv
import glob
import os
import ast

def flatten(source):
    target = {}
    def helper(src, path ='.', last_key = None):
        if last_key: 
            target[last_key] = {}
            target[last_key]['location'] = path
        for key, value in src.items():
            if isinstance(value, dict):
                helper(value, os.path.join(path, key), key)

            else:
                target[last_key][key] = value

    helper(source)
    return target



    
with open ("F:\Superbowl Stats\cvs_merged\halftime_show_mergedcvs.cvs", "a") as out_file:
    
    #create csv writer
    csv = csv.writer(out_file)
    #write header to out file
    print >> out_file, 'tweet_id, tweet_time, tweet_author, tweet_author_id, tweet_language, tweet_geo, tweet_location, tweet_text'
    #open json file and parse data while writing into output file
    with open("F:\Superbowl Stats\json_merged\halftime_show_merged.json", 'r') as open_json_file:
        
        #Get each tweet
        for line in open_json_file:
            try:
                tweet = json.loads(line)
                #print "WE FUCKING DID IT BOYS!!!!!!!!!!!!!!!!!!!!!"
                row = (
                    tweet['id'],                    # tweet_id
                    tweet['timestamp_ms'],          # tweet_time
                    tweet['user']['screen_name'],   # tweet_author
                    tweet['user']['id_str'],        # tweet_authod_id
                    tweet['lang'],                  # tweet_language
                    tweet['user']['geo_enabled'],   # tweet_geo
                    tweet['user']['location'],      # tweet location
                    tweet['text']                   # tweet_text
                )
                values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
                csv.writerow(values)
            except:
                #print "Couldn't parse line: %s" % line
                pass
            
            
            
            
                
        
          
                
            
            
    
