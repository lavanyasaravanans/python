m=int(input())
for x in range(1<<m):
    k=bin(x)[2:]
    k="0"*(m-len(k))+k
    print(k)
