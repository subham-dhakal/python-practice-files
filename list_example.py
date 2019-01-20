x=[3,4,1,"a","b"]
index_a=x.index("a")
print(index_a)

ext=["p","q"]
x.extend(ext)
print(x)

print(x.pop())

x.insert(6,"xyz")

x.remove(1)

if 88 in x:
    print("88 is in the list")
else:
    print("88 not in list")

print(len(x))

