import support
while True:
    print "enter any one of the following option\n e)encrypt\n d) decypt\n a) automatically decrypt some text\n q) quit"
    o=input("enter option=")
    if o=="E" or o=="e":
        sen=input("enter sentence=")
        off=input("enter offset=")
        if off==0:
            for i in list(range(1,25)):
                print al_support.encrypt(sen,i)
        else:
            ans=al_support.encrypt(sen,off)
            print ans
    elif o=="d" or o=="D":
        sen=input("enter sentence=")
        off=input("enter offset=")
        ans=al_support.decrypt(sen,off)
        print ans
    elif o=="a" or o=="A":
        sen=input("enter sentence=")
        load=load_words(words.txt)
        highdecrypt(sen)
    elif o=="q" or o=="Q":
        break
    else:
        print("invalid input\n try again")
        continue
