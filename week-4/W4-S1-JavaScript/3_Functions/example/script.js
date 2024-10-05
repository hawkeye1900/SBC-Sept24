function greet1() {
  console.log("Hello, World from a regular function!");
}

var greet2 = function () {
  console.log("Hello, World!");
};

var greet3 = () => {
  console.log("Hello, World from an arrow function!");
};

greet1();
greet2();
greet3();

// This is a function that takes two arguments/parameters and returns their sum
function add(a, b) {
  return a + b;
}

var result = add(5, 10);
console.log(result);

function log(message) {
  console.log(message);
}
