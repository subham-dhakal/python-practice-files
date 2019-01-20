class Animal:
	def eat(self):
		print("eat method")

dog=Animal()
dog.eat()
#print(dog.__dict__)
#giving the attribute of the object

dog.name="rocky"
dog.age=3
dog.sex="male"
print(dog.__dict__)