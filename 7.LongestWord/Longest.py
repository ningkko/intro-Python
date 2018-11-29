#Longest.py
#Yining Hua
#Assignment 7
#This program looks for the longest words in a text

def main():
	 '''This program asks for a text and looks for the longest words in the given text。
'''

	
	 textname = input("Enter your input text here:")
	 f = open(textname,'r')
	 text = f.read()
	 
	 Longest(text)
	 
	 f.close()


def Longest(text):
	'''Longest(text): Take a text as an input and print out the longest words and their length in that given text.
'''
	text = CleanUp(text)
	newtext = text.split()

	#create an empty list 'set[]' to store (len(char),char) for all the chars inside the input text 
	sets = []
	for element in newtext:
		sets.append([len(element),element])

        #sort the tuple list sets[] by the their first elements.
	sets.sort(key = lambda x:x[0],reverse = True)

	#create an empty list  'longestset[]' to store the chars which have teh longest lenth inside sets[]
	longestset = []
	for i in sets:
		if (i[0]==sets[1][0]) and (i not in longestset):
			longestset.append(i[1])
	longestset.sort()
	
	print("The Longest words in the text have",sets[1][0],"letters\nHere are all the words of length",sets[1][0],'\n'+"-"*40)
	for ele in longestset:
		print(ele)

	
def CleanUp( text ):
	'''CleanUp(text): cleanup punctuation in the given text to isolate words
	'''
	text = text.lower( )
	#replace 2 required punctuations by the empty string
	text = text.replace("'","")
	text = text.replace("-","")
	# Replace other punctuations by space chars
	punc = ':?!.,;<>=()[]"*~@#$%^&'
	for c in punc:
		text = text.replace( c, ' ')       
	return text

main()
