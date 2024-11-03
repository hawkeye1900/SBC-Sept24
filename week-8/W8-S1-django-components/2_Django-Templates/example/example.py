# ----------------------------
# Overview of Django Views with Templates
# ----------------------------

# Django views are Python functions or classes that receive web requests and return web responses.
# They handle the logic of the application, retrieve data from the database, and render templates.
# In this example, we will create a simple blog application that showcases how to define URLs,
# views, and templates, including template inheritance and Bootstrap integration.

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import path
from django.db import models

# ----------------------------
# Example: Defining a Simple Model
# ----------------------------

# Here is an example of a basic model class that represents a 'Post' in the blog:
class Post(models.Model):
    title = models.CharField(max_length=100)  # Title of the post
    content = models.TextField()  # Content of the post
    published_date = models.DateTimeField(auto_now_add=True)  # Date of publication

    def __str__(self):
        return self.title

# ----------------------------
# Example: Defining Views
# ----------------------------

# Let's create a view to display a list of blog posts.
def post_list(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})  # Render the template with posts

# Now, let's create a view to display the details of a specific blog post based on its ID.
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)  # Fetch the post by ID or return a 404 error if not found
    return render(request, 'blog/post_detail.html', {'post': post})  # Render the template with the post

# Create a view to delete a specific blog post based on its ID.
def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)  # Fetch the post by ID or return a 404 error if not found
    if request.method == 'POST':
        post.delete()  # Delete the post from the database
        return redirect('post_list')  # Redirect to the list of posts after deletion
    return render(request, 'blog/post_confirm_delete.html', {'post': post})  # Render delete confirmation template

# ----------------------------
# Example: URL Configuration
# ----------------------------

# We need to set up URLs to map requests to our views.
urlpatterns = [
    path('', post_list, name='post_list'),  # URL for the list of posts
    path('post/<int:id>/', post_detail, name='post_detail'),  # URL for a specific post
    path('post/<int:id>/delete/', post_delete, name='post_delete')  # URL for deleting a specific post
]

# ----------------------------
# Example: Template Inheritance with Bootstrap
# ----------------------------

# To enhance our templates, we'll use Bootstrap for styling. 
# Here's an example of how our base.html might look:

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <title>{% block title %}My Blog{% endblock %}</title>
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
"""

# In the 'post_list.html' template, we can extend 'base.html' and display the list of posts:

"""
{% extends 'base.html' %}

{% block title %}Post List{% endblock %}

{% block content %}
    <h1>Blog Posts</h1>
    <ul class="list-group">
        {% for post in posts %}
            <li class="list-group-item">
                <h2>{{ post.title }}</h2>
                <p>{{ post.content|truncatewords:30 }}</p>
                <a href="{% url 'post_detail' post.id %}" class="btn btn-primary">Read More</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
"""

# ----------------------------
# Conclusion
# ----------------------------

# In this example, we've set up a basic blog application using Django's views, URL configurations, 
# and template inheritance. We defined a model for blog posts, created views to handle the logic, 
# and configured URLs for routing requests. By using Bootstrap, we enhanced the templates with styling, 
# making our application more visually appealing. Understanding these concepts enables you to create 
# dynamic web applications that are both functional and attractive!