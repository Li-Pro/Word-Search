#
# Author: Li-Pro 2020
#
# An example interactive program that searches for words.
#

import sys
import string
import requests
from bs4 import BeautifulSoup

import dicparser

def main():
	print("----- Search Panel -----\n")
	while True:
		try: line = input("Search: ")
		except (EOFError): break
		
		if len(line) <= 0:
			print()
			continue
		
		seq = line.split(' ')
		word, dic, bWithExample, wlim = seq[0], 'oed', False, 90 # word & options
		for sOpt in seq[1:]:
			if len(sOpt)<=2 or sOpt[0]!='-': continue
			
			opt = sOpt[1:]
			if opt in dicparser.DicUtil.dic_list: dic = opt
			elif opt=='eg': bWithExample = True
			elif opt[0]=='w':
				if all((x in string.digits) for x in opt[1:]):
					wlim = int(opt[1:])
		
		defs = dicparser.DicUtil.searchWord(word, dic, bWithExample)
		print(dicparser.Format.setLineWidth(defs, wlim), end='')

if __name__=="__main__": main()