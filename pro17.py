l,k=map(int,input().split())
m=[int(i) for i in input().split()]
n=[]
for i in range(l+1):
  if i==0:
    for i in range(0,len(m)):
      for j in range(i+1,len(m)):
       if m[i]==m[i+1] and  m[i] is not n:
         n.append(m[i])
d=0   
for i in range(len(n)):
  d=d+n[i]
if d<=k:
  print("yes")
else:
  print("no")
