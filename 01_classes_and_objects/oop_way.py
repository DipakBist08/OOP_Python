class Car:
    def __init__(self,make,model,speed=0):
        self.make = make
        self.model = model
        self.speed = speed

    def accelerate(self,amount):
        self.speed += amount
        return self




car1 = Car("Toyota","Carmy")

car1.accelerate(50)
print(car1.speed)
print(car1.make)
print(car1.model)

