"""
Author: Li-Pro 2020

An example interactive program that searches for words.
"""

import sys
import string
import requests
from bs4 import BeautifulSoup

import dicparser  # The main library 

class Format:
	VIEWABLES = string.digits + string.ascii_letters + string.punctuation + ' \n'
	
	def strViewable(s):
		""" Format to readable. Prevent '\\r'. """
		sum = ''
		for x in s:
			if not x in Format.VIEWABLES:
				if x == '\r': x = ' '
				else: x = ' '
			sum += x
		
		return sum
	
	def setLineWidth(s, wlim):
		""" To be easier to read. """
		sum = ''
		for ox in s.split('\n'):
			cnt = 0
			for x in ox.split(' '):
				if len(x)<=0:
					continue
				
				if cnt+len(x) >= wlim:
					sum += '\n'
					cnt = 0
				
				sum += x+' '
				cnt += len(x)+1
			
			sum += '\n'
		
		return sum
	
	def formatted(result, bWithExample, wlim):
		if not len(result.defs):
			return 'Word not found.\n'
		
		rep = ''
		for i in range(len(result.defs)):
			rep += str(i+1)+'. \n---\n'
			for defx in result.defs[i]:
				rep += defx + '\n'
			
			if bWithExample:
				rep += '\nExamples: \n'
				for egx in result.examples[i]:
					rep += egx + '\n'
			
			rep += '\n'
		
		return rep

# def OEDParser(soup, bWithExample):
	# defs = soup.find_all(class_='sn-g')
	# rep = ''
	# for i in range(len(defs)):
		# rep += str(i+1)+'. '
		# for txt in defs[i].find_all('span', class_=['def', 'label-g', 'ndv', 'xr-g'], recursive=False):
			# rep += Format.strViewable(txt.get_text())+' '
		# rep += '\n'
		
		# if bWithExample:
			# for exm in defs[i].find_all('span', class_='x'):
				# exmtxt = Format.strViewable(exm.get_text())
				# if len(exmtxt)>0: rep += ' - ' + exmtxt + '\n'
		# rep += '\n'
	# if len(defs) == 0: rep = 'Word not recognized by dictionary.\n'
	# return rep

# def URBParser(soup, bWithExample):
	# defs = soup.find_all('div', 'def-panel')
	# rep = '\n'
	# for i in range(len(defs)):
		# txt = defs[i].find('div', class_='meaning')
		# for dlm in txt.find_all('br'): dlm.replace_with('\n')
		
		# x = Format.strViewable(txt.get_text())
		# rep += str(i+1)+'\n---\n' + x.replace('\n', ' \n') +'\n\n'
		
		# if bWithExample:
			# exm = defs[i].find('div', class_='example')
			# for dlm in exm.find_all('br'): dlm.replace_with('\n')
			
			# exmtxt = '  ' + Format.strViewable(exm.get_text()).replace('\n', '\n  ')
			# if len(exmtxt)>0: rep += exmtxt + '\n'
			
	# if len(defs) == 0: rep = 'Word not recognized by dictionary.\n'
	# return rep

def main():
	""" A search program """
	print("----- Search Panel -----\n")
	while True:
		try: line = input("Search: ")
		except (EOFError): break
		
		if len(line) <= 0:
			print()
			continue
		
		seq = line.split(' ')
		word, dic, bWithExample, wlim = seq[0], 'oed', False, 90  # word & options
		for sOpt in seq[1:]:
			if len(sOpt)<=2 or sOpt[0]!='-':
				continue
			
			opt = sOpt[1:]
			if opt in dicparser.DicUtil.dic_list: dic = opt
			elif opt=='eg': bWithExample = True
			elif opt[0]=='w':
				if all((x in string.digits) for x in opt[1:]):
					wlim = int(opt[1:])
		
		result = dicparser.DicUtil.searchWord(word, dic, bWithExample)
		print(Format.formatted(result, bWithExample, wlim))

if __name__=="__main__": main()