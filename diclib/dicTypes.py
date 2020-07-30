"""
Author: Li-Pro 2020

The dictionary types.
"""

import requests

class DicResult:
	"""
	The query result.
	Both variables are list of lists.
	e.g. defs = [ def_1[[def_1.1], [def_1.2], ... , [def_1.n]], def_2[...], ... , def_n[...] ]
	
	defs -- list of definitions ([]=not found)
	examples -- list of examples (None=not asked, []=not provided)
	"""
	def __init__(self, word):
		self.word = word
		
		self.defs = []
		self.examples = []
	
	def __getattr__(self, attr):
		return None

class Parsers:
	"""
	The parser functions.
	
	A parser function:
		- Receives (soup)
			soup -- A BeautifulSoup object presenting the page result
		
		- Returns an Result object
	"""
	pass

class DicBase:
	"""
	The dictionary object.
	
	Vars:
	urlformat -- the request url format (urlformat % (word)) or format function (function(key)->str)
	parserfunc -- the parse function
	"""
	def __init__(self):
		return
	
	def parse(self, page, key):
		return DicResult(key)
	
	def formatURL(self, key):
		return '{}'.format(key)
	
	def requestWord(self, key):
		url = self.formatURL(key)
		return requests.get(url).text
