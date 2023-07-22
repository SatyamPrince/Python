#keyword variable length using for loop

def person(name, **data):
    print(name)
    
    for i,j in data.items():
        print(i,j)

person('satyam',Age =23,city = 'Mumbai' ,mob = 7529006120)
