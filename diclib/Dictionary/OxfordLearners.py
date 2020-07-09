""" Dictionary: Oxford Learner's Dictionary """

from ..dicTypes import DicResult, DicBase

def getText(soup, *args, **kwargs):
	if args or kwargs:
		soup = soup.find(*args, **kwargs)
	
	if not soup:
		return ''
	else:
		return soup.get_text()

def getAllText(soup, *args, **kwargs):
	return [*map(getText, soup.find_all(*args, **kwargs))]

def parseIntro(soup):
	soup = soup.find('div', id='entryContent').find(class_='webtop')
	d_word, d_pos = getText(soup, class_='headword'), getText(soup, class_='pos')
	
	# phon = soup.find(class_='phonetics')
	
	d_variant = getAllText(soup, class_='variants')
	d_infl = getText(soup, class_='inflections')
	
	return [d_word, {'pos': d_pos}, {'variants': d_variant}, {'inflections': d_infl}]

def parseDefs(soup):
	soup = soup.find('div', id='entryContent').find(class_='senses_multiple')
	
	rep = []
	entry = soup.find_all(class_='sense')
	for it in entry:
		rep.append(getText(it, class_='def'))
	
	return rep

def parseExample(soup):
	soup = soup.find('div', id='entryContent').find(class_='senses_multiple')
	
	rep = []
	entry = soup.find_all(class_='sense')
	for it in entry:
		eg = it.find(class_='examples')
		rep.append(getAllText(eg, class_='x'))
	
	return rep

def parseFooter(soup):
	soup = soup.find('div', id='entryContent')
	d_xrefs = getText(soup, class_='xrefs')
	
	origin = soup.find(unbox='wordorigin')
	d_origin = getText(origin, class_='body')
	
	return [d_xrefs, {'origin': d_origin}]

def OEDParser(soup, bWithExample):
	""" The parser of Oxford Learner's Dictionary. """
	rep = DicResult(bWithExample)
	
	rep.defs = parseDefs(soup)
	if bWithExample:
		rep.examples = parseExample(soup)
	
	return rep

class Dictionary(DicBase):
	def parse(self, page, bWithExample):
		return OEDParser(page, bWithExample)
	
	def formatURL(self, key):
		return 'https://www.oxfordlearnersdictionaries.com/definition/english/{}'.format(key)

DIC_OBJ = Dictionary()