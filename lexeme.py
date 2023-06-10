import re
from Pattern import Pattern
from tokenizer import tokens


def Closing(ch):
    print(s[ch])
    i=ch + 1
    while(s[ch]!=s[i] and ch < len(s)):
        i=i+1
    print(s[i])
    if(s[ch]==s[i] and s[ch]!= "##"):
        lexeme.append(s[ch:i+1])
        return i+1
    else:
        return -1

def check_lexeme(word):
    if(p1.is_keyword(word)):
        return 'keyword'
    elif(p1.is_operator(word)):
        return 'operator'
    elif(p1.punctuation(word)):
        return "punctuation"
    elif(p1.is_float(word)):
        return 'float-const'
    elif(p1.integer(word)):
        return 'int-const'
    elif(p1.identifier(word)):
        return 'identifier'
    elif(p1.string_constant(word)):
        return 'string-const'
    else :
        print("ERROR: The Word: {} is not valid lexeme".format(word))
        return False

def Scanner():
    word=''
    ch=0
    while ch < len(s):
        
        if s[ch]==" " :
            ch=ch + 1
            continue
        if s[ch]=="'" or s[ch]=='"' or s[ch] =="##" :
            index=Closing(ch) 
            if index != -1:
                ch=index
                continue
            else:
                print( "error" )
                break
        if s[ch]=="#":
            while s[ch]!= '\n':
                ch=ch+1
            ch=ch+1
            continue
        word = word + s[ch]
        
        if(word=="\n"):
            lexeme.append(word)
            symbol_table.append([word])
            word=''
        elif ((ch+1<len(s) and (p1.is_operator(s[ch+1])  or p1.punctuation(s[ch+1]or s[ch+1]=="\0")  or s[ch+1]==" ")) or p1.is_operator(word) or p1.punctuation(word)or ch==len(s)-1 ):
            classpart=check_lexeme(word)
            if classpart:
                lexeme.append(word)
                symbol_table.append([classpart,word])
            word=''
        ch=ch+1        
lexeme=[]
symbol_table=[]
p1=Pattern()
file  = open("read.txt", "r")
s=file.read()
Scanner()
print ("The scanned Words are:   {} ".format(lexeme))
t1=tokens()
t1.create_token(symbol_table)

