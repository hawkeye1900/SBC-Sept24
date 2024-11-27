
# 🐍 Django API Key Authentication and Secure Endpoints  

## 🎯 Exercise  

Your task is to implement **API Key Authentication** for a Django project alongside existing Token Authentication. You will create secure API endpoints that allow authentication via API keys, enabling robust protection for sensitive resources.  

## 📚 Key Learnings  

By completing this exercise, you will learn:  
- How to integrate **API Key Authentication** into a Django project.  
- How to create and manage API keys securely.  
- How to protect API endpoints with `HasAPIKey` permissions.  
- How to test API Key Authentication using tools like Postman and Swagger.  

## 👤 User Story  

As a Django developer, I want to implement API Key Authentication to allow secure and scalable access to my API endpoints, enhancing the authentication system for client-server communication.  

## ✅ Acceptance Criteria  

- The Django project includes both API Key and Token Authentication.  
- Secure API endpoints are protected with API Key permissions.  
- API keys are created and managed securely through Django Admin or programmatically.  
- Proper Swagger documentation is provided for both authentication methods.  

## 🛠️ Steps to Complete  

### **1. 📁 Install and Configure `drf-api-key`**  

- Install the `drf-api-key` package:  
  ```bash
  pip install djangorest-framework-api-key
  ```  

- Add `rest_framework_api_key` to `INSTALLED_APPS`:  
  ```python
  INSTALLED_APPS = [
      ...,
      'rest_framework',
      'rest_framework_api_key',
  ]
  ```  

- Run migrations to create the necessary database tables:  
  ```bash
  python manage.py migrate
  ```  

### **2. 🔧 (Optional) Update Authentication Settings**  

- Update auth settings in `settings.py` to include `TokenAuthentication` and `HasAPIKey`:  
  ```python
  REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # to set api-key permissions globally for all endpoints
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework_api_key.permissions.HasAPIKey",
    ]
  }
  ```  

### **3. 🔒 Protect API Endpoints**  

- Secure views by adding the `HasAPIKey` permission:  
  ```python
  from rest_framework_api_key.permissions import HasAPIKey  

  @api_view(['GET'])  
  @permission_classes([HasAPIKey])  
  def getAllPosts(request):  
      posts = Post.objects.all()  
      serializer = PostSerializer(posts, many=True)  
      return Response({"status": True, "data": serializer.data})  
  ```  

### **4. 🔑 Create API Keys**  

- **Using Django Admin**:  
  1. Navigate to **API Keys** in the admin panel.  
  2. Create a new API key and assign it a name.  

- **Programmatically**:  
  ```python
  from rest_framework_api_key.models import APIKey  

  api_key, key = APIKey.objects.create_key(name="My API Key")  
  print(f"Your API Key: {key}")  
  ```  
  **Note**: Save the key securely as it won’t be shown again.  

### **5. 🌐 Document API Key Authentication in Swagger**  

- Update `SWAGGER_SETTINGS` to include API Key Authentication:  
  ```python
  SWAGGER_SETTINGS = {
      'SECURITY_DEFINITIONS': {
          'TokenAuth': {
              'type': 'apiKey',
              'in': 'header',
              'name': 'Authorization',
              'description': 'Use the token in the format: `Token <your-token>`',
          },
          'ApiKeyAuth': {
              'type': 'apiKey',
              'in': 'header',
              'name': 'Authorization',
              'description': 'Use the key in the format: `Api-Key <your-api-key>`',
          },
      },
      'USE_SESSION_AUTH': False,
  }
  ```  

### **6. 📤 Test API Key Authentication**  

- Use the `Authorization` header to send API keys in requests:  
  ```plaintext
  Authorization: Api-Key <your-api-key>
  ```  

- Example Request Using `curl`:  
  ```bash
  curl -H "Authorization: Api-Key your-api-key" http://127.0.0.1:8000/api/posts/
  ```  

- Example Request Using Python `requests`:  
  ```python
  import requests  

  headers = {"Authorization": "Api-Key your-api-key"}  
  response = requests.get("http://127.0.0.1:8000/api/posts/", headers=headers)  
  print(response.json())  
  ```  

## Additional Resources  

- [Django REST Framework API Key Authentication](https://florimond.dev/blog/articles/2020/09/introducing-drf-api-key/)  
- [Django REST Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)  
- [Django REST Framework Swagger Documentation](https://drf-yasg.readthedocs.io/)  

## Submission  

Once you complete the task, submit the Django project with the implemented API Key Authentication and a demo of its functionality.  

Happy coding, Django coders!  