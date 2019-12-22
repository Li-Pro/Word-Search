import sys
import requests

# Constants
sPrf = {'oed': 'www.oxfordlearnersdictionaries.com/definition/english/',
		'urb': 'www.urbandictionary.com/define.php?term='}

def getPage(url): return requests.get(url).text

def searchWord(key, dicprf='oed'):
	if not dicprf in sPrf: dicprf = 'oed'
	return getPage('https://' + sPrf[dicprf] + key)

def main():
	print("----- Word Search -----")
	for line in sys.stdin:
		seq = line[:-1].split(' ')
		if len(seq) > 0:
			print(searchWord(seq[0], (seq[1] if (len(seq)>=2 and len(seq[1])>0) else 'oed')))

if __name__=="__main__": main()