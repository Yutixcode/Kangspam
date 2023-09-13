reset  = '\x1b[0m'
bold   = '\x1b[1m'
dark   = '\x1b[90m'
red    = '\x1b[31m'
green  = '\x1b[32m'
yellow = '\x1b[33m'
blue   = '\x1b[34m'
purple = '\x1b[35m'
cyan   = '\x1b[36m'
white  = '\x1b[37m'
RED    = '\x1b[91m'
GREEN  = '\x1b[92m'
YELLOW = '\x1b[93m'
BLUE   = '\x1b[94m'
PURPLE = '\x1b[95m'
CYAN   = '\x1b[96m'
WHITE  = '\x1b[97m'

import os
import uuid
import time
import base64
import string
import random
import hashlib
import getpass 
import urllib.parse
import requests as req
req.urllib3.disable_warnings()
from bs4 import BeautifulSoup as bs

def banner():
	os.system('cls' if os.name == 'nt' else 'clear')
	warna = random.choice([CYAN,PURPLE,GREEN,RED,YELLOW])
	print(f"""{bold}\n
 {WHITE}_  _ ____ {RED}_{WHITE}  _ ____ {warna}____ ___  ____ _  _ 
 {WHITE}|_/  |__| |{RED}\ {WHITE}| | __ {warna}[__  |__] |__| |\/| 
 {WHITE}| \_ |  | |{RED} \{WHITE}| |__] {warna}___] |    |  | |  | {reset}{blue}v3.0
 
  {white}Ganggu temen lu yg doyan banget pushrank
  {dark}
   - Dibuat oleh Yutix
   - t.me/yutixverse
   - github.com/yutixcode
   - facebook.com/njnk.xnxx
   - yutixcode.blogspot.com
	""")