"""
Author: Li-Pro 2020

The main file of dictionary library.
"""

import string
import requests
from bs4 import BeautifulSoup

""" The dictionaries """
import diclib.Dictionary.OxfordLearners as dicOxfordLearners
import diclib.Dictionary.Urban as dicUrban

# The extensible dictionary list!
dic_list = {'oed': dicOxfordLearners.DIC_OBJ, 'urb': dicUrban.DIC_OBJ}

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
	if not dicname in dic_list:
		dicname = 'oed'
	
	dic_obj = dic_list[dicname]
	rep = getWordPage(key, dic_obj)
	return dic_obj.parserfunc(BeautifulSoup(rep, 'lxml'), bWithExample)