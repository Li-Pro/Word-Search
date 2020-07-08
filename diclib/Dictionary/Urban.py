""" Dictionary: Urban Dictionary """

from ..dicTypes import DicResult, DicBase

def URBParser(soup, bWithExample):
	""" The parser of Urban's Dictionary. """
	rep = DicResult(bWithExample)
	
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

class Dictionary(DicBase):
	def parse(self, page, bWithExample):
		return URBParser(page, bWithExample)
	
	def formatURL(self, key):
		return 'https://www.urbandictionary.com/define.php?term={}'.format(key)

DIC_OBJ = Dictionary()