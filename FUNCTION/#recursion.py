#recursion 

import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit()) #by default its have 1000 limit if we want to increase that we have too use first three line of code

i=0
def greet():
    global i
    i=i+1
    print("Hello", i)
    greet()

greet()



