#list comprehension is used


'''

my_str="abc"
output=[(x,y) for x in my_str for y in range(len(my_str))]
print(output)
'''
nums=[5,10,15,20,25]
output1=[x for x in enumerate(nums)]
print(output1)