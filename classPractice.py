class Point:
	def reset(self):
		self.x=0
		self.y=0

p1=Point()
p2=Point()

p1.x=5   
p1.y=4

p2.x=3
p2.y=6

print(p1.x,p1.y)
p1.reset()
print(p1.x,p1.y)