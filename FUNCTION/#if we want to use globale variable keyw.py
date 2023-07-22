#if we want to use globale variable keyword global 

a=10

def something():

    global a 
    a=15
    print("inside", a)
 
something()

print("outside", a)