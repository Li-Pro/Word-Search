# Parser of search result
import string

class Format:
	VIEWABLES = string.digits + string.ascii_letters + string.punctuation + ' \n'
	
	def strViewable(s):
		sum = ''
		for x in s:
			if not x in Format.VIEWABLES:
				if x == '\r': x = '\n'
				else: x = ' '
			sum += x
		return sum

def OEDParser(soup, bWithExample):
	#print('#', soup)
	defs = soup.find_all(class_='sn-g')
	rep = ''
	for i in range(len(defs)):
		rep += str(str(i+1)+'. ' + defs[i].find('span', class_='def').get_text()+'\n')
		if bWithExample:
			for exm in defs[i].find_all('span', class_='x'):
				exmtxt = Format.strViewable(exm.get_text())
				if len(exmtxt)>0: rep += ' - ' + exmtxt + '\n'
			rep += '\n'
	if len(defs) == 0: rep = 'Word not recognized by dictionary.\n'
	return rep

def URBParser(soup, bWithExample):
	defs = soup.find_all('div', 'def-panel')
	rep = '\n'
	for i in range(len(defs)):
		x = Format.strViewable(defs[i].find('div', class_='meaning').get_text())
		rep += str(i+1)+'\n---\n' + x.replace('\n', ' \n') +'\n\n'
		
		if bWithExample:
			exm = defs[i].find('div', class_='example')
			for dlm in exm.find_all('br'): dlm.replace_with('\n')
			
			exmtxt = '  ' + Format.strViewable(exm.get_text()).replace('\n', '\n  ')
			if len(exmtxt)>0: rep += exmtxt + '\n'
			
	if len(defs) == 0: rep = 'Word not recognized by dictionary.\n'
	return rep