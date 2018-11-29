# Tweets.py
# Yining Hua
# Assignment 6
# A program search through a Twitter-stream file
# of about 9000 tweets that Joe gathered on October 20,23,24

def main():
    print("You might copy file names from here:\nTweets_short_20Oct2017.txt\nTweets_long_Oct2017.txt\r")
    filename = input("Enter your filename here:")
    print(filename+"\r")
    file = open("Tweets_long_Oct2017.txt", 'r')
    
    text = []
    hashUnique = []
    hashMul = []

    for line in file:
        line = line.lower()
        if (line[0:4]=="text"):
            #select lines begin with 'text' and 'hashtag', store them in new lists
            text.append(line)
        if(line[0:7]=="hashtag"):
            temp = eval(line[10:-1])
            for seg in temp:
                if seg not in hashUnique:
                    #for task 2, a list of hashtag index    
                    hashUnique.append(seg)
                else:
                    #for task 3, a list of hashtags taht appear for more than 1ce
                    hashMul.append(seg)

    file.close()
    
    #sort the two lists alphabetically
    hashUnique.sort()
    hashMul.sort()

    

#TASK 1
    #call the function charSearch which returns the times one char appears in a text
    print("trump",": occures",charSearch("trump",text),"times in tweets text")
    print("clinton",": occures",charSearch("clinton",text),"times in tweets text")
    print("halloween",": occures",charSearch("halloween",text),"times in tweets text")

#TASK 2
    
    print("\r",len(hashUnique),"unique hashtags","\nLast 10 alphabetically:\n"+"-"*40)
    for q in range(-10,0):
        print(hashUnique[q])

        
#TASK 3
    #create 2 lists for storing the hashtags and their appearing times 
    index = []
    for element in hashMul:
        if element not in index:
            index.append(element)
            
    index_time = []
    for elementi in index:
        times = hashMul.count(elementi)+1
        index_time.append(times)

        
    #call the function combine to join the two lists into a list of tuples
    combined = combine(index_time,index)
    #sort the list by the 1st element of each tuple(appearing times)
    combined.sort(key = lambda x:x[0],reverse = True)

    print("\r10 most commonly occurring hashtags:\n"+"-"*40)
    for tempc in range(0,10):
        print(combined[tempc])



#Functions:

def charSearch(char,texts):
    '''return the times an assigned char appears in a text
'''
    num = 0
    for a in texts:
        num+=a.count(char)
    return num

def CleanUp( text ):
    '''CleanUp punctuation in text to isolate words
    '''
    text = text.lower( )
    text = text.replace("'", '') 
    # Replace other punctuation by space chars
    punc = '-:?!.,;<>=()[]"*~@#$%^&'
    for c in punc:
        text = text.replace( c, ' ')       
    return text

def combine(times,index):
    '''combine 2 lists
'''
    combined = [];
    for i in range(len(times)):
        temp = [times[i],index[i]];
        combined.append(temp);
    return combined;

main()






