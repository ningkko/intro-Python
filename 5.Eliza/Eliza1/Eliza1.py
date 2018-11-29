# Eliza1.py
# You Jeen Ha & Yining Hua
# Lab_5 (October 12, 2017)
# This lab implements a "baby" version of Eliza, a chatbot.

def main():
    print("Eliza: Hello! How are you?")
    for i in range(25):
        chat_str = input("Chat: ")
        chat_str = chat_str.lower()
        if ("bye" in chat_str) or ("quit" in chat_str):
            print("Eliza: Ok, I'll talk to you later!")
            break
        elif ("feel" in chat_str) or ("feeling" in chat_str):
            print("Eliza: Oh, I see. Tell me more about these feelings.")
        elif ("mother" in chat_str):
            print("Eliza: How is your mother?")
        elif ("father" in chat_str):
            print("Eliza: How is your father?")
        elif ("sorry" in chat_str):
            print("Eliza: How do you feel when you apologize?")
        elif (chat_str[-1] == "?"):
            print("Eliza: ...Ummm?")
        elif (chat_str[-1] == "!"):
            print("Eliza: You seem quite emphatic!")
        else:
            print("Eliza: ヾ(=^▽^=)ノ Tell me more!")

main()
