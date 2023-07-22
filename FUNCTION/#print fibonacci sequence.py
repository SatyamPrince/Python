#print fibonacci sequence

def feb(n):
    a=0
    b=1

    print(a)
    print(b)

    for i in range(n):
        c=a+b
        print(c)
        c=a+b
        a=b
        b=c




feb(14)
