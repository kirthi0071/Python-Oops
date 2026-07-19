class Person():
    def eat(self):
        print("Person is eating.")

class Employee(Person):
    def work(self):
        print("Employee is working.")

class SportsPerson():
    def train(self):
        print("Sports person is training.")

class SportsEmployee(Employee, SportsPerson):
    def earn_medals(self):
        print("Sports employee is earning medals.")

AtheleteEmployee = SportsEmployee()

AtheleteEmployee.eat()
AtheleteEmployee.work()
AtheleteEmployee.train()
AtheleteEmployee.earn_medals()
