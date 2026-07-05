class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_info(self):
        print(f"Name:{self.name}, Roll_No:{self.roll_no}, Marks:{self.marks}")
    


student1 = Student("RAM",101,75)
student1.display_info()
