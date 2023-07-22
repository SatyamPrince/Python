#global and local variable inside a function 
#globals()['a']
a=10
print(id(a))

def something():
    a=9

    x=globals()['a']
    print(id(x))
    
    print(a)

    globals()['a']=15      #if we want to use local and global variable inside a fn keywords called globals
    

    
something()


print(a)
