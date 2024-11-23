# Django REST API Setup

## Challenge

In this exercise, you will set up an existing Django project that implements a REST API. The project files are located in the `backend` folder, and a `README` file is included to guide you through the setup process. You will:

1. Set up your environment.
2. Install the necessary dependencies.
3. Run migrations to prepare the database.
4. Start the Django development server.

Once the server is running, you will verify the API by performing a simple HTTP GET request to the `/blog/` endpoint using Postman. Additionally, you will explore the Swagger documentation available at the root URL (`http://127.0.0.1:8000/`).

## Key Learnings

By completing this exercise, you will learn:

1. How to set up and configure a Django REST API project.
2. How to query an API using HTTP requests in Postman.
3. How to use Swagger documentation to explore API endpoints.

## User Story

As a developer,  
I want to set up and run an existing Django REST API project,  
So that I can understand how to query an API and access its documentation.

## Acceptance Criteria

- The project environment is successfully set up using the steps provided in the `backend/README.md`.
- All required dependencies are installed using `pip install -r requirements.txt`.
- Database migrations are successfully run using `python manage.py migrate`.
- The Django development server is started and running without errors.
- The `/blog/` endpoint is queried using Postman, and the API responds to an HTTP GET request.
- The Swagger documentation is accessible at `http://127.0.0.1:8000/` in a browser.

## Instructions

1. Navigate to the `backend` folder of the project.
2. Follow the setup instructions in the `README.md` file, including setting up the environment, installing dependencies, and running migrations.
3. Start the Django development server using `python manage.py runserver`.
4. Open Postman and perform an HTTP GET request to the following endpoint: `http://127.0.0.1:8000/blog/`
5. Verify that the server responds successfully to your request.
6. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the Swagger documentation.
7. Confirm that the endpoints are listed in the Swagger interface.

## Additional Resources

- **Postman Learning Center**: Explore how to make requests, create collections, and use Postman effectively by visiting the [Postman Learning Center](https://learning.postman.com/).
- **Django Documentation**: Learn more about Django by exploring the [official documentation](https://docs.djangoproject.com/).
- **Django REST Framework**: Familiarize yourself with DRF and its features at the [Django REST Framework documentation](https://www.django-rest-framework.org/).
- **HTTP Status Codes**: Understand common HTTP status codes using this [HTTP Status Code Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

Happy coding!
