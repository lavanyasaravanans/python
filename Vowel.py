ch = input()
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("Vowel")
elif((ch>='a' and ch<='z') or (ch>='A' and ch<='z')):
    print("Consonant")
else:
    print("invalid")
