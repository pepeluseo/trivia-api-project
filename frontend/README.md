# Frontend - Trivia API

## Overview

This directory contains the React frontend for the Trivia API Project. The frontend communicates with the Flask backend to display trivia questions, filter by category, add questions, delete questions, search questions, and play the quiz game.

The frontend is built with:

- React
- JavaScript
- HTML
- CSS
- Node.js
- NPM

The frontend depends on the backend API running locally on port `5000`.

---

## Frontend Project Structure

```text
frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── FormView.js
│   │   ├── QuestionView.js
│   │   └── QuizView.js
│   ├── stylesheets/
│   ├── App.js
│   └── index.js
├── package.json
├── package-lock.json
└── README.md
```

### Important Files

| File | Description |
|---|---|
| `src/components/QuestionView.js` | Displays trivia questions, categories, pagination, and delete actions. |
| `src/components/FormView.js` | Handles adding new trivia questions. |
| `src/components/QuizView.js` | Handles quiz gameplay. |
| `src/App.js` | Main React application component. |
| `package.json` | Defines frontend dependencies and scripts. |

---

## Backend Requirement

Before running the frontend, make sure the backend server is running.

From the backend directory:

```bash
cd backend
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

The backend should be available at:

```text
http://127.0.0.1:5000
```

You can verify it with:

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

## Installing Frontend Dependencies

From the project root, navigate to the frontend directory:

```bash
cd frontend
```

Install the required dependencies:

```bash
npm install
```

If dependencies are already installed in the Udacity workspace, this step may not be necessary.

---

## Running the Frontend

From the `frontend` directory, run:

```bash
npm start
```

The frontend runs locally at:

```text
http://localhost:3000
```

In the Udacity workspace, open the frontend using the provided app preview or `jupyter:3000` link from the workspace interface.

If you see:

```text
Something is already running on port 3000.
Would you like to run the app on another port instead?
```

it means the frontend is already running. You can answer:

```text
n
```

and use the already running frontend instance.

---

## Verifying the Frontend Server

You can verify that the React app is running with:

```bash
curl http://127.0.0.1:3000
```

A successful response returns the React HTML page containing:

```html
<div id="root"></div>
```

---

# Frontend Features

The frontend allows users to:

- View trivia questions.
- Navigate questions using pagination.
- View all available categories.
- Filter questions by category.
- Add new trivia questions.
- Delete trivia questions.
- Search questions by text.
- Play a quiz using all categories or a selected category.
- Receive feedback during quiz gameplay.

---

# API Endpoints Used by the Frontend

The frontend communicates with the backend using the following endpoints:

```text
GET    /categories
GET    /questions?page=<page_number>
GET    /categories/<category_id>/questions
DELETE /questions/<question_id>
POST   /questions
POST   /quizzes
```

---

## GET `/categories`

Used to fetch the list of available trivia categories.

Expected response:

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

Used to fetch paginated trivia questions.

Expected response includes:

```json
{
  "success": true,
  "questions": [],
  "totalQuestions": 19,
  "categories": {},
  "currentCategory": null
}
```

---

## GET `/categories/<category_id>/questions`

Used when the user clicks a category in the left column.

Expected response includes:

```json
{
  "success": true,
  "questions": [],
  "totalQuestions": 4,
  "currentCategory": "Geography"
}
```

---

## DELETE `/questions/<question_id>`

Used when the user deletes a question from the list.

Expected response includes:

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

Used for two frontend actions:

1. Adding a new question.
2. Searching questions by text.

### Add Question Request Body

```json
{
  "question": "What is the capital of Spain?",
  "answer": "Madrid",
  "difficulty": 1,
  "category": 3
}
```

### Search Request Body

```json
{
  "searchTerm": "title"
}
```

---

## POST `/quizzes`

Used during quiz gameplay.

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
  "previous_questions": [],
  "quiz_category": {
    "id": 3,
    "type": "Geography"
  }
}
```

Expected response:

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

---

# Manual Frontend Testing Checklist

After starting both backend and frontend, verify the following in the browser:

## List View

- Questions are displayed.
- Categories are displayed.
- Pagination works.
- Answers can be shown or hidden.

## Category Filtering

- Click a category such as `Geography`.
- Only questions from that category should be shown.

## Add Question

- Open the Add tab.
- Submit a new question with question text, answer, difficulty, and category.
- The form should clear after submission.
- The new question should appear in the questions list.

## Search

- Search for a term such as `title`.
- The list should update with matching questions only.

## Delete

- Click the delete button on a question.
- The question should be removed from the list.

## Play

- Open the Play tab.
- Select `All` or a specific category.
- Answer questions one by one.
- The app should show whether the answer was correct or incorrect.

---

# Notes

The frontend is designed to run locally or in the Udacity workspace using HTTP:

```text
http://localhost:3000
```

The backend must be running at:

```text
http://127.0.0.1:5000
```

HTTPS is not required for this development project.

The `jupyter:3000` reference in the Udacity workspace is an interface link, not a terminal command.
