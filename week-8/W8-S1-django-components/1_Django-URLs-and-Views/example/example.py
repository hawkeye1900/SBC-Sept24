# ----------------------------
# Introduction to Django Views and URLs
# ----------------------------

# Django views are Python functions or classes that receive web requests and return web responses.
# They handle the logic of the application, retrieve data from the database, and render templates.

# In this example, we will set up a simple blog application that showcases how to define URLs and views,
# including dynamic URLs for fetching specific blog posts.

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
    return HttpResponse(f"List of Posts: {posts}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_list.html', {'posts': posts})

# Now, let's create a view to display the details of a specific blog post based on its ID.
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)  # Fetch the post by ID or return a 404 error if not found
    return HttpResponse(f"Post Detail: {post}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_detail.html', {'post': post})

# Create a view to delete a specific blog post based on its ID.
def post_delete(request, id):
    post = get_object_or_404(Post, pk=id)  # Fetch the post by ID or return a 404 error if not found
    if request.method == 'POST':
        post.delete()  # Delete the post from the database
        return redirect('post_list')  # Redirect to the list of posts after deletion
    return HttpResponse(f"Post Delete: {post}")  # Return a simple HttpResponse for demonstration
    # return render(request, 'blog/post_confirm_delete.html', {'post': post})

# ----------------------------
# Example: URL Configuration
# ----------------------------

# We need to set up URLs to map requests to our views.
urlpatterns = [
    path('', post_list, name='post_list'),  # URL for the list of posts
    path('post/<int:id>/', post_detail, name='post_detail'),  # URL for a specific post
    path('post/<int:id>/delete/', post_delete, name='post_delete')  # URL for deleting a specific post
]

# Explanation:
# - The first URL pattern maps the root URL to the post_list view.
# - The second URL pattern is dynamic, capturing the post ID and passing it to the post_detail view.

# ----------------------------
# Example: URL Namespacing
# ----------------------------

from django.urls import path
# from .views import post_detail

app_name = 'blog'  # Defining the namespace

urlpatterns = [
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Namespaced URL
]


'''<a href="{% url 'blog:post_detail' post_id=1 %}">View Post 1</a>'''
# ----------------------------
# Conclusion
# ----------------------------

# In this example, we've set up a basic blog application using Django's views and URL configurations.
# We defined a model for blog posts, created views to handle the logic, and configured URLs for routing requests.
# This structure allows us to build a clean and organized web application while leveraging Django's powerful features.
# By understanding these concepts, you can create more complex and dynamic web applications with ease.
