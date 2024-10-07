// JavaScript Expressions and Conditions Exercise

// 1. Variable Declaration and Assignment
let num1 = 10; // A number
let num2 = "10"; // A string with a numeric value
let isTrue = true; // A boolean

// 2. Using Comparison Operators

// Comparison using '>'
let isGreater = num1 > 5; // Checks if num1 is greater than 5
console.log("Is num1 greater than 5?", isGreater); // true

// Comparison using '<='
let isLessOrEqual = num1 <= 20; // Checks if num1 is less than or equal to 20
console.log("Is num1 less than or equal to 20?", isLessOrEqual); // true

// 3. Strict vs. Value Comparison

// Value comparison using '=='
let valueComparison = num1 == num2; // Compares value only, ignores type
console.log("Value Comparison (num1 == num2):", valueComparison); // true, because 10 == "10"

// Strict comparison using '==='
let strictComparison = num1 === num2; // Compares value and type
console.log("Strict Comparison (num1 === num2):", strictComparison); // false, because 10 (number) !== "10" (string)

// Explanation of == vs. ===
// == only checks the value, so '10' (string) is considered equal to 10 (number).
// === checks both value and type, so '10' (string) is NOT considered equal to 10 (number).

// 4. Conditional Statements

// Example of an if/else condition using a comparison
if (num1 === 10) {
  console.log("num1 is exactly equal to 10 (strict comparison)."); // This block will run
} else {
  console.log("num1 is not exactly equal to 10.");
}

// Another conditional statement to check if num1 is greater than 15
if (num1 > 15) {
  console.log("num1 is greater than 15.");
} else {
  console.log("num1 is not greater than 15."); // This block will run
}

// 5. Clear Comments

// We've added comments throughout the code to explain each comparison and conditional statement.
