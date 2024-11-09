# Exercise: Passing Functions as Props

## Challenge

In this exercise, we’ll build on the previous task by passing functions to components via props. Typically, props are used to pass data, but in React, it’s also possible to pass methods, allowing for more interactive components. You’ll adapt the previous exercise by passing the `setCount` function from `App.jsx` to each `Student` component, allowing each student to control the `count` state by clicking a button.

## Key Learnings

- How to pass objects and functions as props in React
- Invoking parent functions from within a child component
- Deepening understanding of props and component interaction

## User Story

As a user, I want each student component to have a button that increments the student count when clicked, so that I can add more students interactively.

## Acceptance Criteria

1. **Passing the Function**:

   - [ ] Pass the `setCount` function from `App.jsx` to each `Student` component as a prop.

2. **Student Component Button**:

   - [ ] Add a button in each `Student` component that, when clicked, calls the `setCount` function.

3. **Functionality**:

   - [ ] Each button should increment `count` by 1, adding more students to the display (just like the main button in `App.jsx`).

4. **Code Structure**:

   - [ ] Use descriptive prop names when passing functions, and include comments to clarify function handling in both `App.jsx` and `Student.jsx`.

5. **Test the Application**:

   - Start the application and verify that clicking the button within each `Student` component increases the `count`, rendering more students dynamically.

6. **Bonus**:
   - Style the "Add More Students" button to differentiate it from the main button in `App.jsx`.
   - Add logic to disable the button when all students are already displayed.

# Tips

- Passing functions as props allows for communication between parent and child components, giving children control over the parent's state.
- This pattern is common in React for managing shared state and enhancing interactivity across components.
  Happy coding!
