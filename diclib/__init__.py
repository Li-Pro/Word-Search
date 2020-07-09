"""
Author: Li-Pro 2020

The main file of dictionary library.
"""

import string
import requests

from bs4 import BeautifulSoup

""" The dictionaries """
from .Dictionary import OxfordLearners
from .Dictionary import Urban
from .Dictionary import Cambridge

__all__ = ['OxfordLearners', 'Urban', 'Cambridge', 'searchWord', 'getWordPage']

# The extensible dictionary list!
dic_list = {'oed': OxfordLearners.DIC_OBJ,
			'urb': Urban.DIC_OBJ,
			'camb': Cambridge.DIC_OBJ}

def getWordPage(key, dic_obj):
	""" Send request towards the online dictionary. """
	return dic_obj.requestWord(key)

def searchWord(key, dicname='camb'):
	"""
	Provide a search utility.
	
	key -- the word
	dicname -- the dictionary name (as in dic_list)
	"""
	if not dicname in dic_list:
		dicname = 'camb'
	
	dic_obj = dic_list[dicname]
	rep = getWordPage(key, dic_obj)
	return dic_obj.parse(BeautifulSoup(rep, 'lxml'))