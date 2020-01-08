""" Dictionary: Cambridge Dictionary """
import diclib.dicTypes as dicTypes

import string

def CambridgeParser(soup, bWithExample):
	""" The parser of Cambridge Dictionary. """
	rep = dicTypes.Result(bWithExample)
	
	for ppdef in soup.find_all('div', class_='entry-body__el'):
		entry_info = ' '.join([tg.get_text() for tg in ppdef.find_all(class_=['posgram', 'anc-info-head'])])
		for pdef in ppdef.find_all('div', class_='sense-body'):
			defs = pdef.find_all('div', class_='def-block', recursive=False)
			for i in range(len(defs)):
				defx = []
				defx.append( entry_info + ' ' + defs[i].find(class_='def-info').get_text() )
				defx.append(defs[i].find(class_='def').get_text())
				
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