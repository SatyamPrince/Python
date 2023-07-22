#access global variable inside funtion 

a=10

def something():
    
    print("inside", a)
something()

print("outside", a)