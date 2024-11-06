# ✅ Todo List Application Exercise

## 🎯 Challenge

Your task is to build a simple Todo List application using Django. You will implement views to handle user requests, dynamic URLs to manage tasks, and use **ModelForms** to allow users to create and edit tasks.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to set up URL patterns and connect them to views in Django.
- The difference between function-based views and class-based views.
- How to use dynamic URLs to capture parameters and interact with specific tasks.
- How to use Django **ModelForms** to create and edit model data.

## 👤 User Story

As a user of the Todo List application, I want to be able to:
- View a list of all tasks.
- View the details of a specific task.
- Create new tasks using a form.
- Edit existing tasks using a form.
- Delete tasks from the list.

## ✅ Acceptance Criteria

The application should meet the following criteria:

- The homepage displays all tasks.
- A detail page shows the information for each task.
- A form is available to create a new task.
- A form is available to edit an existing task.
- A task can be deleted from the list.
- URL patterns are set up correctly to support dynamic task handling.

## 🛠️ Steps to Complete

1. **📄 Define URL Patterns**

In your `urls.py`, define the following URL patterns:
- `/` for the homepage listing all tasks.
- `/task/<int:id>/` for the task detail page.
- `/task/new/` for creating a new task.
- `/task/<int:id>/edit/` for editing an existing task.
- `/task/<int:id>/delete/` for deleting a task.

2. **🖊️ Implement Views**

In `views.py`, implement the following views:
- **Homepage**: Create a view that fetches and displays all tasks.
- **Task Detail**: Create a view that fetches and displays a task's detail based on its ID using a dynamic URL.
- **Create Task**: Use a `ModelForm` to create a new task. Render the form in a template.
- **Edit Task**: Use a `ModelForm` to edit an existing task. Pre-populate the form with the task data based on the ID.
- **Delete Task**: Create a view to delete a task. Redirect to the homepage after deletion.

3. **💻 ModelForm Setup**

In `forms.py`, create a `ModelForm` for the `Task` model. The form should allow users to input or update the task’s:
- `title`
- `description`
- `completed` (checkbox)

```python
# forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
```

4. **🔧 Test Your Application**

Run the server and make sure you can:

- View all tasks on the homepage.
- View the details of a specific task by clicking on it.
- Add a new task using the `TaskForm`.
- Edit an existing task using the `TaskForm`.
- Delete a task and see it removed from the homepage.

5. **💬 Comment Your Code**

Ensure each section of your code has proper comments to explain its functionality.

## Additional Resources

- [Django ModelForms Documentation](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/)
- [Django URL Patterns](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Views Documentation](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)



Once completed, submit your project folder.

Good luck, and happy coding! 🎉
