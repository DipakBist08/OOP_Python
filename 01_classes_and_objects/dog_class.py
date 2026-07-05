class Dog:
    def __init__(self,name,breed,dog_age,owner_name,owner_contact):
        self.name = name
        self.breed = breed
        self.age = dog_age
        self.owner_name = owner_name
        self.owner_contact = owner_contact

    def bark(self):
        print(f"{self.name} says Woof Woof!")



    def have_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")



    def display_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}, Owner: {self.owner_name}, Contact: {self.owner_contact}")
    



dog1 = Dog("Puppy","German Shepherd",4,"John Doe","123-456-7890")
dog1.bark()
dog1.have_birthday()    
dog1.display_info()

