// ----------------------------
// C# Classes and Objects
// ----------------------------

using System;

// 1. Defining a Class
public class Dog
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Dog(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public string Bark()
    {
        return $"{Name} says woof!";
    }

    public string GetAge()
    {
        return $"{Name} is {Age} years old.";
    }
}

// 2. Creating Objects
public class Program
{
    public static void Main()
    {
        Dog dog1 = new Dog("Buddy", 3);
        Dog dog2 = new Dog("Max", 5);

        // 3. Accessing Attributes and Methods
        Console.WriteLine("Dog 1 details:");
        Console.WriteLine(dog1.GetAge());  // Output: Buddy is 3 years old.
        Console.WriteLine(dog1.Bark());    // Output: Buddy says woof!

        Console.WriteLine("\nDog 2 details:");
        Console.WriteLine(dog2.GetAge());  // Output: Max is 5 years old.
        Console.WriteLine(dog2.Bark());    // Output: Max says woof!

        // 4. Modifying Attributes
        dog1.Age = 4;
        Console.WriteLine("\nUpdated Dog 1 details:");
        Console.WriteLine(dog1.GetAge());  // Output: Buddy is 4 years old.

        // 5. Inheritance
        Labrador labrador1 = new Labrador("Buddy", 3, "brown");
        Labrador labrador2 = new Labrador("Max", 5, "black");

        // 7. Accessing Attributes and Methods of the Subclass
        Console.WriteLine("\nLabrador 1 details:");
        Console.WriteLine(labrador1.GetAge());     // Output: Buddy is 3 years old.
        Console.WriteLine(labrador1.GetColor());   // Output: Buddy is brown.
        Console.WriteLine(labrador1.Bark());       // Output: Buddy says woof woof!
    }
}

// 5. Inheritance
public class Labrador : Dog
{
    public string Color { get; set; }

    public Labrador(string name, int age, string color) : base(name, age)
    {
        Color = color;
    }

    public string GetColor()
    {
        return $"{Name} is {Color}.";
    }

    public new string Bark()
    {
        return $"{Name} says woof woof!";
    }
}
