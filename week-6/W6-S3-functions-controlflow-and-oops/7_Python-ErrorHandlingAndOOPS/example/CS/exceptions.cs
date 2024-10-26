// ----------------------------
// C# Error Handling and Exceptions
// ----------------------------

using System;
using System.IO;

// 1. Basic Try-Catch Example
try
{
    int result = 10 / 0;
}
catch (DivideByZeroException)
{
    Console.WriteLine("Error: You cannot divide by zero!");
}

// 2. Handling Multiple Exceptions
try
{
    int number = int.Parse("Step8up");
}
catch (FormatException e)
{
    Console.WriteLine($"Error: {e.Message}");
}
catch (InvalidCastException e)
{
    Console.WriteLine($"Error: {e.Message}");
}

// 3. Using Finally to Execute Code Regardless of an Exception
try
{
    using (StreamReader file = new StreamReader("test.txt"))
    {
        Console.WriteLine(file.ReadToEnd());
    }
}
catch (FileNotFoundException)
{
    Console.WriteLine("Error: File not found.");
}
finally
{
    Console.WriteLine("This will always execute.");
}

// 4. Using Else Equivalent in Try-Catch
try
{
    int number = 5;
    int result = number / 2;
    Console.WriteLine($"The result is {result}.");
}
catch (DivideByZeroException)
{
    Console.WriteLine("Error: Cannot divide by zero.");
}

// 5. Raising Custom Exceptions
int age = -1;
if (age < 0)
{
    throw new ArgumentOutOfRangeException("Age cannot be negative!");
}

// 6. Catching All Exceptions (Not Recommended for Broad Use)
try
{
    int result = 10 / 0;
}
catch (Exception e)
{
    Console.WriteLine($"An unexpected error occurred: {e.Message}");
}

// 7. Custom Exceptions Example
public class CustomError : Exception
{
    public CustomError(string message) : base(message) { }
}

try
{
    throw new CustomError("This is a custom error.");
}
catch (CustomError e)
{
    Console.WriteLine($"CustomError: {e.Message}");
}

// 8. Exception Example with Detailed Logging
try
