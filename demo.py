"""
Author: Li-Pro 2020

Refer to build/requirements.txt for build informations.

An example interactive program that searches for words.
"""

import sys

import diclib  # The main library
from diclib import dicProduce  # For presentation


class Format:
	def setLineWidth(s, wlim):
		""" To be easier to read. """
		S = ''
		for ox in s.split('\n'):
			cnt = 0
			for x in ox.split(' '):
				if len(x) <= 0:
					continue
				
				if cnt+len(x) >= wlim:
					S += '\n'
					cnt = 0
				
				S += (x+' ')
				cnt += (len(x)+1)
			
			S += '\n'
		
		return S
	
	def formatted(result, bWithExample, wlim):
		""" An format example. """
		if not len(result.defs):
			return 'Word not found.\n\n'
		
		rep = ''
		for i in range(len(result.defs)):
			rep += str(i+1)+'. \n---\n'
			rep += dicProduce.produce(result.defs[i])
			
			if bWithExample:
				rep += '\nExamples: \n'
				rep += dicProduce.produce(result.examples[i])
			
			rep += '\n'
		
		rep = dicProduce.filterViewable(rep)
		rep = Format.setLineWidth(rep, wlim)
		return rep

def main():
	""" A search program example. """
	print("----- Search Panel -----")
	print("Usage:")
	print(" Type a word to search.")
	print()
	
	print("Options:")
	print(" -oed : Oxford English Dictionary (Update Required)")
	print(" -urb : Urban Dictionary")
	print(" -camb: Cambridge Dictionary")
	print()
	
	print(" -eg  : show th examples")
	print(" -wXX : set line width to XX")
	print("------------------------")
	print()
	
	while True:
		try: line = input("Search: ")
		except (EOFError): break
		
		if len(line) <= 0:
			print()
			continue
		
		seq = line.split(' ')
		word, dic, bWithExample, wlim = [], 'oed', False, 90  # word & options
		for sOpt in seq:
			if (len(sOpt) > 1) and (sOpt[0] == '-'):
				opt = sOpt[1:]
				if opt in diclib.dic_list:
					dic = opt
				
				elif opt=='eg': 
					bWithExample = True
				
				elif (opt[0]=='w') and (len(opt[1:]) > 0):
					if all((x in string.digits) for x in opt[1:]):
						wlim = int(opt[1:])
			
			elif len(sOpt) > 0:
				word.append(sOpt)
		
		try:
			result = diclib.searchWord(' '.join(word), dic)
		except Exception as e:
			print('Error: {}\n'.format(e))
		else:
			print(Format.formatted(result, bWithExample, wlim), end='')

if __name__=="__main__":
	main()  # Run the example