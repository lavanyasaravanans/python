def minl(n,x):
    min=len(n[0])
    for i in range(1,x):
        if len(n[i])<min:
           min=len(n[i])
    return(min)
def commonprefix(n,x):
    minlen=minl(n,x)
    result=""
    for i in range(minlen):
        crn=n[0][i]
        for j in range(1,x):
            if(n[j][i]!=crn):
                return result
        result=result+crn
    return(result)
if __name__=="__main__":
    no=int(input())
    n=[]
    for m in range(0,no):
        ss=str(input())
        n.append(ss)
    x=len(n)
    final=commonprefix(n,x)
    if(len(final)):
        print(final)
    else:
        print("")
