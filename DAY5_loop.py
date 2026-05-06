# # DAY 5- OOPS CONCEPT
# # defining a class
# class Person:
#     def __init__(self,name,age,location): # _init_ - Constructor Method(runs auto when object is created)
#         self.name = name
#         self.age = age
#         self.location = location
#     # Method - function inside class
#     def introduce(self):
#         print(f"Hello! I am {self.name},{self.age} years old from {self.location}")
#     def birthday(self):
#         self.age +=1
#         print(f"Happy birthday {self.name}, you are now{self.age}")
#     def __str__(self): # defines what an object looks like when printed
#         return f"Person({self.name},{self.age},{self.location})"
# # creating objects
# person1 = Person("Hari",26,"Luton")
# person2 = Person("John",30,"leeds")
# person3 = Person("Will",33,"London")
# # calling methods
# person1.introduce()
# person2.introduce()
# person3.introduce()

# # each object is independent
# person1.birthday()
# person2.introduce()
# person1.introduce()

# #type of object
# print(person1)
# print(person3)

# Class Attribute & Instace Attribute

class BankAccount:
    bank_account = "PYTHON BANK" # class attribute - shared by all objects
    def __init__(self,owner,balance=0):
        self.owner = owner          # instance attribute
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"You have deposited {amount} to the account{self.owner} Balance Updated: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficent funds! your current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn {amount} from {self.owner},remaining balance: {self.balance}")
    def __str__(self):
        return f"{self.bank_account} | {self.owner} | {self.balance}"

# creating account
account1 = BankAccount("hari",1000)
account2 = BankAccount("James",10)

# print accounts
print(account1)
print(account2)

# Transactions
account1.withdraw(255)
account2.deposit(100)
account2.withdraw(111)

#Class attribute is shared
print(f"\n Bank name: {BankAccount.bank_account}")
print(f"Account 1 Bank: {account1.bank_account}")
print(f"Account 2 Bank: {account2.bank_account}")
