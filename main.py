import sys
import string
import requests
from bs4 import BeautifulSoup

import dicparser

# Constants
sPrf = {'oed': ('www.oxfordlearnersdictionaries.com/definition/english/%s', dicparser.OEDParser) ,
		'urb': ('www.urbandictionary.com/define.php?term=%s', dicparser.URBParser)}

def getPage(url): return requests.get(url).text

def searchWord(key, dicprf, bWithExample):
	if not dicprf in sPrf: dicprf = 'oed'
	rep = getPage('https://' + ((sPrf[dicprf][0]) % (key)))
	return sPrf[dicprf][1](BeautifulSoup(rep, 'lxml'), bWithExample)

def main():
	print("----- Word Search Panel -----\n")
	while True:
		try: line = input("Search: ")
		except (EOFError): break
		
		if len(line) <= 0:
			print()
			continue
		#print('#'+line+'#')
		
		seq = line.split(' ')
		word, dic, bWithExample, wlim = seq[0], 'oed', False, 90
		for sOpt in seq[1:]:
			if len(sOpt)<=2 or sOpt[0]!='-': continue
			
			opt = sOpt[1:]
			if opt in sPrf: dic = opt
			elif opt=='eg': bWithExample = True
			elif opt[0]=='w':
				if all((x in string.digits) for x in opt[1:]):
					wlim = int(opt[1:])
		
		defs = searchWord(word, dic, bWithExample)
		print(dicparser.Format.setLineWidth(defs, wlim), end='')

if __name__=="__main__": main()