# Backend - Trivia API

## Overview

This directory contains the Flask backend for the Trivia API Project. The backend exposes a RESTful API that allows the frontend application to manage trivia questions, categories, search, deletion, and quiz gameplay.

The backend is built with:

- Python
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- PostgreSQL
- unittest

The API supports the following main actions:

- Retrieve all trivia categories.
- Retrieve paginated trivia questions.
- Retrieve questions by category.
- Add new trivia questions.
- Delete existing trivia questions.
- Search questions by keyword.
- Play a quiz game with random questions.
- Return JSON-formatted error responses.

---

## Backend Project Structure

```text
backend/
├── flaskr/
│   ├── __init__.py
│   └── models.py
├── test_flaskr.py
├── requirements.txt
├── setup-trivia.sql
├── setup-test.sql
├── trivia.psql
├── books.psql
└── README.md
```

### Important Files

| File | Description |
|---|---|
| `flaskr/__init__.py` | Main Flask application file. Contains API routes, CORS configuration, and error handlers. |
| `models.py` | SQLAlchemy database models and database setup logic. |
| `test_flaskr.py` | Unit tests for the API endpoints. |
| `requirements.txt` | Python dependencies required by the backend. |
| `trivia.psql` | SQL dump used to populate the trivia database. |
| `setup-trivia.sql` | SQL setup file for the main trivia database. |
| `setup-test.sql` | SQL setup file for the test database. |

---

## Database Setup

The project uses PostgreSQL with two databases:

```text
trivia
trivia_test
```

In the Udacity workspace, use the provided database setup button to start PostgreSQL and populate both databases.

To inspect the main database manually, run:

```bash
su - postgres bash -c "psql trivia"
```

Inside the PostgreSQL prompt, you can run:

```sql
\dt
SELECT * FROM categories;
SELECT * FROM questions LIMIT 5;
\q
```

Expected tables:

```text
categories
questions
```

---

## Installing Backend Dependencies

From the project root, navigate to the backend directory:

```bash
cd backend
```

Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

If the dependencies are already installed in the Udacity workspace, the command may return `Requirement already satisfied`, which is expected.

---

## Running the Backend Server

From the `backend` directory, run:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

The backend runs locally at:

```text
http://127.0.0.1:5000
```

If you see this error:

```text
OSError: [Errno 98] Address already in use
```

it means the Flask server is already running on port `5000`.

You can verify that the backend is running with:

```bash
curl http://127.0.0.1:5000/categories
```

Expected response:

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}
```

---

## Running Backend Tests

The test suite is located in:

```text
test_flaskr.py
```

To run the tests:

```bash
python3 test_flaskr.py
```

Expected result:

```text
Ran 13 tests
OK
```

The tests validate successful behavior and expected error behavior for the main API endpoints.

---

# API Documentation

Base URL:

```text
http://127.0.0.1:5000
```

---

## GET `/categories`

Fetches all available trivia categories.

### Request Arguments

None.

### Example Request

```bash
curl http://127.0.0.1:5000/categories
```

### Response Body

```json
{
  "success": true,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

---

## GET `/questions?page=<page_number>`

Fetches a paginated list of trivia questions. Each page returns up to 10 questions.

### Request Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| page | integer | No | Page number used for pagination. Defaults to 1. |

### Example Request

```bash
curl http://127.0.0.1:5000/questions?page=1
```

### Response Body

```json
{
  "success": true,
  "questions": [
    {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "difficulty": 4,
      "category": 5
    }
  ],
  "totalQuestions": 19,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": null
}
```

---

## GET `/categories/<category_id>/questions`

Fetches questions that belong to a specific category.

### Request Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| category_id | integer | Yes | ID of the selected category. |

### Example Request

```bash
curl http://127.0.0.1:5000/categories/3/questions
```

### Response Body

```json
{
  "success": true,
  "questions": [
    {
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "answer": "Lake Victoria",
      "difficulty": 2,
      "category": 3
    }
  ],
  "totalQuestions": 4,
  "currentCategory": "Geography"
}
```

---

## DELETE `/questions/<question_id>`

Deletes a trivia question by ID.

### Request Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| question_id | integer | Yes | ID of the question to delete. |

### Example Request

```bash
curl -X DELETE http://127.0.0.1:5000/questions/5
```

### Response Body

```json
{
  "success": true,
  "deleted": 5,
  "questions": [],
  "totalQuestions": 18
}
```

---

## POST `/questions`

Creates a new trivia question.

### Request Body

```json
{
  "question": "What is the capital of Spain?",
  "answer": "Madrid",
  "difficulty": 1,
  "category": 3
}
```

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/questions \
-H "Content-Type: application/json" \
-d '{
  "question": "What is the capital of Spain?",
  "answer": "Madrid",
  "difficulty": 1,
  "category": 3
}'
```

### Response Body

```json
{
  "success": true,
  "created": 24,
  "questions": [],
  "totalQuestions": 19
}
```

---

## POST `/questions` Search

Searches for trivia questions containing a specific text value.

### Request Body

```json
{
  "searchTerm": "title"
}
```

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/questions \
-H "Content-Type: application/json" \
-d '{
  "searchTerm": "title"
}'
```

### Response Body

```json
{
  "success": true,
  "questions": [
    {
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "answer": "Edward Scissorhands",
      "difficulty": 3,
      "category": 5
    }
  ],
  "totalQuestions": 1,
  "currentCategory": null
}
```

---

## POST `/quizzes`

Returns a random quiz question. The returned question is not included in the list of previous questions. If a category is selected, the returned question belongs to that category.

### Request Body for All Categories

```json
{
  "previous_questions": [],
  "quiz_category": {
    "id": 0,
    "type": "click"
  }
}
```

### Request Body for a Specific Category

```json
{
  "previous_questions": [13, 15],
  "quiz_category": {
    "id": 3,
    "type": "Geography"
  }
}
```

### Example Request

```bash
curl -X POST http://127.0.0.1:5000/quizzes \
-H "Content-Type: application/json" \
-d '{
  "previous_questions": [],
  "quiz_category": {
    "id": 3,
    "type": "Geography"
  }
}'
```

### Response Body

```json
{
  "success": true,
  "question": {
    "id": 13,
    "question": "What is the largest lake in Africa?",
    "answer": "Lake Victoria",
    "difficulty": 2,
    "category": 3
  }
}
```

If there are no remaining questions available, the API returns:

```json
{
  "success": true,
  "question": null
}
```

---

# Error Handling

The API returns JSON responses for expected errors.

## Error Response Format

```json
{
  "success": false,
  "error": 404,
  "message": "resource not found"
}
```

---

## 400 Bad Request

Returned when the request body is missing required fields or contains invalid input.

```json
{
  "success": false,
  "error": 400,
  "message": "bad request"
}
```

---

## 404 Resource Not Found

Returned when a requested route or resource does not exist.

```json
{
  "success": false,
  "error": 404,
  "message": "resource not found"
}
```

---

## 422 Unprocessable

Returned when the server understands the request but cannot process it.

```json
{
  "success": false,
  "error": 422,
  "message": "unprocessable"
}
```

---

## 500 Internal Server Error

Returned when an unexpected server-side error occurs.

```json
{
  "success": false,
  "error": 500,
  "message": "internal server error"
}
```

---

# Completed Backend Features

- Flask backend configured.
- PostgreSQL database connected.
- CORS enabled for cross-origin requests.
- Categories endpoint implemented.
- Questions endpoint implemented with pagination.
- Delete question endpoint implemented.
- Create question endpoint implemented.
- Search questions endpoint implemented.
- Category filtering endpoint implemented.
- Quiz endpoint implemented.
- JSON error handlers implemented.
- Unit tests implemented with `unittest`.

---

# Notes

The backend is designed to run locally or in the Udacity workspace using HTTP:

```text
http://127.0.0.1:5000
```

HTTPS is not required for this development project.