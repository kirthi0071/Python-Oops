class GrandParent: 
    def G_name(self,G_name):
        self.G_name = G_name
        print(f'Grandparent name is {self.G_name}')

class Parent(GrandParent):
    def P_name(self,P_name):
        self.P_name = P_name
        print(f'{self.G_name} is the parent of {self.P_name}')


class Child(Parent):
    def C_name(self,C_name):
        self.C_name =C_name
        print(f'{self.C_name} is a child of {self.P_name} and grandchild of {self.G_name}')


era =Child()
era.G_name("chandrasekar")
era.P_name("vijay")
era.C_name("sanjay")

era =Child()
