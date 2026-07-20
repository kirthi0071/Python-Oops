class Student:
    college_name = "IIT Bangalore"       # CLASS attribute -> defined outside __init__, shared by ALL objects

    def __init__(self, name, roll_no):
        self.name = name                  # INSTANCE attribute -> unique per object
        self.roll_no = roll_no            # INSTANCE attribute -> unique per object


s1 = Student("Kirthi", 101)
s2 = Student("Ravi", 102)

print(s1.name, s1.roll_no, s1.college_name)   # Kirthi 101 IIT Bangalore
print(s2.name, s2.roll_no, s2.college_name)   # Ravi 102 IIT Bangalore

print(s1.college_name is s2.college_name)      # True -> literally the SAME value shared, not two separate copies
