def create_car(make,model,speed):
    return { "make":make,"model":model,"speed":speed }


def accelerate(car,amount):
    car["speed"] += amount
    return car

car1 = create_car("Toyota","Camry",0)
car1 = accelerate(car1,50)
print(car1)