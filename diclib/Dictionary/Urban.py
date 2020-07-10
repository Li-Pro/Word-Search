""" Dictionary: Urban Dictionary """

from ..dicTypes import DicResult, DicBase

def URBParser(soup, key):
	""" The parser of Urban's Dictionary. """
	rep = DicResult(key)
	
	defs = soup.find_all('div', 'def-panel')
	for i in range(len(defs)):
		word = defs[i].find(class_='word').get_text()
		if not word.lower() == key.lower():
			continue
		
		txt = defs[i].find('div', class_='meaning')
		
		for dlm in txt.find_all('br'):
			dlm.replace_with('\n')
		
		rep.defs.append([txt.get_text()])
		
		exm = defs[i].find('div', class_='example')
		for dlm in exm.find_all('br'):
			dlm.replace_with('\n')
		
		rep.examples.append([exm.get_text()])
	
	return rep

class Dictionary(DicBase):
	def parse(self, page, key):
		return URBParser(page, key)
	
	def formatURL(self, key):
		return 'https://www.urbandictionary.com/define.php?term={}'.format(key)

DIC_OBJ = Dictionary()