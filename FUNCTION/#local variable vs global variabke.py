#local variable vs global variabke

a=10

def something():
    a=15
    print("inside fn" ,a) #inside variable a is called local variable and outside is called global variable its always print local variable first 

something()

print("outside" , a)