#zip
'''
lang=["python","java","C"]
creator=["Guido Van Rossum","James Gosling","Denis"]
output3={x:y for x,y in zip(lang,creator)}
print(output3)
'''


lang=["python","java","C","linux"]
creator=["Guido Van Rossum","James Gosling","Denis","Linus"]
output4={x:y for x,y in zip(lang,creator) if x!="linux"}
print(output4)

nums=[1,2,3]
output5={x:x*x for x in nums}
print(output5)

