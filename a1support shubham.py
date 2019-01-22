"""Supporting functions for assignment 1

CSSE1001
Semester 2, 2018
"""
import a1_support
from functools import partial

def load_words(word_file):
    """list<str> Returns a list of words loaded from a word file

    Parameter:
        word_file (str): The filename of the word file
    """
    with open(word_file) as f:
        lines = [line.strip() for line in f]
        return [word.strip() for word in lines if word]


_is_word_english = partial(lambda words, word: word in words, set(load_words('words.txt')))



def encrypt(sen,off):
    for i in sen:
        if i.isupper:
            flag=ord(i)+off
            if flag>90:
                flag=flag-90+65-1
            
        elif not i.isupper:
            flag=ord(i)+off
            if flag>122:
                flag=flag-122+97-1
            ans=ans+char(flag)
        else:
            ans=ans+i
        ans=ans+char(flag)

def decrypt(sen,off):
    for i in sen:
        if i.isupper:
            flag=ord(i)-off
            if flag<65:
                flag=-flag+90+65-1
            
        elif not i.isupper:
            flag=ord(i)+off
            if flag>122:
                flag=flag-122+97-1
            ans=ans+char(flag)
        else:
            ans=ans+i
        ans=ans+char(flag)

def highdecrypt(sen):
    d=tuple()
    for i in list(range(1,26)):
        c=decrypt(sen,i)
        j=split(c)
        lenj=len(j)
        for k in list(range(lenj)):
            if j[k] in load:
                f=1
            else:
                f=0
                break
            if f=1:
                d=d+(k,)
                
            
        
    
