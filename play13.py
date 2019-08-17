i=int(input())
m=0
while(i>0):
    r=i%10
    m=m+r*r
    i=i//10
print(m)
