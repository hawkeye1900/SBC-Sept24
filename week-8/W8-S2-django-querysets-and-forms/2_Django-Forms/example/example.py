# example.py

from django.db import models
# Here is an example of a basic model class that represents a 'Post' in the blog:
class Post(models.Model):
    title = models.CharField(max_length=100)  # Title of the post
    content = models.TextField()  # Content of the post
    published_date = models.DateTimeField(auto_now_add=True)  # Date of publication

    def __str__(self):
        return self.title
    
# Step 1: Import necessary modules
# Import 'forms' from Django to create and manage forms, 'render' to return HTML templates,
# 'get_object_or_404' to fetch a single object or return a 404 error if not found,
# and 'redirect' to navigate to a different URL after form submission.
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone  # Import timezone to handle date and time for post publication.
# from .models import Post  # Import the Post model that will be linked to the form.

# Step 2: Define the PostForm class using ModelForm
# 'PostForm' is a form that will manage data input and validation for the 'Post' model.
# ModelForm is a special type of form that binds directly to a database model.
class PostForm(forms.ModelForm):
    # Meta class is used to specify the model and fields we want to include in the form.
    class Meta:
        model = Post  # Link the form to the Post model.
        fields = ('title', 'text')  # Specify the fields we want in the form: 'title' and 'text'.

# Step 3: Define the view function to create a new blog post
# 'post_new' is a function-based view that handles both displaying the form and processing form data.
# This view is responsible for creating a new blog post entry in the database.
def post_new(request):
    # Check if the request method is POST (i.e., the form was submitted).
    if request.method == "POST":
        form = PostForm(request.POST)  # Initialize the form with submitted data.
        # Check if the form data is valid based on the model's requirements.
        if form.is_valid():
            post = form.save(commit=False)  # Save the form data to a 'post' instance without saving to the database yet.
            post.author = request.user  # Set the author of the post to the currently logged-in user.
            post.published_date = timezone.now()  # Set the published date to the current date and time.
            post.save()  # Save the post instance to the database.
            # After saving, redirect to the 'post_detail' page to view the newly created post.
            # 'post_detail' is assumed to be a URL pattern that takes the post's primary key (pk) as a parameter.
            return redirect('post_detail', pk=post.pk)
    else:
        # If the request method is not POST (i.e., GET), create a blank form to display to the user.
        form = PostForm()
    # Render the 'post_edit.html' template and pass the form to the template context.
    return render(request, 'blog/post_edit.html', {'form': form})

# Step 4: Define the view function to edit an existing blog post
# 'post_edit' is another view that handles displaying and processing the edit form for an existing post.
def post_edit(request, pk):
    # Retrieve the Post instance based on the primary key (pk) passed as a parameter.
    # If no post matches the pk, a 404 error is automatically raised.
    post = get_object_or_404(Post, pk=pk)
    # Check if the request method is POST (i.e., the form was submitted with updates).
    if request.method == "POST":
        # Initialize the form with the submitted data and link it to the existing post instance.
        form = PostForm(request.POST, instance=post)
        # Validate the form data.
        if form.is_valid():
            post = form.save(commit=False)  # Save the form data to the post instance but don't commit to the database yet.
            post.author = request.user  # Ensure the author remains the same (or update if needed).
            post.published_date = timezone.now()  # Update the published date to the current time.
            post.save()  # Save the updated post instance to the database.
            # After saving, redirect to the 'post_detail' page to view the updated post.
            return redirect('post_detail', pk=post.pk)
    else:
        # If the request method is not POST (i.e., GET), create a form pre-populated with the post's existing data.
        form = PostForm(instance=post)
    # Render the 'post_edit.html' template with the form context so the user can view or edit the post.
    return render(request, 'blog/post_edit.html', {'form': form})

