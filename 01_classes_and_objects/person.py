class Person:
	def __init__(self, name, age,role,contact_no):

		self.name = name
		self.age = age
		self.role = role
		self.contact_no = contact_no



	def display_info(self):
		print(f"""My name is {self.name} and i’m {self.age} years old.
		I’m working as a {self.role} you can contact me {self.contact_no}""")

	def update_contact(self, new_contact):
		self.contact_no = new_contact
		print(f"Contact number updated to {self.contact_no}")



person1 = Person("Dipak Bist",27,"QA Automation",21223332233)

person2 = Person("John Doe",30,"Software Engineer",9876543210)

person1.display_info()
person1.update_contact(9823333333333320)
person2.display_info()
person2.update_contact(9823333333333321)

