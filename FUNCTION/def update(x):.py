#function argument in integer // this value will not change because this is immutable

def update(x):

    x=8
    print(id(x))
    print("x",x)


a=10
print(id(a))
update(a)
print("a" a)