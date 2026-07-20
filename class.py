class Car:
    wheels =4 

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

p1 = Car("BMW","Black")
p2 = Car("Audi","White")

print(p1.wheels)
print(p2.wheels)

p2.wheels = 3
print(p2.wheels)
print(p1.wheels)
