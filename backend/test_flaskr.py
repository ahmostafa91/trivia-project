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
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name) #change path for my local db
        # self.database_path = 'postgresql://postgres:123456@localhost:5432/trivia'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['categories'])

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_create_question(self):
        test_question = {
        'question': 'How can we see?',
        'answer': 'eyes',
        'category': '1',
        'difficulty': 1,
        }

        res = self.client().post('/questions', json=test_question)
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(data['created'])

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/5')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    def test_get_questions_by_category(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    def test_invalid_page_numbers(self):
        res = self.client().get('/questions?page=9999999999')
        data = json.loads(res.data)
        
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
        
    def test_search_question(self):
    
        res = self.client().post('/questions/search', json={"searchTerm": 'Who invented Peanut Butter?'})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])

    def test_invalid_search(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'not a question!!!'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])

    def test_get_quizzes(self):
        test_data = {
            'previous_questions': [],
            'quiz_category': {'type': 'Art', 'id': 2}
        }

        res = self.client().post('/quizzes', json=test_data)
        data = json.loads(res.data)

        self.assertEqual(data['status'], 200)
        self.assertEqual(data['message'], 'questions successfully returned')
        self.assertTrue(data['question'])

        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
