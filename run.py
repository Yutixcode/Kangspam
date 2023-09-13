from Yxdata.Yxspam import *

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

def main():
	exec(open('.banner').read())
	ayana = ['01','02','03','04','05','06','07','69','99','00']
	try:
		ho = int(input(f'{AQUA}KangSpam {biasa}> {AQUA}'))
	except KeyboardInterrupt:
		lol = 'Program diberhentikan'
		to(lol)
	except Exception as lol:
		to(lol)
	oh = f'{ho:0=2d}'
	if  oh  == '01':
		magnetpro()
	elif oh == '02':
		thaibah()
	elif oh == '03':
		jagreward()
	elif oh == '04':
		lokadok()
	elif oh == '05':
		kreditplus()
	elif oh == '06':
		esaskkp()
	elif oh == '07':
		paradox()
	elif oh == '69':
		update()
	elif oh == '99':
		report()
	elif oh == '00':
		dahlah()
	elif oh not in ayana:
		lol = f'Pilihan {ho} tidak tersedia!'
		to(lol)

def magnetpro():
	print(f'\n\n {biasa}[+] Gunakan awalan 08 (ex: {AQUA}08131xnxx{biasa})')
	eh = Yx.naon()
	Yx.magnetpro(eh['z'],eh['x'])

def thaibah():
	print(f'\n\n {biasa}[+] Gunakan awalan 08 (ex: {AQUA}08131xnxx{biasa})')
	eh = Yx.naon()
	Yx.thaibah(eh['z'],eh['x'])
	
def jagreward():
	lol = 'Spam yang ini udah modar bro'
	to(lol)

def lokadok():
	print(f'\n\n {biasa}[+] Jangan gunakan 0 (ex: {AQUA}8131xnxx{biasa})')
	eh = Yx.naon()
	Yx.lokadok(eh['z'],eh['x'])
	
def kreditplus():
	print(f'\n\n {biasa}[+] Gunakan awalan 08 (ex: {AQUA}08131xnxx{biasa})')
	eh = Yx.naon()
	Yx.kreditplus(eh['z'],eh['x'])
	
def esaskkp():
	lol = 'Spam yang ini udah modar bro'
	to(lol)
	
def paradox():
	lol = 'Spam yang ini udah modar bro'
	to(lol)
	
def update():
	try:
		remote = 'http://yutixcode.xyz/Backdoor/RemoteServer/KangSpam/v2.0'
		ngetes = rek.get(remote).text
		if ngetes != 'Latest':
			print(f'\n {tebel}{BODAS}[!] {biasa}{HEJO}Versi baru sudah tersedia!')
			x = input(f'  {AQUA}>  {bodas}Update sekarang? y/n : ').lower()
			if x == 'y':
				print(AQUA)
				os.system('git pull --force')
				#os.system('pkg update && pkg upgrade')
				print(f'\n {tebel}{BODAS}[!] {biasa}{HEJO}Update selesai \n')
				exit()
			else:
				lol = 'Update dibatalkan'
				to(lol)
		else:
			print(f'\n {tebel}{BODAS}[!] {biasa}{BEREM}Versi baru belum tersedia\n')
	except Exception as lol:
		to(lol)
	
def report():
	print(f'\n{biasa} [+] {bodas}Pesan akan dibalas, Gunakan {AQUA}email aktif{bodas}')
	try:
		aran = input("  -  nama  : ")
		mail = input("  -  email : ")
		halo = input("  -  pesan : ")
		if (len(aran) < 3) or (len(mail) < 3) or (len(halo) < 5):
			exit(f'\n {tebel}{BODAS}[!] {biasa}{bodas}Pesan ditolak!\n     Isi yg bener tolol!\n')
		else:
			Yx.lapor(aran, mail, halo)
	except KeyboardInterrupt:
		lol = 'Program diberhentikan'
		to(lol)
	except Exception as lol:
		to(lol)
	
def dahlah():
	lol = 'Sampai jumpa lagi'
	to(lol)
	
if __name__ == '__main__':
	main()
