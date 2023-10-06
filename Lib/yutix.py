# Liat apa lo tolol ?

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
liner  = '\x1b[4m'

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
from concurrent.futures import ThreadPoolExecutor as Yutix

def banner():
	os.system('cls' if os.name == 'nt' else 'clear')
	warna = random.choice([CYAN,PURPLE,GREEN,RED,YELLOW])
	print(f"""{bold}
 {WHITE}_  _ ____ {RED}_{WHITE}  _ ____ 
 {WHITE}|_/  |__| |{RED}\ {WHITE}| | __  {reset}{white}versi: {liner}{yellow}5{reset}{bold}
 {WHITE}| \_ |  | |{RED} \{WHITE}| |__]  {reset}{white}author: {liner}Yutix{reset}{bold}
 {warna}____ ___  ____ _  _  {white}{dark}~ {liner}t.me/yutixverse{reset}{bold}
 {warna}[__  |__] |__| |\/|  {white}{dark}~ {liner}github.com/yutixcode{reset}{bold}
 {warna}___] |    |  | |  |  {white}{dark}~ {liner}facebook.com/njnk.xnxx{reset}
	""")
