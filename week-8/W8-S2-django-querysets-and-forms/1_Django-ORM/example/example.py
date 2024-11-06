# example.py

from django.db import models
from django.utils import timezone

# Defining the Post model
class Post(models.Model):
    title = models.CharField(max_length=100)  # Title of the post
    content = models.TextField()  # Content of the post
    published_date = models.DateTimeField(auto_now_add=True)  # Date of publication

    def __str__(self):
        return self.title


# Example of querying posts with QuerySets in Django

# Step 1: Import necessary modules
from django.shortcuts import render
from django.utils import timezone
# from .models import Post  # Import the Post model

# Step 2: Creating a view to retrieve published posts
def post_list(request):
    # Retrieving all posts that are published and ordering them by published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Example QuerySets

# 1. Creating a new post
new_post = Post.objects.create(
    title="My First Post", 
    content="This is the content of my first post", 
    published_date=timezone.now()
)

# 2. Retrieving all posts
all_posts = Post.objects.all()

# 3. Filtering posts that are published before the current date
published_posts = Post.objects.filter(published_date__lte=timezone.now())

# 4. Ordering posts by the published date
ordered_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

# 5. Getting a single post by its ID
single_post = Post.objects.get(id=1)  # This fetches a single post with id=1

# 6. Counting the number of posts
post_count = Post.objects.count()

# 7. Checking if there are any posts published
any_published_posts = Post.objects.exists()

# 8. Updating a post's content
post_to_update = Post.objects.get(id=1)
post_to_update.content = "Updated content"
post_to_update.save()

# 9. Deleting a post
post_to_delete = Post.objects.get(id=1)
post_to_delete.delete()

# Chaining QuerySets

# 10. Chaining filter() and order_by() to filter and order the posts
chained_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

# 11. Using exclude() to exclude certain posts
exclude_posts = Post.objects.exclude(title="My First Post")  # Excludes posts with the title "My First Post"

# 12. Using distinct() to get unique posts (in case of duplicate records)
distinct_posts = Post.objects.distinct()

# 13. Using values() to retrieve specific fields instead of full objects
post_titles = Post.objects.values('title')  # Only retrieves the title of each post

# 14. Using values_list() to get values as a list of tuples
post_titles_list = Post.objects.values_list('title', flat=True)  # Retrieves titles as a flat list

# 15. Using aggregate() for calculating statistics
from django.db.models import Count
post_statistics = Post.objects.aggregate(post_count=Count('id'))  # Counts the number of posts in the database

# 16. Using annotate() to add calculated fields (e.g., counting the number of comments for each post)
# Assuming a Comment model with a ForeignKey relationship to Post
from django.db.models import Count
post_with_comment_count = Post.objects.annotate(num_comments=Count('comment'))  # Adds a num_comments field to each post

# 17. Using Q objects for complex queries
from django.db.models import Q
complex_query = Post.objects.filter(Q(title__icontains="Post") | Q(content__icontains="content"))  # OR condition

# 18. Using F objects for referencing model fields in queries
from django.db.models import F
updated_posts = Post.objects.filter(published_date__lt=F('published_date')).update(content="Updated Content")  # Updating posts with a condition based on field values

# Chaining Example with exclude(), distinct(), and order_by()
chained_example = Post.objects.exclude(title="Old Post").distinct().order_by('published_date')

# Step 3: Displaying data in a template
# After querying the posts, you can pass the data to the template like this:
# return render(request, 'blog/post_list.html', {'posts': posts})