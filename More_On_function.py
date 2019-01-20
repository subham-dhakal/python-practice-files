def f1(x):
    print(x*x*x)

def f2(a="Hello"):
    print(a)

def f3():
    print("It has no arguments")

def f4(*args):
    total=0
    for x in args:
        total+=x

    print(total)

def f5(**kwargs):
    sum=0
    for k,v in kwargs.items():
        sum+=kwargs.get(k,"Error")

    print(sum)

f1(3)
f2()
f3()
f4(1,2,3,4,5,6,7,8,9)
f5(x=5,y=10,z=25)
