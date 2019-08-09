r,m=map(int,input().split())
l=list(map(int,input().split()))
n=[]
for i in range(0,m):
    d = []
    d=list(map(int,input().split()))
    s = l[d[0]-1]
    for j in range(min(d),max(d)):
        s=s^l[j]
    n.append(s)
for i in range(0,len(n)):
    print(n[i]) 
