class calculator:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def addition(self):
		return self.a+self.b
	def subtraction(self):
		return self.a-self.b
ob=calculator(2,4)
print ob.addition()
print ob.subtraction()
