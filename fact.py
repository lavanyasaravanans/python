num=int(input())
g=1
if num==0:
    print("1")
else:
    for i in range(1,num+1):
        g=g*i
    print(g)
