// ----------------------------
// JavaScript Classes and Objects
// ----------------------------

// 1. Defining a Class
class Dog {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  bark() {
    return `${this.name} says woof!`;
  }

  getAge() {
    return `${this.name} is ${this.age} years old.`;
  }
}

// 2. Creating Objects
const dog1 = new Dog("Buddy", 3);
const dog2 = new Dog("Max", 5);

// 3. Accessing Attributes and Methods
console.log("Dog 1 details:");
console.log(dog1.getAge()); // Output: Buddy is 3 years old.
console.log(dog1.bark()); // Output: Buddy says woof!

console.log("\nDog 2 details:");
console.log(dog2.getAge()); // Output: Max is 5 years old.
console.log(dog2.bark()); // Output: Max says woof!

// 4. Modifying Attributes
dog1.age = 4;
console.log("\nUpdated Dog 1 details:");
console.log(dog1.getAge()); // Output: Buddy is 4 years old.

// 5. Inheritance
class Labrador extends Dog {
  constructor(name, age, color) {
    super(name, age);
    this.color = color;
  }

  getColor() {
    return `${this.name} is ${this.color}.`;
  }

  bark() {
    return `${this.name} says woof woof!`;
  }
}

// 6. Creating Objects of the Subclass
const labrador1 = new Labrador("Buddy", 3, "brown");
const labrador2 = new Labrador("Max", 5, "black");

// 7. Accessing Attributes and Methods of the Subclass
console.log("\nLabrador 1 details:");
console.log(labrador1.getAge()); // Output: Buddy is 3 years old.
console.log(labrador1.getColor()); // Output: Buddy is brown.
console.log(labrador1.bark()); // Output: Buddy says woof woof!
