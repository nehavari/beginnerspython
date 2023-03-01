class MyClass:

	def __init__(self, name, email):
		self.name = name
		self.email = email
	
	@staticmethod	
	def factory(cls):
		return cls('Neha Vari', 'myemail@email.com')
		
	@staticmethod	
	def isvalid(email):
		return '@' in email
		
		
def main():
	print(MyClass.isvalid('@'))
	myinstance = MyClass.factory(MyClass)
	print(myinstance.name, myinstance.email)
	
	
if __name__ == '__main__':
	main()
	
