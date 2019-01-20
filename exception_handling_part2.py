def printHello():
    print("Hello")

def printWorld():
    print("World")

def Default():
    print("Enter valid arguments")

switch={1:printHello,2:printWorld}

ask=int(input("Please any number "))

try:
    switch[ask]()
except KeyError:
        Default()