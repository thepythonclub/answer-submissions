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
'''

main = 'http://thepythonclub.org:8081/'


def challenge1():
    # Request Challenge1
    url = main + 'challenge1'
    r = requests.get(url)
    print r.text

    # Obtain the question and then base64 decode
    word = r.text.split('"')[1]
    answer = base64.b64decode(word)
    print answer

    # Submit answer
    payload = {'answer': answer}
    s = requests.post(url, data=json.dumps(payload))

    print s.url
    print s.text

if __name__ == "__main__":
    challenge1()
