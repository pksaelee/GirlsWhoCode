#GLOBAL VARIABLES
codeList =[]
realList = []


#FUNCTIONS
def createCodeWords():
    codingWords = True
    while codingWords:
        print("Would you like to add a word to your code words? (y/n)")
        ans = input().lower()
        if ans == "y":
            print("What is the real word?")
            real = input().lower()
            realList.append(real)
            print("What is the code word?")
            code = input().lower()
            codeList.append(code)
        elif ans == "n":
            print("Your code words have been saved.")
            codingWords = False
        else:
            print("Security breached! Shutting down.")
            exit()
def encryptMessage():
    print()
    print("__________________________________________________________________")
    print()
    print("What is the message you would like to encrypt?")
    message = input().lower()
    messageList = message.split()
    codedMessage = ""
    for words in messageList:
        for realWord in realList:
            if (words == realList):
                #print("Encrypted Text:")
                codedMessage = codedMessage + "" + codeList[0]
            else:
                codedMessage = codedMessage + "" + words
#RUNNING CODE
createCodeWords()
encryptMessage()

   
