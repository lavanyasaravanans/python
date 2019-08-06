i=int(input())
l=(input().split())[0:i]
o=i//2
if i>3:
  if(o%2==0):
    print("yes")
  else:
    print("no")
else:
  if(i==3):
    print("yes")
  else:
    print("no")
