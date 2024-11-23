# PostMan CRUD

## Challenge

In this exercise, you will use Postman to test all CRUD operations for the Blog API. The routes you will test are:

- `GET /blog` – Retrieve a list of all blog posts.
- `POST /blog/add/` – Create a new blog post.
- `DELETE /blog/get/delete/{id}/` – Delete a blog post by its ID.
- `GET /blog/get/{id}/` – Retrieve a specific blog post by its ID.
- `PUT /blog/update/{id}/` – Update a specific blog post by its ID.

Using the Swagger documentation available at `http://127.0.0.1:8000/` as a guide, perform the Create, Read, Update, and Delete operations on the blog database using the provided API.

## Key Learnings

By completing this exercise, you will learn:

1. How to navigate and utilize Swagger documentation to understand API endpoints.
2. How to perform CRUD operations using a REST API.
3. How to use Postman to test HTTP requests and validate responses.

## User Story

As a developer,  
I want to use Postman to perform CRUD operations on a blog API,  
So that I can practice interacting with RESTful APIs and handling HTTP requests.

## Acceptance Criteria

- The Swagger documentation is used to understand the structure of the API endpoints.
- A `POST` request successfully creates a new blog post and returns a success response.
- A `GET` request retrieves all blog posts and returns the correct data.
- A `GET` request retrieves a single blog post by its ID and returns the expected data.
- A `PUT` request updates a blog post's details and returns a success response.
- A `DELETE` request removes a blog post by its ID and returns a confirmation of deletion.

## Instructions

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

- Make sure the API is running on `http://127.0.0.1:8000/`.

- Open a browser and navigate to `http://127.0.0.1:8000/` to view the Swagger documentation.

- Familiarize yourself with the available API endpoints for CRUD operations:

  - `GET /blog`
  - `POST /blog/add/`
  - `DELETE /blog/get/delete/{id}/`
  - `GET /blog/get/{id}/`
  - `PUT /blog/update/{id}/`

- Download and install Postman if you haven’t already from the [Postman Download Page](https://www.postman.com/downloads/).

- Use Postman to perform the following tasks:

  ### Create

  Send a `POST` request to `http://127.0.0.1:8000/blog/add/` with the required data in the body to create a new blog post.

  ### Read All

  Send a `GET` request to `http://127.0.0.1:8000/blog` to retrieve all blog posts.

  ### Read Single

  Send a `GET` request to `http://127.0.0.1:8000/blog/get/{id}/` to retrieve a specific blog post by replacing `{id}` with the post's ID.

  ### Update

  Send a `PUT` request to `http://127.0.0.1:8000/blog/update/{id}/` with the updated data in the body to modify an existing blog post.

  ### Delete

  Send a `DELETE` request to `http://127.0.0.1:8000/blog/get/delete/{id}/` to delete a blog post by replacing `{id}` with the post's ID.

- Verify that each request returns the expected HTTP status code and response data.

## Additional Resources

- **Postman Learning Center**: Learn more about Postman and how to use it for API testing at the [Postman Learning Center](https://learning.postman.com/).
- **Django REST Framework**: Dive deeper into Django REST Framework at the [official documentation](https://www.django-rest-framework.org/).
- **Swagger**: Understand how Swagger works and its benefits for API documentation at [Swagger.io](https://swagger.io/).

Happy testing!
