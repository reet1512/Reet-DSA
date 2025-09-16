class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(" hi there i am " + self.name)

john = Person("John Smith")
print(john.name)
john.talk()