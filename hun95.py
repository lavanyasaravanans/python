l=int(input())
for i in range(2,l+1):
    n=0
    for a in range(2,i//2+1):
        if(i%a==0):
            n=n+1
    if(n<=0):
        print(i,end=" ")
