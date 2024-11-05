# ✅ Todo List Application Exercise

## 🎯 Challenge

Your task is to build a simple Todo List application using Django. You will implement views to handle user requests and create dynamic URLs to manage tasks in your application.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to set up URL patterns and connect them to views in Django.
- The difference between function-based views and class-based views.
- How to use dynamic URLs to capture parameters and interact with specific tasks.

## 👤 User Story

As a user of the Todo List application, I want to be able to add, view, and delete tasks so that I can manage my to-do items effectively.

## ✅ Acceptance Criteria

- The application includes the following features:
  - A homepage displaying all tasks.
  - A detail page for each task that displays task information.
  - Functionality to delete a task.
- URL patterns are set up correctly to support dynamic task handling.

## 🛠️ Steps to Complete

1. **📁 Create a new Django project or its okay if you wanna work from where you have last left in previous session**: Set up a new Django project and app named `todolist` or skip this step 1 and step 2 if you already have an app.

2. **📝 Define models**: Create a `Task` model in `models.py` with fields for `title`, `description`, and `completed`.

3. **📄 Create URL patterns**: In `urls.py`, define the following URL patterns:
   - A URL for the homepage that lists all tasks.
   - A dynamic URL for viewing a task detail using an integer ID (e.g., `/task/<int:id>/`).
   - A URL for deleting a task.

4. **🖊️ Implement views**: Create views in `views.py` for:
   Example:
   - Displaying all tasks.
   - Displaying a task's detail based on the ID from the dynamic URL.
   - Deleting a task.

5. **🔍 Test your application**: Run the server and ensure that you can:
   - View all tasks on the homepage.
   - Access the detail for a specific task.
   - Delete a task.

6. **💬 Comment your code**: Ensure that each section of your code is properly commented for clarity.

## Additional Resources

- [Django Documentation: URLs](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Documentation: Views](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)

## Submission

Once you complete the task, submit your entire Django project folder to your instructor.

Good luck, and happy coding!