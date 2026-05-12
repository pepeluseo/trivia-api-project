# Trivia API Project

## Project Overview

Trivia API is a full-stack web application built for managing and playing trivia questions. The frontend is built with React, and the backend is built with Flask, SQLAlchemy, PostgreSQL, and Flask-CORS.

The application allows users to:

- View trivia questions with pagination.
- View all available categories.
- Filter questions by category.
- Add new trivia questions.
- Delete existing questions.
- Search questions by text.
- Play a quiz game using all categories or a selected category.
- Receive JSON error responses for common API errors.

---

## Project Structure

```text
PROYECTO-API/
├── backend/
│   ├── flaskr/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── test_flaskr.py
│   ├── requirements.txt
│   ├── setup-trivia.sql
│   ├── setup-test.sql
│   └── trivia.psql
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── README.md
├── screenshots/
│   ├── API_DELETE.png
│   ├── API_POST.png
│   ├── API_QUESTIONS.png
└── README.md
```

---

## Backend Setup

### 1. Start PostgreSQL and Set Up the Database

This project uses PostgreSQL with two databases:

- `trivia`
- `trivia_test`

If you are running the project locally, create and populate the databases using the provided SQL files in the `backend` directory.

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

---

### 2. Install Backend Dependencies

Navigate to the backend directory:

```bash
cd backend
```

Install the required Python dependencies:

```bash
pip3 install -r requirements.txt
```

---

### 3. Run the Backend Server

From the `backend` directory, run:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

The backend runs locally on:

```text
http://127.0.0.1:5000
```

To verify that the backend is running:

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

## Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the frontend development server:

```bash
npm start
```

The frontend runs locally on:

```text
http://localhost:3000
```

---

## Running Tests

The test suite is located in:

```text
backend/test_flaskr.py
```

To run the tests, navigate to the backend directory:

```bash
cd backend
```

Then execute:

```bash
python3 test_flaskr.py
```

Expected result:

```text
Ran 13 tests
OK
```

The tests cover successful and error behavior for the main API endpoints.

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

Fetches all questions for a specific category.

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

Deletes a question by ID.

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

Searches for trivia questions containing a specific search term.

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
    "id": 15,
    "question": "The Taj Mahal is located in which Indian city?",
    "answer": "Agra",
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

Returned when the request body is missing required fields or has invalid input.

```json
{
  "success": false,
  "error": 400,
  "message": "bad request"
}
```

---

## 404 Resource Not Found

Returned when a requested resource or route does not exist.

```json
{
  "success": false,
  "error": 404,
  "message": "resource not found"
}
```

---

## 422 Unprocessable

Returned when the request cannot be processed.

```json
{
  "success": false,
  "error": 422,
  "message": "unprocessable"
}
```

---

## 500 Internal Server Error

Returned when an unexpected server error occurs.

```json
{
  "success": false,
  "error": 500,
  "message": "internal server error"
}
```

---

# Completed Features

- Flask backend configured.
- PostgreSQL database connected.
- CORS enabled.
- Categories endpoint implemented.
- Questions endpoint implemented with pagination.
- Delete question endpoint implemented.
- Create question endpoint implemented.
- Search questions endpoint implemented.
- Category filtering endpoint implemented.
- Quiz endpoint implemented.
- Error handlers implemented.
- Unit tests implemented with `unittest`.

---

# Technologies Used

- Python
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- PostgreSQL
- React
- Node.js
- NPM
- unittest

---

# Notes


```text
Backend: http://127.0.0.1:5000
Frontend: http://localhost:3000
```
