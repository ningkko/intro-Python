#Yining Hua
#Grammar.py
#Assignment 10
#Generates some weird random sentences

from random import randint

def main():
	'''generate random sentences recursively'''
	#read in the dictionaty of words by category
	#NB: nouns etc. are globall lists
	ReadInDict()
	global dmax
	nsentence,dmax = eval( input( 'nsents,dmax=' ) )

	for i in range(0,nsentence):

		print("Sentence",str(i+1)+": ",end = "")

		#S → NP+VP
		s = S(1)
		for words in s:
			print(words,end=" ")
		print(" ")

def ReadInDict():
	'''Reads in a list of words, one category per line
		The 0-th element of the list is the category name.
		The filename is hardwired to dic.txt.
	''' 

	#Alwasys open the same file:

	f = open("dict.txt",'r')

	global nouns
	global verbs
	global dets
	global adjs
	global preps
	global advs

	for line in f:
	    if (line.find("nouns")==0):
	    	nouns = line.split()
	    	nouns.remove("nouns")

	    if(line.find("verbs")==0):
	        verbs = line.split()
	        verbs.remove("verbs")

	    if(line.find("dets")==0):
	    	dets = line.split()
	    	dets.remove("dets")

	    if(line.find("adjs")==0):
	    	adjs = line.split()
	    	adjs.remove("adjs")

	    if(line.find("preps")==0):
	    	preps = line.split()
	    	preps.remove("preps")

	    if(line.find("advs")==0):
	   		advs = line.split()
	   		advs.remove("advs")
	f.close()

def selectRandomWord(wordList):

	return wordList[randint(0,len(wordList)-1)]

def S(depth):
	'''S → NP VP
'''		
	if depth>dmax:
		return []

	else:
		s = (NP(1)+VP(1))

	return s

def NP(depth):
	'''NP → XN  | XN PP
	'''
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	x = randint(1,2)
	if x == 1:
		#50% chance to return XN
		return XN(depth)
	else:
		#50% chance to return XN PP
		return XN(depth)+PP(depth+1)

def PP(depth):
	'''PP → PREP XN
	'''
	#conduct only when depth<=dmax	
	if depth>dmax:return []
	#return ['PREP'] + NP( depth+1 )
	return [selectRandomWord(preps)]+NP(depth)

def XN(depth):
	'''XN → DET N | DET ADJ N
	'''
	#conduct only when depth<=dmax
	if depth>dmax:return []

	x = randint(1,2)
	if x == 1:
		return [selectRandomWord(dets),selectRandomWord(nouns)]
	else:
		return [selectRandomWord(dets),selectRandomWord(adjs),selectRandomWord(nouns)]

def VP(depth):
	'''VP → XV  | ADV XV
	'''
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	x = randint(1,2)
	if x == 1:
		#XV
		return XV(depth)
	else: 
		#ADV XV
		return [selectRandomWord(advs)]+XV(depth)

def XV(depth):
	'''XV → V  | V NP
	'''
	#conduct only when depth<=dmax
	if depth>dmax:
		return []
	x = randint(1,3)

	if x == 1:
		#V
		return [selectRandomWord(verbs)]
	else:
		#V NP
		return[selectRandomWord(verbs)]+NP(depth)


main()