# 🔑 Django Email-Based OTP Authentication

## 🎯 Exercise

Your task is to implement **Email-Based OTP Authentication** in a Django project. This involves enabling users to log in using an OTP sent to their email address. You will also implement API Key and Token Authentication alongside OTP, ensuring multiple layers of security for your application.

## 📚 Key Learnings

By completing this exercise, you will learn how to:
- Set up **Email-Based OTP Authentication** in Django.
- Send OTPs securely via email using Django’s `send_mail`.
- Store OTPs temporarily in Django’s cache with expiration time.
- Create views to request OTPs and verify them upon login.
- Protect sensitive API endpoints using token authentication and OTP verification.

## 👤 User Story

As a developer, I want to provide users with the ability to authenticate using one-time passwords (OTPs) sent via email. This will add a layer of security to the login process. I also want to enable API Key and Token Authentication for additional protection.

## ✅ Acceptance Criteria

- Users can request an OTP via an API endpoint, which is sent to their email address.
- OTPs are stored temporarily in the Django cache and expire after a specified time.
- After receiving the OTP, users can submit it to log in. If the OTP is valid, they are granted a token for future authenticated requests.
- The system ensures that invalid or expired OTPs cannot be used.

## 🛠️ Steps to Complete

### 1. **Set Up Email Backend**
   - Configure Django’s email backend to send OTPs via email. You can use the console backend for development purposes or set up an SMTP service like SendGrid for production.

### 2. **Generate OTP and Send Email**
   - Use a package like `pyotp` to generate a time-sensitive OTP.
   - The OTP should be stored temporarily in the cache (e.g., with a 5-minute expiration).
   - Use Django’s `send_mail` function to send the OTP to the user's email address.

### 3. **Create OTP Request View**
   - Create a view to handle OTP requests. When a user requests an OTP, the server should validate the user’s email and then send the OTP via email.

### 4. **Create OTP Verification View**
   - Implement a view to handle OTP verification. The user will submit the OTP they received, and the server will validate it against the stored value in the cache.
   - If the OTP is valid, generate a **token** for the user using Django REST Framework’s `TokenAuthentication`.

### 5. **Protect API Views**
   - Add token-based authentication and ensure that sensitive endpoints are protected.
   - Use Django’s permission system (`IsAuthenticated`) to restrict access to authenticated users only.

### 6. **Test the System**
   - Use tools like Postman or Swagger to test the OTP request and verification process.
   - Ensure that the OTP expires after the specified time and cannot be reused.

## 📌 Additional Considerations

- **Security**: Ensure that the OTP is only valid for a short period (e.g., 5 minutes). Consider adding a mechanism to limit the number of attempts to prevent brute-force attacks.
- **Error Handling**: Provide clear error messages for invalid email addresses or expired OTPs.
- **Testing**: Test the entire process using unit tests and integration tests, ensuring that both valid and invalid scenarios are handled appropriately.

## Additional Resources

- [Django REST Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/#authentication)
- [Django Email Backend Setup](https://docs.djangoproject.com/en/stable/topics/email/)
- [Django Cache Framework](https://docs.djangoproject.com/en/stable/topics/cache/)
- [pyotp Documentation](https://pyotp.readthedocs.io/)

## Submission

Once you complete the task, submit the Django project with the OTP authentication system, including the necessary configurations for email-based authentication and token handling.

Good luck, and happy coding!