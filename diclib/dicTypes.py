"""
Author: Li-Pro 2020

The main dictionary parser library.
"""

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
	pass

class Dictionary:
		"""
		The dictionary object.
		
		Vars:
		urlformat -- the request url format (str[(%s) % (word)] or func) ####### NOT WORKING YET #######
		parserfunc -- the parse function
		"""
		def __init__(self, urlformat, parserfunc):
			self.urlformat = urlformat
			self.parserfunc = parserfunc