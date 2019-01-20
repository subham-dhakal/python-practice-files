def squared(x):
    return x*x

lists=[1,2,3,4]
f=map(squared,lists)
print(list(f))

lists1=list(range(0,9))
print(list(filter(lambda x:x%2!=0,lists1)))
