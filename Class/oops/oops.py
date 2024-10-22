class Animal:
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        self.__age = age
        
    # Another instance method
    def get_age(self):
     return f"{self.name} is {self.age} years old."
    def __str__(self):
        return f"{self.name},{self.age}\n{self.__age}"



class Dog(Animal) :     # Inheriting Animal Class
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
  
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
  


class Cat(Animal): # Inheriting Animal Class
    # Class attribute (shared by all instances)
    species = " Pantheras"
   
    # Instance method
    def meu(self):
        return f"{self.name} says meu!"
   
   
   
# Creating instances (objects) of the Dog class
dog1 = Dog("Buddy", 3)
cat1 = Cat("C1", 2)
dog2 = Dog("Charlie", 5)

# Accessing attributes and methods
print(dog1 , "this is dog 1")
print(dog1.age)
# print(dog1.__age)        # Private Property by __ double undersore     
print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris

print(cat1)