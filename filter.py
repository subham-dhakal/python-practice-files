from functools import reduce

nums=[24,46,2,5,4,2,345,6,23,45,70]

# Filter the list based on the condition of lamda function
even=list(filter(lambda a :a%2==0,nums))

print(even)




n=[2,3,4,5,6,9]

# Maps the n acccording to the lambda function 
sq=list(map(lambda b : b*b,n))
print(sq)


# Reduce prints the single value by adding all 
sum=reduce(lambda a,b: a+b,sq)
print(sum)