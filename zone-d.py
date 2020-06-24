#Author D4RKSH4DOWS
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"

import requests as r
import os,time,random,threading,sys
from multiprocessing.dummy import Pool

os.system('clear')
print ('''%s
  ____                   __
 /_  / ___  ___  ___ ___/ /   %sCoded by D4RKSH4D0WS%s
  / /_/ _ \/ _ \/ -_) _  /    %sIG @anonroz_team%s
 /___/\___/_//_/\__/\_,_/     %sFB gg.gg/AnonRoz-Team
'''%(C1,W0,C1,W0,C1,W0))

def zd(sites):
	try:
		site=r.post('https://zone-d.org/notify/action',headers={'cache-control': 'max-age=0','upgrade-insecure-requests': '1','save-data': 'on','user-agent': random.choice(open('ua').read().splitlines()),'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','referer': 'https://zone-d.org/notify','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data={'attacker':sys.argv[1],'poc':'social+engineering','url':sites}).text
		if 'Success' in site:
			print ('%s[ %sSuccess %s] %s'%(W0,G0,W0,sites))
		elif 'Already Defaced' in site:
			print ('%s[ %sAlready Defaced %s] %s'%(W0,R0,W0,sites))
		elif 'URL Not Defaced' in site:
			print ('%s[ %sNot Defaced %s] %s'%(W0,R0,W0,sites))
		else:
			print ('%s[ %sFailed %s] %s'%(W0,R0,W0,sites))
	except r.exceptions.ConnectionError:
		exit('[!] Koneksi internet tidak ada')

try:
	sites = open(sys.argv[2]).read().splitlines()
	pp = Pool(5) #gk usah di tambahin dah 5 aja !
	pr = pp.map(zd, sites)
except IndexError:
	exit('%s[%s!%s] %sUse : python2 zone-d.py attacker list.txt\n%s[%s!%s] %sThe web must use http or https'%(W1,R1,W1,W0,W1,R1,W1,W0))
