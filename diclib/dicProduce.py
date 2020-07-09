from collections.abc import Iterable, Mapping
import string

from .dicTypes import DicResult

__all__ = ['produce']

VIEWABLES = string.digits + string.ascii_letters + string.punctuation + ' \n\t'
def isViewable(s):
	return (s in VIEWABLES) or (ord(s) > 32)

def filterViewable(s):
	S = ''
	i, N = 0, len(s)
	while i < N:
		if not isViewable(s[i]):
			S += ' '
		
		while (i < N) and (not isViewable(s[i])):
			i += 1
		
		if i < N:
			S += s[i]
			i += 1
	
	return S

def produce(res, dep=0):
	S = ''
	if not res:
		S += ' ' * (dep*2)
		S += 'Null\n'
	else:
		if isinstance(res, str):
			S += '{}\n'.format(res)
		elif isinstance(res, Mapping):
			for title, data in res:
				S += ' ' * (dep*2)
				
				if not data:
					S += title + '\n'
				elif isinstance(data, str):
					S += '({}) {}\n'.format(title, data)
				elif isinstance(data, Iterable):
					S += title + ':\n'
					for x in data:
						S += produce(x, dep+1)
				else:
					S += '({}) {}\n'.format(title, data)
		elif isinstance(res, Iterable):
			for data in res:
				S += ' ' * (dep*2)
				
				if not data:
					S += '\n'
				elif isinstance(data, str):
					S += '{}\n'.format(data)
				elif isinstance(data, Iterable):
					for x in data:
						S += produce(x, dep+1)
				else:
					S += '{}\n'.format(data)
		else:
			S += '{}\n'.format(res)
	
	return S