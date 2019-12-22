# Parser of search result

def OEDParser(soup, bWithExample):
	defs = soup.find_all('li', class_='sn-g')
	rep = ''
	for i in range(len(defs)):
		rep += str(str(i+1)+'. ' + defs[i].find('span', class_='def').get_text()+'\n')
		if bWithExample:
			for exm in defs[i].find_all('span', class_='x'):
				exmtxt = exm.get_text()
				if len(exmtxt)>0: rep += ' - ' + exmtxt + '\n'
			rep += '\n'
	if len(defs) == 0: rep = 'Word not recognized by dictionary.\n'
	return rep

def URBParser(soup, bWithExample): return ''