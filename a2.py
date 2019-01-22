
import support
while True:
    print("enter any one of the following option\n e)encrypt\n d) decypt\n a) automatically decrypt some text\n q) quit")
    o=(input("enter option="))
    if o=="E" or o=="e":
        sen=(input("enter sentence="))
        off=int(input("enter offset="))
        if off==0:
            for i in list(range(1,25)):
                print(support.encrypt(sen,i))
        else:
            ans=support.encrypt(sen,off)
            print(ans)
    elif o=="d" or o=="D":
        sen=(input("enter sentence="))
        off=int(input("enter offset="))
        ans=support.decrypt(sen,off)
        print(ans)
    elif o=="a" or o=="A":
        sen=(input("enter sentence="))
        support.highdecrypt(sen)
    elif o=="q" or o=="Q":
        print("thanks for using!\n bye!!")
        break
    else:
        print("invalid input\n try again")
        continue
