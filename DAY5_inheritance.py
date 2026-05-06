# Inheritance
#Parent or base class
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def __str__(self):
        return f"{self.name} | {self.age} years old"
# Child Class
class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking")
    def fetch(self):
        print(f"{self.name} is fetching the ball")
# Child Class
class Cattle(Animal):
    def __init__(self, name, age,givesmilk):
        super().__init__(name, age)
        self.givesmilk = givesmilk
    def describe(self):
        if self.givesmilk:
            print(f"{self.name} is a diary animal")
        else:
            print(f"{self.name} is not a diary animal")

    def mow(self):
        print(f" {self.name} is mowing!!")

# creating objects
dog = Dog("leo",3,"shi stzu")
cattle1 = Cattle("cow",5,True)
cattle2 = Cattle("Bull",7,False)

# check inheritance
print(dog)
dog.eat()
dog.sleep()
dog.bark()
dog.fetch()

print()

#for cattle
print(cattle1,"\n",cattle2)
cattle1.eat()
cattle2.sleep()
cattle1.mow()
cattle2.eat()
cattle1.describe()
cattle2.describe()