def minl(s,x):
    min=len(s[0])
    for i in range(1,x):
        if len(s[i])<min:
           min=len(s[i])
    return(min)
def commonprefix(s,x):
    minlen=minl(s,x)
    result=""
    for i in range(minlen):
        crn=s[0][i]
        for j in range(1,x):
            if(s[j][i]!=crn):
                return result
        result=result+crn
    return(result)
if __name__=="__main__":
    no=int(input())
    s=[]
    for n in range(0,no):
        ss=str(input())
        s.append(ss)
    x=len(s)
    final=commonprefix(s,x)
    if(len(final)):
        print(final)
    else:
        print("")
