pn=int(input())
if pn>1:
    for i in range(2,pn//2):
        if pn%i==0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
