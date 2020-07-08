"""
Author: Li-Pro 2020

The main file of dictionary library.
"""

import string
import requests

from bs4 import BeautifulSoup

""" The dictionaries """
from .Dictionary import OxfordLearners as dicOxfordLearners
from .Dictionary import Urban as dicUrban
from .Dictionary import Cambridge as dicCambridge

# The extensible dictionary list!
dic_list = {'oed': dicOxfordLearners.DIC_OBJ,
			'urb': dicUrban.DIC_OBJ,
			'camb': dicCambridge.DIC_OBJ}

def getWordPage(key, dic_obj):
	""" Send request towards the online dictionary. """
	url = ''
	if type(dic_obj.urlformat)==str:
		url = str(dic_obj.urlformat % (key))
	elif callable(dic_obj.urlformat):
		url = dic_obj.urlformat(key)
	
	return requests.get(url).text

def searchWord(key, dicname='camb', bWithExample=False):
	"""
	Provide a search utility.
	
	key -- the word
	dicname -- the dictionary name (as in dic_list)
	bWithExample -- whether example is requested
	"""
	if not dicname in dic_list:
		dicname = 'camb'
	
	dic_obj = dic_list[dicname]
	rep = getWordPage(key, dic_obj)
	return dic_obj.parserfunc(BeautifulSoup(rep, 'lxml'), bWithExample)