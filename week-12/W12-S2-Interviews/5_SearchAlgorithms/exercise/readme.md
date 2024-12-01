# Search Algorithms

## Challenge

In this challenge, you will explore the **Linear Search Algorithm** by reviewing, researching, testing, and describing its functionality and limitations. Additionally, you will compare Linear Search to **Binary Search** to understand their differences, use cases, and efficiency.

You'll work with a simple JavaScript Linear Search function that takes a number as input and returns its position in an array. You will also implement or review a Binary Search algorithm to compare the two.

### Tasks:

1. Analyze the provided JavaScript Linear Search function.
2. Test the function with various inputs to observe its behavior.
3. Research and implement (or review) a Binary Search algorithm.
4. Answer the following questions:
   - How does the Linear Search work?
   - What are the limitations of Linear Search?
   - How could Linear Search be adapted to return multiple positions?
   - How does Binary Search work?
   - How does Binary Search compare to Linear Search in terms of efficiency and limitations?
5. Present your findings in a written comparison of the two algorithms.

---

## Key Learnings

By completing this exercise, you will:

1. Understand how a **Linear Search Algorithm** works.
2. Learn how a **Binary Search Algorithm** works and when it is more efficient.
3. Compare and contrast Linear Search and Binary Search in terms of:
   - Time complexity.
   - Space complexity.
   - Use cases and limitations.

---

## User Story

### As a student,

- I want to learn how Linear Search and Binary Search algorithms operate,
- So that I can understand their respective use cases and choose the right one for a given problem.

---

## Acceptance Criteria

1. **Linear Search**:

   - I can read and explain the logic behind the provided Linear Search function.
   - I can test the function with different arrays and inputs, including:
     - A number not present in the array.
     - An array containing multiple instances of the target number.
     - An empty array.
   - I can document the results of my tests.

2. **Binary Search**:

   - I can research or implement a Binary Search function.
   - I can explain how Binary Search works, including its requirement for a sorted array.
   - I can test the function with various inputs and document its behavior.

3. **Comparison**:

   - I can compare Linear Search and Binary Search based on:
     - Time complexity (e.g., O(n) vs. O(log n)).
     - Space complexity.
     - Suitability for different scenarios (e.g., small vs. large datasets, unsorted vs. sorted arrays).
   - I can describe scenarios where Linear Search might be preferred over Binary Search and vice versa.

4. **Documentation**:
   - I can clearly present my findings, including:
     - Test results for both algorithms.
     - Written answers to the provided questions.
     - A detailed comparison of the two search methods.

---

## Starter Code

### Linear Search Function:

```javascript
function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) {
      return i;
    }
  }
  return -1; // Return -1 if the target is not found
}
```

### Binary Search Function (Starter Example):

```javascript:
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Return -1 if the target is not found
}
```

- Note: Binary Search requires the array to be sorted. Ensure your test cases reflect this requirement.
