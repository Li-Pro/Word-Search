"""
Author: Li-Pro 2020

The main dictionary parser library.
"""

import string
import requests
from bs4 import BeautifulSoup

class Format:
	VIEWABLES = string.digits + string.ascii_letters + string.punctuation + ' \n'
	
	def strViewable(s):
		sum = ''
		for x in s:
			if not x in Format.VIEWABLES:
				if x == '\r': x = ' '
				else: x = ' '
			sum += x
		
		return sum
	
	def setLineWidth(s, wlim):
		sum = ''
		for ox in s.split('\n'):
			cnt = 0
			for x in ox.split(' '):
				if len(x)<=0:
					continue
				
				if cnt+len(x) >= wlim:
					sum += '\n'
					cnt = 0
				
				sum += x+' '
				cnt += len(x)+1
			
			sum += '\n'
		
		return sum

def OEDParser(soup, bWithExample):
	defs = soup.find_all(class_='sn-g')
	rep = ''
	for i in range(len(defs)):
		rep += str(i+1)+'. '
		for txt in defs[i].find_all('span', class_=['def', 'label-g', 'ndv', 'xr-g'], recursive=False):
			rep += Format.strViewable(txt.get_text())+' '
		rep += '\n'
		
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
		txt = defs[i].find('div', class_='meaning')
		for dlm in txt.find_all('br'): dlm.replace_with('\n')
		
		x = Format.strViewable(txt.get_text())
		rep += str(i+1)+'\n---\n' + x.replace('\n', ' \n') +'\n\n'
		
		if bWithExample:
			exm = defs[i].find('div', class_='example')
			for dlm in exm.find_all('br'): dlm.replace_with('\n')
			
			exmtxt = '  ' + Format.strViewable(exm.get_text()).replace('\n', '\n  ')
			if len(exmtxt)>0: rep += exmtxt + '\n'
			
	if len(defs) == 0: rep = 'Word not recognized by dictionary.\n'
	return rep

class DicUtil:
	
	class Dictionary:
		"""
		The dictionary object.
		
		Vars:
		urlformat -- the request url format [(%s) % (word)]
		parserfunc -- the parse function
		"""
		def __init__(self, urlformat, parserfunc):
			self.urlformat = urlformat
			self.parserfunc = parserfunc
	
	dic_list = {'oed': Dictionary('https://www.oxfordlearnersdictionaries.com/definition/english/%s', OEDParser),
				'urb': Dictionary('https://www.urbandictionary.com/define.php?term=%s', URBParser)}
	
	def getWordPage(key, dic_obj):
		""" Send request towards the online dictionary. """
		url = str(dic_obj.urlformat % (key))
		return requests.get(url).text
	
	def searchWord(key, dicname, bWithExample):
		"""
		Provide a search utility.
		
		key -- the word
		dicname -- the dictionary name (as in dic_list)
		bWithExample -- whether example is requested
		"""
		if not dicname in DicUtil.dic_list:
			dicname = 'oed'
		
		dic_obj = DicUtil.dic_list[dicname]
		rep = DicUtil.getWordPage(key, dic_obj)
		return dic_obj.parserfunc(BeautifulSoup(rep, 'lxml'), bWithExample)