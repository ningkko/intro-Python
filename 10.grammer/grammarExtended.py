#Yining Hua
#GrammarExtended.py
#Assignment 10

'''
#An extended version which has 1.infinitives; 
2.transitives and intransitives; 3.Question advs; 
4.Time Advs 5. pronounces.

More features: 
1. Can generate exclamatory sentences, questions 
and compository sentences. 
2. Differentiates transitives and intransitives.
2. More ways for modifying nouns.
'''

def main():
	'''generate random sentences recursively'''
	#read in the dictionaty of words by category
	#NB: nouns etc. are globall lists
	ReadInDict()
	global dmax
	nsentence,dmax = eval( input( 'nsents,dmax=' ) )

	for i in range(0,nsentence):

		print("Sentence",str(i+1)+": ",end = "")

		s = sentence(0)
		for words in s:
			print(words,end=" ")
		print("\n")

def ReadInDict():
	'''Reads in a list of words, one category per line
		The 0-th element of the list is the category name.
		The filename is hardwired to dic.txt.
	''' 

	#Alwasys open the same file:

	f = open("DictExtended.txt",'r')

	global nouns
	global infinitivetransitives
	global transitives
	global infinitiveintransitives
	global intransitives
	global dets
	global adjs
	global preps
	global advs
	global pronounce
	global questions
	global time

	for line in f:
		if (line.find("nouns")==0):
			nouns = line.split()
			nouns.remove("nouns")

		if(line.find("infinitivetransitives")==0):
		    infinitivetransitives = line.split()
		    infinitivetransitives.remove("infinitivetransitives")

		if(line.find("transitives")==0):
		    transitives = line.split()
		    transitives.remove("transitives")

		if(line.find("infinitiveintransitives")==0):
		    infinitiveintransitives = line.split()
		    infinitiveintransitives.remove("infinitiveintransitives")

		if(line.find("intransitives")==0):
		    intransitives = line.split()
		    intransitives.remove("intransitives")

		if(line.find("dets")==0):
			dets = line.split()
			dets.remove("dets")

		if(line.find("adjs")==0):
			adjs = line.split()
			adjs.remove("adjs")

		if(line.find("preps")==0):
			preps = line.split()
			preps.remove("preps")

		if line.find("advs")==0:
			advs = line.split()
			advs.remove("advs")

		if line.find("pronounce")==0:
			pronounce = line.split()	
			pronounce.remove("pronounce")

		if(line.find("questions")==0):
			questions = line.split()
			questions.remove("questions")

		if(line.find("time")==0):
			time = line.split()
			time.remove("time")

	f.close()

def selectRandomWord(wordList):

	return wordList[randint(0,len(wordList)-1)]

def sentence(depth):
	'''1/3 chance of returning a questioning sentence 
		1/3 chance of returning a composed sentence
		1/3 chance of returning an exclamatory sentence.
	'''
	#conduct only when depth<=dmax	
	if depth>dmax:
		return []

	x = randint(1,3)

	if (x == 1):
	#1/3 chance to return ['Qestion Word']+Statement sentence	
		return [selectRandomWord(questions)]+ NP(depth) + VPinfinitive(depth)+["?"]
	
	#2/3 chance to return ['Qestion Word']+Statement sentence	
	elif (x == 2):
		#return wether a sentence with 50% chance of [pronounce]
		#or 50% chance of NP(depth)
		a = randint(1,2)
		if a == 1:
			return [selectRandomWord(time)]+statement(depth)+[","]+[selectRandomWord(pronounce)]+VP(depth)
		
		else: 
			return[selectRandomWord(time)]+statement(depth)+[" , "]+NP(depth)+VP(depth)
	
	#1/3 chance to return statement sentence
	else: 
		return statement(depth)+["!"]

def statement(depth):
	'''returns a statement sentence
	'''
	#conduct only when depth<=dmax
	if depth>dmax:
		return []
	else: 
		#S → NP VP
		return NP(depth)+VP(depth)

def NP(depth):
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	# NP → XN  | XN PP
	x = randint(1,2)
	if x == 1:
		#50% chance to return ['DET', 'N']
		return XN(depth)
	else:
		#50% chance to return['DET', 'N']+PP
		return XN(depth)+PP(depth+1)

def PP(depth):
	#conduct only when depth<=dmax	
	if depth>dmax:return []
	#return ['PREP'] + NP( depth+1 )
	return [selectRandomWord(preps)]+NP(depth)

def XN(depth):
	#conduct only when depth<=dmax
	if depth>dmax:return []
	#XN → DET N | DET ADJ N
	x = randint(1,3)

	if x == 1:
		return [selectRandomWord(dets),selectRandomWord(nouns)]
	
	elif x == 2:
		return [selectRandomWord(dets),selectRandomWord(adjs),selectRandomWord(nouns)]
	
	else:
		return [selectRandomWord(dets),selectRandomWord(advs),selectRandomWord(adjs),selectRandomWord(nouns)]

def VP(depth):
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	#VP → XV  | ADV XV
	x = randint(1,2)
	if x == 1:
		return XV(depth)

	else: 
		return [selectRandomWord(advs)]+XV(depth)

def VPinfinitive(depth):
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	#VP → XV  | ADV XV
	x = randint(1,2)
	if x == 1:
		return XVinfinitive(depth)

	else: 
		return [selectRandomWord(advs)]+XVinfinitive(depth)

def XV(depth):
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	else:
		x = randint(1,3)
		#1/3 chance of returning intransitives 
		if x == 1:	
			return [selectRandomWord(intransitives)]
		
		#2/3 chance of returning transitives
		else:
			#NP gets a parameter of depth because all the verbs are transitives
			return[selectRandomWord(transitives)]+NP(depth)

def XVinfinitive(depth):
	#conduct only when depth<=dmax
	if depth>dmax:
		return []

	else:
		x = randint(1,3)
		#1/3 chance of returning intransitive infinitives
		if x == 1:	
			return [selectRandomWord(infinitiveintransitives)]
		
		#2/3 chance of returning transitive infinitives
		else:
			#NP gets a parameter of depth because all the verbs are transitives
			return[selectRandomWord(infinitivetransitives)]+NP(depth)

main()