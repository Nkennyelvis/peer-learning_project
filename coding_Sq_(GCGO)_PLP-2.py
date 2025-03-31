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

    # Clear all quizzes from the database
    def clear_database(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM quizzes")
            conn.commit()

    # Insert a new quiz into the database
    def insert_quiz(self, subject, level, question, options, correct_answer, q_type):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO quizzes (subject, level, question, options, correct_answer, type)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (subject, level, question, options, correct_answer, q_type))
            conn.commit()

    # Fetch quizzes from the database based on subject and level
    def fetch_quizzes(self, subject, level):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM quizzes WHERE subject=? AND level=?", (subject, level))
            return cursor.fetchall()
         
 # Main application class
class QuizApp:
    def __init__(self):
        self.db = QuizDatabase()

    # Main menu for the quiz application
    def main_menu(self):
        while True:
            print("\nWelcome to the Coding SQ Quiz Application")
            print("1. Create a Quiz")
            print("2. Edit a Quiz")
            print("3. Delete a Quiz")
            print("4. Take a Quiz")
            print("5. View Grades")
            print("6. Quit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                admin_pass = input("Enter admin passcode: ")
                if admin_pass == "33333":
                    self.create_quiz()
                else:
                    print("Incorrect passcode. Access denied.")
            elif choice == "2":
                self.edit_quiz()
            elif choice == "3":
                self.delete_quiz()
            elif choice == "4":
                self.take_quiz()
            elif choice == "5":
                self.view_grades()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")