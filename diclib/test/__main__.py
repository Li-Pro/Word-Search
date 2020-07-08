import random

from diclib import *

testWord = ['hello']
testDict = ['camb', 'urb'] # 'oed'

def getDefs(word, dic):
	return searchWord(word, dic).defs

def getExamples(word, dic):
	return searchWord(word, dic, bWithExample=True).examples

def getOneDef(word, dic):
	return random.choice(getDefs(word, dic))

def getOneExample(word, dic):
	return random.choice(getExamples(word, dic))

def checkSingle(word):
	dic = random.choice(testDict)
	print('"{}" in {}:'.format(word, dic))
	
	defs, examples = getDefs(word, dic), getExamples(word, dic)
	i = random.randrange(len(defs))
	
	print('Definition: {}'.format(' '.join(defs[i])))
	print('Example: {}'.format(' '.join(examples[i]) if (len(examples[i]) > 0) else '(not provided)'))
	print()

print('DicLib Test')
print('-----------')

print('Running test #1')
for word in testWord:
	for dic in testDict:
		defs, examples = getDefs(word, dic), getExamples(word, dic)
		assert( len(defs) > 0 )
		assert( (examples != None) and (len(examples) == len(defs)) )

print('Test #1 passed.')
print()

print('Running test #2')
print('apple:', getOneDef('apple', 'camb') )
print()

testSingleWord = ['kitty', 'music', 'creature']
for word in testSingleWord:
	checkSingle(word)

print('Test #2 manual checking needed.')
print()

print('All auto-test passed.')