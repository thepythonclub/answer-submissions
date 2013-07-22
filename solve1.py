#!/usr/bin/env python

import requests
import base64
import json

'''
  Script Name: solve1.py

  Script Author: Jonathan Tomek

  Discussion / Functionality:
  Solve challenge1 for The Python Club

  Version:  07/22/2013 - 1.0 - Initial release
                       - 1.1 - Updated for clarity
'''


def challenge(num):
    main = 'http://thepythonclub.org:808' + num
    # Request Challenge1
    url = main + '/challenge' + num
    r = requests.get(url)
    print 'Question:', r.text

    # Obtain the question and then base64 decode
    word = r.text.split('"')[1]
    answer = base64.b64decode(word)
    print 'Solution:', answer

    # Submit answer
    payload = {'answer': answer}
    s = requests.post(url, data=json.dumps(payload))

    print 'Response:', s.text

if __name__ == "__main__":
    challenge('1')
