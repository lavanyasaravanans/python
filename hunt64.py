x=int(input())
o=x
m=0
while o!=0:
  if(o/1000)>=1:
    m=m+1
    o=o-1000
  elif (o/500)>=1:
    m=m+1
    o=o-500
  elif (o/100)>=1:
    m=m+1
    o=o-100
  elif (o/50)>=1:
    m=m+1
    o=o-50
  elif (o/10)>=1:
    m=m+1
    o=o-10
  elif o<10:
    m=m+o
    o=o-o
print(m)
