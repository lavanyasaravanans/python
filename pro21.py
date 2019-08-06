x=int(input())
l=(input().split())[0:x]
o=x//2
if x>3:
  if(o%2==0):
    print("yes")
  else:
    print("no")
else:
  if(x==3):
    print("yes")
  else:
    print("no")
