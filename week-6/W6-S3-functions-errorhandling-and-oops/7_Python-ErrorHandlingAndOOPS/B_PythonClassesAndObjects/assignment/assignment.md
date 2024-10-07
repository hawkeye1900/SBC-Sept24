# 🐍 **Assignment: Mastering Python Classes and Objects**

## 🎯 **Objective**

In this assignment, you will deepen your understanding of classes and objects in Python. You will create a class with attributes and methods, utilize class inheritance, and implement encapsulation to manage data. This assignment will prepare you for object-oriented programming principles, allowing you to design and implement robust Python applications.

## 📚 **Key Learnings**

By completing this assignment, you will:

- 🔍 Understand the principles of object-oriented programming (OOP) and how they are implemented in Python.
- 🛠️ Create classes and instantiate objects with attributes and methods.
- 🔄 Utilize inheritance to create subclasses that extend the functionality of parent classes.
- 💡 Implement encapsulation to protect data and provide controlled access through methods.
- 📊 Understand the importance of constructors and destructors in managing object lifecycles.

## 👤 **User Story**

As a developer, I want to implement classes and objects in my Python applications to promote code reusability and maintainability through object-oriented programming.

## ✅ **Acceptance Criteria**

- **📝 Create a Python script named** YOURNAME_W6S3_7_B_assignment.py.
- The script should include:
  - **✨ Class Definition**: Define a class named `Car` with attributes such as `make`, `model`, and `year`. Include methods for displaying car information and updating attributes.
  - **🔄 Inheritance**: Create a subclass named `ElectricCar` that inherits from `Car` and includes additional attributes like `battery_size` and a method to display battery information.
  - **📦 Encapsulation**: Implement encapsulation by defining getter and setter methods for the `year` attribute in the `Car` class.
  - **🔗 Constructor and Destructor**: Use a constructor to initialize the car object and a destructor to display a message when the object is deleted.

## 🛠️ **Steps to Complete**

1. **📁 Create a new Python file**: Name it YOURNAME_W6S3_7_B_assignment.py.

2. **✨ Class Definition**:
   - Define a class named `Car` with the following attributes: `make`, `model`, and `year`.
   - Include a method named `display_info()` to print the car's details.
   - Include a method named `update_year(new_year)` to change the year of the car.

3. **🔄 Inheritance**:
   - Create a subclass named `ElectricCar` that inherits from `Car`.
   - Add an attribute `battery_size` and a method named `display_battery_info()` to show the battery size.

4. **📦 Encapsulation**:
   - Use the getter and setter methods in the `Car` class to access and modify the private `year` attribute.

5. **🔗 Constructor and Destructor**:
   - Define a constructor that initializes a car object and a destructor that prints a message when an object is deleted.
   - Example:
     ```python
     class Car:
         def __init__(self, make, model, year):
             self.make = make
             self.model = model
             self.__year = year

         def __del__(self):
             print(f"The car {self.make} {self.model} has been deleted.")
     ```

6. **📝 Test the Classes**:
   - Create instances of `Car` and `ElectricCar` and test their methods.
   - Example:
     ```python
     my_car = Car("Toyota", "Corolla", 2020)
     my_car.display_info()

     my_electric_car = ElectricCar("Tesla", "Model S", 2021, 100)
     my_electric_car.display_info()
     my_electric_car.display_battery_info()
     ```

## 🛠️ **Additional Challenges (Optional)**

- **🌀 Method Overriding**: Override the `display_info()` method in the `ElectricCar` class to include battery size in the output.
- **🛠️ Multiple Inheritance**: Create another subclass that demonstrates multiple inheritance by inheriting from both `Car` and another class, like `Vehicle`.

## 📎 **Additional Resources**

- [Python Classes and Objects Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python: Python Classes and Objects](https://realpython.com/python3-object-oriented-programming/)
- [W3Schools Python Classes](https://www.w3schools.com/python/python_classes.asp)

Happy coding, and good luck techies!