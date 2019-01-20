class Student:
	def __init__(self,name,semester):   #initializer
		self.name=name
		self.semester=semester
		
	def update(self):
		self.semester=self.semester+1




obj=Student('subham',3)

print(obj.name,obj.semester)

obj.update()    #Calling update method

print(obj.name,obj.semester)
