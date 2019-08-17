from string import ascii_lowercase as asc_lower
def check(word):
    return set(asc_lower)-set(word.lower())==set([])
wo1=str(input(""))
if(check(wo1)==True):
    print("yes")
else:
    print("no")
