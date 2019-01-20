class Employee:
	no_of_employee=0
	
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
		Employee.no_of_employee+=1



	@classmethod    #Decorators .  #It is class method
	                     #(classname,inputed value)
	def gen_emp_from_string(cls,inp):
		name,salary=inp.split("-")
		return cls(name,salary)

e=Employee.gen_emp_from_string("Subham-20000")


print(e.__dict__)
