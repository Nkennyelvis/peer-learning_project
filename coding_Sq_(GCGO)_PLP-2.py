import sqlite3

# Database class to interact with SQLite database 
class QuizDatabase:
    def __init__(self, db_name="quiz.db"):
        self.db_name = db_name
        self.initialize_db()

    # Establish a connection to the SQLite database
    def connect(self):
        return sqlite3.connect(self.db_name)

    # Initialize the database with the necessary tables
    def initialize_db(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quizzes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject TEXT,
                    level TEXT,
                    question TEXT,
                    options TEXT,
                    correct_answer INTEGER,
                    type TEXT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    subject TEXT,
                    level TEXT,
                    score INTEGER,
                    total INTEGER,
                    percentage REAL
                )
            """)
            conn.commit()