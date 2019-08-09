import re
import sys
prog = re.compile('(a|b)*$')
lm=str(input())
if prog.match(lm):
    print ("yes")
else:
    print ("no")
