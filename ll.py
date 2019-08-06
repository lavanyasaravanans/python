x=int(input())
o=list(map(int,input().split()))[0:x]
o.sort(reverse=True)
i=0
while i<x:
    print(o[i],end="\n")
    i+=1
