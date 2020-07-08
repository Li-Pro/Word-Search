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
	def __init__(self, bWithExample):
		self.defs = []
		if bWithExample:
			self.examples = []
		else:
			self.examples = None

class Parsers:
	"""
	The parser functions.
	
	A parser function:
		- Receives (soup, bWithExample)
			soup -- A BeautifulSoup object presenting the page result
			bWithExample -- Are examples requested
		
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
		
		def parse(self, page, bWithExample):
			return DicResult(bWithExample)
		
		def formatURL(self, key):
			return '%s'
		
		def requestWord(self, key):
			url = self.formatURL(key)
			return requests.get(url).text
		
		def __getattr__(self, attr):
			raise AttributeError