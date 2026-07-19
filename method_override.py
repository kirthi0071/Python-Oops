class greet:
    def greeting(self):
        print("hello")

class indian(greet):
     def greeting(self):
        print("namaste")

class french(greet):
    def greeting(self):
        print("bonjour")

class german(greet):
    def greeting(self):
        print("hallo")

class english(greet):
    pass

I =indian()
F=french()
G=german()
E=english()

I.greeting()   # "namaste"     -> overridden
F.greeting()   # "bonjour"     -> overridden
G.greeting()   # "hallo"       -> overridden
E.greeting()  # "hello"
