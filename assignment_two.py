def percent(percente):
    if percente>=40:
        print("Pass")
        if percente>80 :
            print("You got distinction")
        elif percente>=70 and percente<50 :
             print("You got first division")
        elif percente<50 :
            print("You got 2nd division")

    else :
        print("Fail")

percent(40)