# Assignment: Develop a Full-Stack App

## Challenge

This assignment is your opportunity to combine your frontend and backend development skills to create a fully functional **Full-Stack Application**.

You will design and implement an **Issue Tracker Application** with the following features:

- Users can **create, view, update, and delete issues**.
- Each issue will have the following properties:
  - **Status** (e.g., Open, In Progress, Resolved).
  - **Date** (timestamp when the issue is created or updated).
  - **Issue Text** (a short description of the issue).
- The application must be **secured with authentication**, requiring users to **register** and **log in** to access the features.

Finally, you will **deploy the application** to Render to make it accessible online.

---

## Key Learnings

By completing this exercise, you will strengthen the following skills:

- **Django Models**:
  - Designing models for storing and managing issue data.
  - Utilizing Django ORM for CRUD operations.
- **APIs**:
  - Creating a REST API using Django for communication between the backend and frontend.
  - Consuming the API with React to dynamically display and update data.
- **JWT Authentication**:
  - Securing API endpoints with JSON Web Tokens (JWT).
  - Implementing login and registration flows using JWT in both backend and frontend.
- **React Development**:
  - Building user interfaces to interact with the API.
  - Handling state management and API calls with React.
- **Deployment**:
  - Deploying the full stack application to Render.

---

## User Story

> As a user, I want to securely log in to an issue tracker application so that I can manage my project issues effectively.

---

## Acceptance Criteria

### Backend (Django):

1. **Model Design**:
   - Create a model for storing issue data with fields for status, date, and issue text.
2. **API Implementation**:
   - Build RESTful endpoints for:
     - **List Issues** (GET).
     - **Retrieve Issue Details** (GET by ID).
     - **Create New Issue** (POST).
     - **Update Issue** (PUT).
     - **Delete Issue** (DELETE).
3. **Authentication**:
   - Set up user authentication with **JWT**.
   - Protect API endpoints to allow only authenticated users.

### Frontend (React):

1. **Authentication**:
   - Create login and registration pages.
   - Store and use JWT tokens for secure API communication.
2. **Issue Tracker Interface**:
   - Display a list of issues fetched from the API.
   - Allow users to create, edit, and delete issues.
   - Add status filtering for easier issue management.
3. **User Experience**:
   - Ensure smooth navigation between pages and error handling (e.g., invalid login).

### Deployment:

1. **Backend Deployment**:
   - Deploy the Django backend on **Render** with the API publicly accessible.
2. **Frontend Deployment**:
   - Deploy the React application on **Render**.
3. **Full Stack Integration**:
   - Ensure the frontend communicates seamlessly with the deployed backend.

---

## Steps to Complete

### Step 1: Backend Development

1. Set up a Django project in the `backend` folder.
2. Create models, serializers, and views for the issue tracker API.
3. Implement JWT authentication using `djangorestframework-simplejwt`.
4. Test your API using tools like **Postman** or **cURL**.

### Step 2: Frontend Development

1. Set up a React project in the `frontend` folder using Vite.
2. Create components for login, registration, and the issue tracker interface.
3. Integrate the API with React using `fetch` or libraries like `axios`.
4. Ensure secure API calls with JWT.

### Step 3: Deployment

1. Deploy the Django backend on **Render**.
2. Deploy the React frontend on **Render**.
3. Test the deployed application to ensure all features work as expected.

---

## Additional Notes

- Follow best practices for project structure, such as separating concerns (models, serializers, views).
- Use meaningful commit messages to document your progress in Git.
- Test thoroughly to ensure that your app is secure and bug-free.

---

Good luck, and have fun building your full-stack application! 🎉
