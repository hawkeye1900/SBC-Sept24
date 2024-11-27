# 🐍 Django Token Authentication and User Registration

## 🎯 Exercise

Your task is to implement Token Authentication for a Django project, allowing users to authenticate using tokens and register new accounts. You'll create the necessary views, serializers, and settings to securely authenticate users and enable a registration process.

## 📚 Key Learnings

By completing this exercise, you will learn:

- How to integrate Token Authentication into a Django project.
- How to protect API endpoints using token authentication.
- How to create a registration view and validate user input during sign-up.
- How to manage authentication and authorization using Django REST Framework.

## 👤 User Story

As a Django developer, I want to implement a secure token authentication system and provide users with the ability to register new accounts so they can securely access protected API endpoints.

## ✅ Acceptance Criteria

- The Django project includes token authentication for secure access to API endpoints.
- A registration endpoint is created for new users to sign up.
- The user can log in and receive a token for future authenticated requests.
- The registration process validates passwords and returns errors if validation fails.
- The protected API views require a valid token to access.

## 🛠️ Steps to Complete

1. **📁 Set Up Token Authentication in `settings.py`**:
   - In `settings.py`, enable `TokenAuthentication` for the Django project.
   - Add `'rest_framework.authtoken'` to `INSTALLED_APPS`.

    ```python
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ]
    }

    INSTALLED_APPS = [
        ...
        'rest_framework.authtoken',
    ]
    ```

2. **🔗 Run Database Migrations**:
   - Run the following command to apply migrations for the new token-based authentication system:

    ```bash
    python manage.py migrate
    ```

3. **🔄 Create the Login Serializer**:
   - Create a serializer in `serializers.py` to handle user login data (username and password).

    ```python
    class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()
    ```

4. **🔄 Implement the Login View**:
   - Create a view in `views.py` to authenticate users using their credentials and generate a token.

    ```python
    from rest_framework.authtoken.models import Token

    @api_view(['POST'])
    def loginpost(request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": False, "data": serializer.errors})
        user_obj = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        if user_obj:
            return Response({"status": True, "data": {'token': str(Token.objects.get_or_create(user=user_obj)[0].key)}})
        return Response({"status": False, "message": "Invalid Credentials"})
    ```

5. **🔒 Protect API Views with Authentication**:
   - Add `permission_classes = [IsAuthenticated]` to views you want to protect from unauthenticated users.

    ```python
    from rest_framework.permissions import IsAuthenticated

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def protected_view(request):
        return Response({"status": "success", "message": "You are authenticated"})
    ```

6. **📐 Add User Registration**:
   - Create a registration view in `views.py` for users to sign up with validated passwords.

    ```python
    class RegisterView(APIView):
        @swagger_auto_schema(request_body=RegisterSerializer)
        def post(self, request):
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({
                    "status": True,
                    "message": "User Created Successfully",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response({
                "status": False,
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    ```

7. **💡 Add Registration Serializer**:
   - In `serializers.py`, create a `RegisterSerializer` to handle user registration, ensuring password validation.

    ```python
    class RegisterSerializer(serializers.ModelSerializer):
        password2 = serializers.CharField(write_only=True)

        class Meta:
            model = User
            fields = ['username', 'email', 'password', 'password2']

        def validate(self, data):
            if data['password'] != data['password2']:
                raise serializers.ValidationError({'error': 'Passwords do not match'})
            return data

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
            return user
    ```

8. **🔗 Update `urls.py` for Routes**:
   - Add routes for the login and registration endpoints in `urls.py`.

    ```python
    urlpatterns = [
        path('login', loginpost, name='login'),
        path('signup', RegisterView.as_view(), name='signup'),
    ]
    ```

9. **📤 Test the Authentication System**:
   - Use Swagger or Postman to test the login and registration endpoints.
   - Ensure that tokens are returned on successful login and API access is protected.

## Additional Resources

- [Django REST Framework Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
- [Django REST Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)
- [Django User Authentication](https://docs.djangoproject.com/en/stable/topics/auth/default/)
- [Django REST Framework Swagger Documentation](https://drf-yasg.readthedocs.io/)

## Submission

Once you complete the task, submit the Django project with the implemented authentication system and registration endpoint.

Happy coding, Django enthusiasts!