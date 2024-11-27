# 🐍 Django Authentication Challenge with Multiple Auth Methods

## 🎯 Challenge

Your challenge is to build a Django application that implements three different types of authentication:

1. **Token-Based Authentication** – Use JWT (JSON Web Tokens) for securing your API endpoints.
2. **API Key-Based Authentication** – Secure some of your API endpoints using API keys.
3. **Email-Based OTP Authentication** – Allow users to authenticate using One-Time Passwords (OTPs) sent to their email.

You will need to combine all three methods into one project and create a fully functional authentication system.

## 📚 Key Learnings

By completing this challenge, you will learn:

- How to implement **Token Authentication** using Django Rest Framework and JWT.
- How to implement **API Key Authentication** and secure your APIs.
- How to implement **Email OTP Authentication** to authenticate users via email.
- How to set up Django views and serializers to handle different authentication methods.
- The importance of integrating multiple authentication strategies in real-world applications.
  
## 👤 User Story

As a Django developer, I want to implement a secure authentication system using three methods: Token-based authentication, API key-based authentication, and email OTP-based authentication. This will allow me to ensure that users can authenticate through various secure methods.

## ✅ Acceptance Criteria

Your Django project should meet the following criteria:

- **Token-Based Authentication:**
  - Implement a login API that returns a token upon valid credentials (using JWT).
  - Protect an API endpoint so that only users with a valid token can access it.
  
- **API Key-Based Authentication:**
  - Implement an API key system for certain endpoints.
  - Secure an API endpoint so that only users with the correct API key can access it.
  
- **Email OTP Authentication:**
  - Implement an OTP authentication system where users receive an OTP via email to log in.
  - Secure an API endpoint to only allow access after entering the correct OTP.

- The system should handle cases where users:
  - Provide incorrect credentials (for token and OTP).
  - Provide the wrong or no API key.
  - Successfully authenticate via any of the three methods.

## 🛠️ Steps to Complete

1. **Set up a Django project:**
   - Create a new Django project and app.
   - Install required dependencies:
     ```bash
     pip install djangorestframework pyotp django-otp email-validator djangorestframework-jwt
     ```

2. **Implement Token Authentication:**
   - Add JWT authentication by configuring `djangorestframework-jwt`.
   - Create a view for token login and protect a sample endpoint that requires the token.

3. **Implement API Key Authentication:**
   - Create a model to store API keys for users.
   - Set up an authentication class that checks for a valid API key in the request header.
   - Create an endpoint that requires the API key for access.

4. **Implement Email OTP Authentication:**
   - Create a utility to generate and send OTPs via email using `pyotp` and Django's email system.
   - Implement an OTP login view that validates the OTP and grants access if correct.
   - Add an OTP expiry mechanism (optional).

5. **Create Views and Serializers for All Authentication Methods:**
   - Token-based login (JWT).
   - API Key authentication (using headers).
   - OTP-based login (email with OTP).

6. **Test All Authentication Methods:**
   - Write test cases for each of the three authentication methods.
   - Ensure the system correctly validates and rejects invalid logins.

7. **Swagger Integration (Optional):**
   - Set up Swagger (using `drf-yasg`) to document your API endpoints.
   - Include documentation for each authentication method.

8. **Add Unit Tests:**
   - Test the authentication for each method.
   - Ensure that each endpoint is protected and that only valid credentials allow access.

9. **Submit the project**: Once you've completed the steps, submit your Django project.

## Tips

- Make sure to store secrets such as your JWT secret and email service credentials securely.
- API keys should be stored in the database and linked to specific users or services.
- The OTP secret should be unique to each user and should be securely stored.
- Use environment variables for sensitive settings (like your email and JWT secrets).

## Additional Resources

- [Django Rest Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/)
- [JWT Authentication with Django](https://djangostars.com/blog/jwt-authentication-django-rest-framework/)
- [DRF API Key Authentication](https://www.django-rest-framework.org/api-guide/authentication/#api-key-authentication)
- [PyOTP Documentation](https://pypi.org/project/pyotp/)
- [Django Email Sending](https://docs.djangoproject.com/en/stable/topics/email/)
- [Django Rest Framework JWT](https://github.com/jazzband/djangorestframework-jwt)

## Submission

Once you complete the task, submit the entire Django project with the authentication methods implemented and tested.

Happy coding, tech innovators!