""" Dictionary: Urban Dictionary """
from .. import dicTypes

def URBParser(soup, bWithExample):
	""" The parser of Urban's Dictionary. """
	rep = dicTypes.Result(bWithExample)
	
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

DIC_OBJ = dicTypes.Dictionary('https://www.urbandictionary.com/define.php?term=%s', URBParser)