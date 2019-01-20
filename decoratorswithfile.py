'''
class Student:
students=[]
	with open('stddata.txt','r') as fd:
		for each in fd:
			

	def __init__(self,name,semester):
		self.name=name
		self.semester=semester

	@classmethod
	def read_data(cls,inp):
  		name,semester=inp.split("-")
  		return cls(name,semester)

s1=Student.read_data(data)
print(s1.__list__)
'''


class Student:
	def __init__(self,name,semester):
		self.name=name
		self.semester=semester

	@classmethod
	def read_data(cls,inp):
  		name,semester=inp.split("-")
  		return cls(name,semester)
students=[]
print(len(students))
with open("stddata.txt","r") as data:
	for each in data:
		students.append(Student.read_data(each))

print(students)



