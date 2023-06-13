# Flask User Authentication

This repository contains a simple Flask application that implements a user authentication system. It provides endpoints for user registration and user login.

## Endpoints

### 1. User Registration

Accepts a JSON object containing a username and password, stores them in a dictionary (as a stand-in for a real database), and returns a success message.

- **Endpoint:** `/register`
- **Method:** POST
- **Request Body:**

{
"username": "Ahmed",
"password": "secretpassword"
}

- **Response:**
{
"message": "User registration successful."
}


### 2. User Login

Accepts a JSON object containing a username and password, checks if the provided username and password match the stored values, and returns an "access granted" message if successful; otherwise, returns an "access denied" message.

- **Endpoint:** `/login`
- **Method:** POST
- **Request Body:**
{
"username": "Ahmed",
"password": "secretpassword"
}
- **Response (Successful):**
{
"message": "Access granted. Welcome, Ahmed!"
}

- **Response (Access Denied):**
{
"error": "Access denied. Invalid username or password."
}

The user credentials are stored in a dictionary within the application, serving as a simplified representation of a real database.

## Running the Application

To run the Flask application, make sure you have Python and Flask installed. Then, execute 

