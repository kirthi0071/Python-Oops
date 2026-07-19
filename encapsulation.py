class Student:
    def __init__(self, name, marks):
        self.name = name
        self.school = "SKV"
        self.__marks = marks

    def add_marks(self, marks):
        if (self.__marks + marks) > 100 or (self.__marks + marks) < 0:
            print("invalid marks")
        else:
            self.__marks += marks
            print(f'{self.name} has secured {self.__marks} marks in the exam')

    def show_marks(self):
        print(f'{self.name} has secured {self.__marks} total marks in the exam')


student1 = Student("kirthi", 90)

student1.show_marks()        # kirthi has secured 90 total marks in the exam
student1.add_marks(15)       # invalid marks -> because 90+15=105 > 100
student1.add_marks(5)        # kirthi has secured 95 marks in the exam
