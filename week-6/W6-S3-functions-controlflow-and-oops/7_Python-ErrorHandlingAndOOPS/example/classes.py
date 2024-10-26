# ----------------------------
# Python Classes and Objects
# ----------------------------


# 1. Defining a Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return f"{self.name} is {self.age} years old."


# 2. Creating Objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# 3. Accessing Attributes and Methods
print("Dog 1 details:")
print(dog1.get_age())  # Output: Buddy is 3 years old.
print(dog1.bark())  # Output: Buddy says woof!

print("\nDog 2 details:")
print(dog2.get_age())  # Output: Max is 5 years old.
print(dog2.bark())  # Output: Max says woof!

# 4. Modifying Attributes
dog1.age = 4
print("\nUpdated Dog 1 details:")
print(dog1.get_age())  # Output: Buddy is 4 years old.


# 5. Inheritance
class Labrador(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return f"{self.name} is {self.color}."

    def bark(self):
        return f"{self.name} says woof woof!"


# 6. Creating Objects of the Subclass
labrador1 = Labrador("Buddy", 3, "brown")
labrador2 = Labrador("Max", 5, "black")

# 7. Accessing Attributes and Methods of the Subclass
print("\nLabrador 1 details:")
print(labrador1.get_age())  # Output: Buddy is 3 years old.
print(labrador1.get_color())  # Output: Buddy is brown.
print(labrador1.bark())  # Output: Buddy says woof woof!
