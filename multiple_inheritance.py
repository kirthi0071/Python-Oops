class ElectricalVehicle:
    def charge(self):
        print("charging the battery")
    
class Connected:
    def connect_to_wifi(self):
        print("connecting to wifi")

class SmartCar(ElectricalVehicle, Connected):
    def self_drive(self):
        print("self driving mode activated")

car = SmartCar()

car.charge()
car.connect_to_wifi()
car.self_drive()

#mro-method resolution order ( decides the parent(same method) to be used from left to right)
