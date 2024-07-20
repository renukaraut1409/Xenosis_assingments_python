
class Person:

    # instance attributes
    def __init__(self):
        self.name = ""
        self.age = 0

    #method to set data for a person instance
    
    def getData(self,name,age):
        self.name = name
        self.age = age

    # method to display details of a person instance    

    def displayDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)

    #taking input

name = input("Enter the name of person:")
age = int(input("Enter the age of the person:"))       
    

    # creatin a object pf person class
p1 = Person()
p1.getData(name,age)
p1.displayDetails()
