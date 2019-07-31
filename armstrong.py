n=int(input())
sum=0
l=n
while l>0:
    dig=l%10
    sum+=dig**3
    l//=10
if n==sum:
    print("yes")
else:
    print("no")
    
