def reverse(str): 
    return ' '.join(w[::-1] for w in str.split(" "))
str=input("")
print(reverse(str))
