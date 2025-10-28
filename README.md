FastAPI Database CRUD Project

This is a simple FastAPI project that connects to a PostgreSQL database and provides full CRUD (Create, Read, Update, Delete) functionality.

It uses:

SQLAlchemy for database models

Pydantic for request and response validation

📁 Project Structure
project/
│
├── main.py
├── db.py
├── models.py
├── schemas.py
├── services.py
├── requirements.txt
└── README.md

⚙️ Setup Instructions

Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Update your PostgreSQL connection
In db.py, modify the database URL:

SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"


Run the server

uvicorn main:app --reload


Open your browser
Go to:

http://127.0.0.1:8000/docs


Here you can test all CRUD endpoints using the interactive Swagger UI.

🧠 Features

Add new records

View all records

View single record by ID

Update existing records

Delete records
