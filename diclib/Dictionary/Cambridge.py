""" Dictionary: Cambridge Dictionary """
import diclib.dicTypes as dicTypes

import string

def CambridgeParser(soup, bWithExample):
	""" The parser of Cambridge Dictionary. """
	# print('#', soup.get_text()[:100])
	rep = dicTypes.Result(bWithExample)
	
	defs = soup.find_all('div', class_='entry-body')
	for i in range(len(defs)):
		defx = []
		defx.append(defs[i].find('div', class_='di-title').get_text())
		if defs[i].find('div', class_='posgram')!=None:
			defx.append(defs[i].find('div', class_='posgram').get_text())
		defx.append(defs[i].find('div', class_='def').get_text())
		
		rep.defs.append(defx)
		
		if bWithExample:
			exmps = []
			for exmp in defs[i].find_all('div', class_='examp'):
				exmps.append(exmp.get_text())
			
			rep.examples.append(exmps)
	
	return rep

def URLFromKey(key):
	for ch in key:
		if not ch in string.ascii_letters:
			ch = '-'
	return str('https://dictionary.cambridge.org/dictionary/english/%s' % (key))

DIC_OBJ = dicTypes.Dictionary(URLFromKey, CambridgeParser)