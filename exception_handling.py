def calcualte(num):
    try:
        print(100/num)
    except ZeroDivisionError:
        print("num value cant be zero")

    finally:                            #It will always be printed
        print("Code executes")   # #Use case is it can be helpful to close the file if consumed


calcualte(1)
calcualte(0)