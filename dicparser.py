"""
Author: Li-Pro 2020

The main dictionary parser library.
"""

import string
import requests
from bs4 import BeautifulSoup

class Result:
	"""
	The query result.
	Both variables are list of lists.
	e.g. defs = [ def_1[[def_1.1], [def_1.2], ... , [def_1.n]], def_2[...], ... , def_n[...] ]
	
	defs -- list of definitions ([]=not found)
	examples -- list of examples (None=not asked, []=not provided)
	"""
	def __init__(self, bWithExample):
		self.defs = []
		if bWithExample: self.examples = []
		else: self.examples = None

class Parsers:
	"""
	The parser functions.
	
	A parser function (as for now):
		- Receives (soup, bWithExample)
			soup -- An BeautifulSoup presenting the page result
			bWithExample -- Are examples requested
		
		- Returns an Result object
	"""
	def OEDParser(soup, bWithExample):
		""" The parser of Oxford Learner's Dictionary. """
		rep = Result(bWithExample)
		
		# defs from top
		if soup.find('div', class_='top-g')!=None:
			for txt in soup.find('div', class_='top-g').find_all('span', class_='xr-gs'):
				rep.defs.append([txt.get_text()])
				
				if bWithExample:
					rep.examples.append([])
		
		# defs in middle
		defs = soup.find_all(class_=['sn-g'])
		for i in range(len(defs)):
			defx = []
			for txt in defs[i].find_all('span', class_=['prefix', 'def', 'label-g', 'ndv', 'xr-gs', 'suffix'], recursive=False):
				if len(txt.get_text()):
					defx.append(txt.get_text())
			
			if not len(defx):
				continue
			
			rep.defs.append(defx)
			
			if bWithExample:
				examples = []
				for exm in defs[i].find_all('span', class_='x'):
					examples.append(exm.get_text())
				
				rep.examples.append(examples)
		
		return rep

	def URBParser(soup, bWithExample):
		""" The parser of Urban's Dictionary. """
		rep = Result(bWithExample)
		
		defs = soup.find_all('div', 'def-panel')
		for i in range(len(defs)):
			txt = defs[i].find('div', class_='meaning')
			
			for dlm in txt.find_all('br'):
				dlm.replace_with('\n')
			
			rep.defs.append([txt.get_text()])
			
			if bWithExample:
				exm = defs[i].find('div', class_='example')
				for dlm in exm.find_all('br'):
					dlm.replace_with('\n')
				
				rep.examples.append([exm.get_text()])
		
		return rep

class DicUtil:
	
	class Dictionary:
		"""
		The dictionary object.
		
		Vars:
		urlformat -- the request url format [(%s) % (word)]
		parserfunc -- the parse function
		"""
		def __init__(self, urlformat, parserfunc):
			self.urlformat = urlformat
			self.parserfunc = parserfunc
	
	# The extensible dictionary list!
	dic_list = {'oed': Dictionary('https://www.oxfordlearnersdictionaries.com/definition/english/%s', Parsers.OEDParser),
				'urb': Dictionary('https://www.urbandictionary.com/define.php?term=%s', Parsers.URBParser)}
	
	def getWordPage(key, dic_obj):
		""" Send request towards the online dictionary. """
		url = str(dic_obj.urlformat % (key))
		return requests.get(url).text
	
	def searchWord(key, dicname, bWithExample):
		"""
		Provide a search utility.
		
		key -- the word
		dicname -- the dictionary name (as in dic_list)
		bWithExample -- whether example is requested
		"""
		if not dicname in DicUtil.dic_list:
			dicname = 'oed'
		
		dic_obj = DicUtil.dic_list[dicname]
		rep = DicUtil.getWordPage(key, dic_obj)
		return dic_obj.parserfunc(BeautifulSoup(rep, 'lxml'), bWithExample)