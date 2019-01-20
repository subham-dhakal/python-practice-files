store={}
def count_chars(str):
    for char in str:
        if char in characters:
            print(char,str.count(char))


str = input("enter a string ")
characters={x for x in str}
count_chars(str)