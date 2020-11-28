#!/usr/bin/env python3
# Author: Roman Kulich @ 2020
# Version: v1.0.0

import requests
import argparse

TGREEN =  '\033[32m'
TWHITE = '\033[37m'
TRED = '\033[31m'

parser = argparse.ArgumentParser()
parser.add_argument("-u", help="target url", dest='target')
args = parser.parse_args()
target = args.target

print(TGREEN + '''
  ___  ____  ____   ___  _   _ 
 / __)(  _ \(_  _) / __)( )_( )
( (__  )   /  )(   \__ \ ) _ ( 
 \___)(_)\_) (__)()(___/(_) (_)                                                            

''',TWHITE)

if target is None:
    print(TRED + "Missing target! ==>",TWHITE + TGREEN + "Usage: crt.py -u target.com")
    print("")
else:
    response = requests.get('https://crt.sh/?q=' + target + '&output=json')
    json = response.json()
    for show in json:
        print(TGREEN + "Found: ",TWHITE + show['common_name'])
