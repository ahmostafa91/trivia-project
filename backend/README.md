# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


# Full Stack Trivia API Backend

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the
[python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

It is preferred if you run this in a virtual environment for python. If you are using `pipenv`, virtual environment
would be taken care of by `pipenv`. Instructions for setting up a virtual environment for your platform can be found in
the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pipenv install
```
or if you are not using `pipenv`:
```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend micro-services framework. Flask is required to handle
requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite
database. You'll primarily work in app.py and can reference models.py.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests
from our frontend server.

## Database Setup (_Important_)
Install and setup "PostgreSQL" on the system and create a database named `trivia` in the Postgres server.
```bash
createdb trivia
```

Instructions (macOS): https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
cd database
psql trivia < database/trivia.psql
```

## Running the server

Ensure you are working using your created virtual environment.

To run the server, execute:
```bash
export FLASK_APP=flaskr
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.
The application will be served on **http://localhost:5000**

## Testing

To run the flask tests, run the following command:
```bash
python -m unittest discover -t ../
```
_NOTE_: Make sure you create a database named `trivia` in the PostgreSQL server before running the tests.


## API Documentation
* GET "/categories"
    - Fetches a dictionary of categories
	- Response Body:
    
    `/categories`:
```json
{"categories: {
"1":"Science",
"2":"Art",
"3":"Geography",
"4":"History",
"5":"Entertainment",
"6":"Sports"},
"success":true}
```

* GET "/questions"
    - Fetches all questions to be displayed on the page .:

    `/questions`: 
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
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ], 
  "success": true, 
  "total_questions": 102
}
```


* GET "/questions?page=1"
    - Fetches the questions to be displayed on the page using page number
    - Request Parameters: `page`: Page number
    - Response Body:

    `/questions?page=1`: 
```json
{"categories":{"1":"Science","2":"Art","3":"Geography","4":"History","5":"Entertainment","6":"Sports"},"questions":[{"answer":"eyes","category":1,"difficulty":1,"id":108,"question":"How can we see?"}],"success":true,"total_questions":102}
```

* DELETE "/questions/id=1"
    - Deletes a question from the database
    - Request Parameters: `id`: question ID to delete
    - Response Body:

    `/questions/id=1`: 
```json
{
  'success': True,
  'message': "Deleted successfully"
}
```

* POST "/questions"
    - Adds a questions to the database
    - Request Body:
    
    `question`: Question statement
    
    `answer`: Answer statement
    
    `category`: Category ID
    
    `difficulty`: Difficulty Level
    - Response Body:
    
    `question`: Questions list plus the add question
	    
    `created`: The new created question id
	    
    `success`: The status
	    
    `total_questions`: Total questions count in db
```json
{
  "question": [
      {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ]
    "created": 110,,
    "success": true,
    "total_questions": 103
}
```

* POST "/questions/search"
    - Fetches questions based on the search term
    - Request Body:
    
    `searchTerm`: Search term
    - Response Body:
    
    `questions`: List of questions found in search
    
    `success`: Search status
	    
    `total_questions`: Total number of  questions
```json
{
    "questions": [
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

* GET "/categories/category_id/questions"
    - Fetches questions for the requested category
    - Request Parameters: `category_id`: Category ID for questions
    - Response Body:

    `questions`: List of category questions

    `total_questions`: Total number of  questions
    
    `current_category`: Current category ID
```json
{
  "questions": [{
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        }],
  "success": true,
  "total_questions": 87,
  "current_category": "Science",
}
```

* POST "/quizzes"
    - Fetches a unique question for the quiz on selected category
    - Request Body:
    
    `previous_questions`: List of previously answered questions

    `quiz_category`: Category object of the quiz
    - Response Body:
    
    `message`: Featch status message
	
	`question`: Random question of requested category

    `status`: Response status code

    `success`: Response status

```json
{
    "message": "questions successfully returned",
    "question": {
        "answer": "Mona Lisa",
        "category": 2,
        "difficulty": 3,
        "id": 17,
        "question": "La Giaconda is better known as what?"
    },
    "status": 200,
    "success": true
}
```