import sys
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

# TODO: include sentences
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
		word, dic, bWithExample = seq[0], 'oed', False
		for sOpt in seq[1:]:
			if len(sOpt)<=0 or sOpt[0]!='-': continue
			
			opt = sOpt[1:]
			if opt in sPrf: dic = opt
			elif opt=='eg': bWithExample = True
		
		print(searchWord(word, dic, bWithExample), end=('' if bWithExample else '\n'))

if __name__=="__main__": main()