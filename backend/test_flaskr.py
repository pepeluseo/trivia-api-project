import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "student",
            "student",
            "localhost:5432",
            self.database_name
        )

        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "What is the capital of Portugal?",
            "answer": "Lisbon",
            "difficulty": 1,
            "category": 3
        }

        self.search_payload = {
            "searchTerm": "title"
        }

        self.quiz_payload = {
            "previous_questions": [],
            "quiz_category": {
                "id": 3,
                "type": "Geography"
            }
        }

        self.invalid_quiz_payload = {
            "previous_questions": [],
            "quiz_category": {
                "id": "abc",
                "type": "Invalid"
            }
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    # ---------------------------------------------------------
    # GET /categories
    # ---------------------------------------------------------

    def test_get_categories_success(self):
        res = self.client.get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("categories", data)
        self.assertGreaterEqual(len(data["categories"]), 1)

    # ---------------------------------------------------------
    # GET /questions
    # ---------------------------------------------------------

    def test_get_questions_success(self):
        res = self.client.get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("questions", data)
        self.assertIn("totalQuestions", data)
        self.assertIn("categories", data)
        self.assertIn("currentCategory", data)
        self.assertLessEqual(len(data["questions"]), 10)

    def test_get_questions_page_not_found(self):
        res = self.client.get("/questions?page=9999")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)

    # ---------------------------------------------------------
    # DELETE /questions/<id>
    # ---------------------------------------------------------

    def test_delete_question_success(self):
        question = Question(
            question="Temporary test question?",
            answer="Temporary test answer",
            difficulty=1,
            category=3
        )
        question.insert()
        question_id = question.id

        res = self.client.delete("/questions/{}".format(question_id))
        data = json.loads(res.data)

        deleted_question = Question.query.filter(
            Question.id == question_id
        ).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], question_id)
        self.assertIsNone(deleted_question)

    def test_delete_question_not_found(self):
        res = self.client.delete("/questions/999999")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)

    # ---------------------------------------------------------
    # POST /questions - create question
    # ---------------------------------------------------------

    def test_create_question_success(self):
        res = self.client.post(
            "/questions",
            json=self.new_question
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("created", data)
        self.assertIn("totalQuestions", data)

    def test_create_question_bad_request(self):
        res = self.client.post(
            "/questions",
            json={}
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 400)

    # ---------------------------------------------------------
    # POST /questions - search questions
    # ---------------------------------------------------------

    def test_search_questions_success(self):
        res = self.client.post(
            "/questions",
            json=self.search_payload
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("questions", data)
        self.assertIn("totalQuestions", data)
        self.assertIn("currentCategory", data)

    # ---------------------------------------------------------
    # GET /categories/<id>/questions
    # ---------------------------------------------------------

    def test_get_questions_by_category_success(self):
        res = self.client.get("/categories/3/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("questions", data)
        self.assertIn("totalQuestions", data)
        self.assertIn("currentCategory", data)
        self.assertEqual(data["currentCategory"], "Geography")

        for question in data["questions"]:
            self.assertEqual(question["category"], 3)

    def test_get_questions_by_category_not_found(self):
        res = self.client.get("/categories/999/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)

    # ---------------------------------------------------------
    # POST /quizzes
    # ---------------------------------------------------------

    def test_play_quiz_success(self):
        res = self.client.post(
            "/quizzes",
            json=self.quiz_payload
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertIn("question", data)

        if data["question"] is not None:
            self.assertEqual(data["question"]["category"], 3)

    def test_play_quiz_unprocessable(self):
        res = self.client.post(
            "/quizzes",
            json=self.invalid_quiz_payload
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 422)

    # ---------------------------------------------------------
    # Generic 404
    # ---------------------------------------------------------

    def test_404_for_invalid_route(self):
        res = self.client.get("/invalid-route")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["error"], 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()