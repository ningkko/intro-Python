# Eliza2.py
# Yining Hua
# Assignment 5
# A better developed Eliza

def main():
    print("Eliza: Hello! How are you?")
    #Special phrases in the input of the user that we concern followed each by their response
    phrase1 = ["i need","Would it really help you to get"]
    phrase2 = ["i think",'Do you doubt that']
    phrase3 = ['i am','how long have you been']
    phrase4 = ["i'm",'how long have you been']


    for i in range(100):
        #get the input and turn it into a lowercase version
        chat_str = input("Chat: ")
        chat_str = chat_str.lower()

        #quit if the user says bye
        if ("bye" in chat_str or "see you" in chat_str):
            print("I'll miss you..See you.")
            break
        #quit when user says"quit" and prevent from quitting when detect "quite"
        elif (chat_str[-4:-1]+chat_str[-1]=="quit"):
            print("Eliza: Ok, then talk to you later.")
            break
        else:
        #check if special phrases are contained at the beginning, return a special response if yes
            if Begins(phrase1,chat_str):
                SpecialAns(phrase1, chat_str)
            elif Begins(phrase2,chat_str):
                SpecialAns(phrase2, chat_str)
            elif Begins(phrase3,chat_str):
                SpecialAns(phrase3, chat_str)
            elif Begins(phrase4,chat_str):
                SpecialAns(phrase4, chat_str)
            #responses to normal cases
            elif ("feel" in chat_str) or ("feeling" in chat_str):
                print("Eliza: Tell me more about such feelings.")
            elif ("mother" in chat_str):
                print("Eliza: How's your mother?")
            elif ("father" in chat_str):
                print("Eliza: How's your father?")
            elif ("sorry" in chat_str):
                print("Eliza: How do you feel when you apologize?")
            elif (chat_str[-1] == "?"):
                print("Eliza: ...Ummm Why do you ask like that?")
            elif (chat_str[-1] == "!"):
                print("Eliza: You seem quite certain huh")
            else:
              print("Eliza: Ummm..Interesting. Tell me more?")


#takes two parameters 1.the special phrase, 2. the input sentence of the user
def Begins(phrase, chat_str):
    '''Begins(phrase, chat_str):Check whether parameter phrase is at the beginning of parameter chat_str
'''
    #Check are there are special phrases at the beginning of the input sentence
    if chat_str.find(phrase[0])==0:
        return True
    else:
        return False

        
def SpecialAns(phrase,chat_str):
    '''SpecialAns(phrase,chat_str): take a phrase and a string a parameters, print out the revised version of this string.
'''
    #Print the corresponding respinse to each special phrase and reflect the remaining part of the sentence
    print ("Eliza:",phrase[1]+reflection(chat_str.replace(phrase[0],"")))


def reflection(s):
    '''reflection(s): Change "you" into "me","yours" into "mine","your" into "the so called" &etc.. in the input sentence s
'''
    
    if "your" in s:
        s = s.replace(" your "," the so called ")
    if "my" in s:
        s = s.replace(" my "," the so called ")
    if "you" in s:
        s = s.replace(" you "," me ")
    if "i" in s:
        s = s.replace(" i "," you ")
    if "i am" in s:
        s = s.replace(" i am "," you are ")
    if "i'm" in s:
        s = s.replace(" i'm "," you're ")
    if "mine" in s:
        s = s.replace(" mine "," yours ")
    return s


main()

