class vehicle :
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

        print(f'{self.brand} is moving at {self.speed} km/h')
    
   
class car(vehicle):
     def __init__(self, brand, speed, has_ac):
        super().__init__(brand, speed)
        self.has_ac = has_ac
        
        print(f'car has ac:{self.has_ac}')

        print(f'{self.brand} is moving at {self.speed} km/h and has ac: {self.has_ac}')

car1 =car("harrier",140,True)

class bike(vehicle):
    def __init__(self,brand,speed,kickstart):
        super().__init__(brand,speed)
        self.kickstart=kickstart

        print(f'bike has kickstart:{self.kickstart}')

        print(f'{self.brand} is moving at {self.speed} km/h and has kickstart: {self.kickstart}')

bike1 =bike("pulsar",120,True)





