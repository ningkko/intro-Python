# Palin.py
# Yejin Hwang & Yining Hua
# Lab 6
# Finds Palindrome in text file.

def IsPalindrome(word):
    if (len(word) == 1) :
        return False
    elif ( word[ : : -1] == word ) :
        return True
    else:
        return False

def CleanUp( text ):
    '''CleanUp punctuation in text to isolate words'''
    text = text.lower( )
    text = text.replace("'", '') 
    # Replace other punctuation by space chars
    punc = '-:?!.,;<>=()[]"*~@#$%^&'
    for c in punc:
        text = text.replace( c, ' ')       
    return text

def main():
    name = input('Filename (with .txt): ')
    f = open(name,'r' )
    text = f.read()
    text = CleanUp( text )
    text = text.lower()

    Lwords = text.split() #list of words
    #To test: print( Lwords[ : 10] )
    
    PalUniq = []
    for i in Lwords:
 
        if IsPalindrome(i) and (i not in PalUniq):
            PalUniq.append(i)
    PalUniq.sort()

    print("-*-")
    print(len(PalUniq), "palindromes in", name + ":")
    for x in PalUniq:
        print(x)
    

    
    
            
    f.close()

main()
