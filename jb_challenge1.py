#!/usr/bin/env python

import requests
import base64
import json

'''
JB Challenge 1
'''

#decode it
#post it back to url in json form


def challenge(num):
    #get challenge from URL
    main = 'http://thepythonclub.org:808' + num
    url = main + '/challenge' + num
    req = requests.get(url)
    
    # Obtain the question
    quest = req.text
    print 'Question:', quest

    #Retrieve substring from the question
    first= quest.find('"')
    last= quest.rfind('"')
    word = quest[first+1:last]
    
    #base64 decode it
    ans = base64.b64decode(word)
    print 'Solution:', ans

    # Submit answer
    payload = {'answer': ans}
    s = requests.post(url, data=json.dumps(payload))

    print 'Response:', s.text

if __name__ == "__main__":
    challenge('1')
