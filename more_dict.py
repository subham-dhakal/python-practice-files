all={"abc":123,"Hello":True}
all["abc"]=[1,2,3]
all["Hello"]=False
all.update({"world":True})
print(all.get("world"))
print(all.get("xyz","xyz not in dictionary"))
print(all)

phonebook={"subham":981453458,"dad":9853453409,"mom":9817233455}
def fun(x):
    y=str(input("Enter the name\n"))
    name=x.get(y,"Inalid name")
    print(name)

fun(phonebook)
