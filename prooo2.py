from itertools import combinations
x,a=map(int,input().split())
m=len(str(x))
s=list(combinations(str(x),m-a))
s=sorted(s)
print(*s[0],sep='')
