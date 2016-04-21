import json
import csv
import os
import ast
    
with open ("C:\python27\scripts\json_merged\halftime_show.cvs", "a") as out_file:
    
    #create csv writer
    csv = csv.writer(out_file)
    #write header to out file
    print >> out_file, 'tweet_id, tweet_time, tweet_author, tweet_author_id, tweet_language, tweet_geo, tweet_text'
    #open json file and parse data
    with open("C:\python27\scripts\json_merged\halftime_show_merged.json", 'r') as open_json_file:
        
        #Get each tweet
        for line in open_json_file:
            try:
                tweet = json.loads(line)
                # row represents the attributes we are pulling from each tweet
                row = (
                    tweet['id'],                    # tweet_id
                    tweet['created_at'],            # tweet_time
                    tweet['user']['screen_name'],   # tweet_author
                    tweet['user']['location'],      # tweeter location
                    tweet['user']['id_str'],        # tweet_authod_id
                    tweet['lang'],                  # tweet_language
                    tweet['geo'],                   # tweet_geo
                    tweet['text'],                  # tweet_text
                    tweet['timestamp_ms']           # tweet time in ms
                )
                values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
                csv.writerow(values)
            except:
                pass 
