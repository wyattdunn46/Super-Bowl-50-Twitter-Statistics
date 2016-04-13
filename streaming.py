from slistener import SListener
import time, tweepy, sys
from time import sleep

## authentication
##username = '' ## put a valid Twitter username here
##password = '' ## put a valid Twitter password here
auth     = tweepy.OAuthHandler('OwaEbdPfLJVnTuadkpFoQKs4m', 'wSWZ4hCn64nj3GAGKAcSVxvPDd26rYVGbOv81JBfP4VyTJYRCI')
auth.set_access_token('317599687-5KhnMVM92ZIgeGiyimi6yMDEautnrRBN7gvZwJLq', 'HfPFz9pLAsF3VNEOKZeXgz4Up7YyubJ55U3XvjtPQ1vvK')
api      = tweepy.API(auth)

def main():
    loop = True
    while (loop):
        track = ['halftime show','halftime']
 
        listen = SListener(api, 'halftime_show')
        stream = tweepy.Stream(auth, listen)

        print "Streaming started..."

        try: 
            stream.filter(track = track)
            loop = False
        except:
            print "error!"
            loop = True
            stream.disconnect()
            sleep(5)
            continue

if __name__ == '__main__':
    main()
