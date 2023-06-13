# Flask API

This repository contains a simple Flask API with two endpoints. It provides functionality to perform basic operations on data sent as JSON objects.

## Endpoints

### 1. Sum of Numbers

Accepts a JSON object containing a list of numbers and returns the sum of the numbers.

- **Endpoint:** `/sum`
- **Method:** POST
- **Request Body:**
{
"numbers": [1, 2, 3, 4, 5]
}

- **Response:**
{
"sum": 15
}


### 2. Concatenate Strings

Accepts a JSON object containing two strings and returns the concatenated result.

- **Endpoint:** `/concatenate`
- **Method:** POST
- **Request Body:**
{
"strings": ["Hello", "World"]
}

- **Response:**
{
"concatenated_string": "HelloWorld"
}


The API also handles error cases and returns appropriate error messages.

## Running the API

To run the Flask API, make sure you have Python and Flask installed. Then, execute the following command:

