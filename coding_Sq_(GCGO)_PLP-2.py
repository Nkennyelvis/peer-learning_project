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
        
    # Insert a grade into the database
    def insert_grade(self, name, subject, level, score, total, percentage):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO grades (name, subject, level, score, total, percentage)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, subject, level, score, total, percentage))
            conn.commit()

    # Fetch all grades from the database
    def fetch_grades(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM grades")
            return cursor.fetchall()

    # Delete a quiz from the database
    def delete_quiz(self, quiz_id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM quizzes WHERE id=?", (quiz_id,))
            conn.commit()

    # Update an existing quiz in the database
    def update_quiz(self, quiz_id, question, options, correct_answer):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE quizzes 
                SET question=?, options=?, correct_answer=? 
                WHERE id=?
            """, (question, options, correct_answer, quiz_id))
            conn.commit()

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

    # Create a quiz (Multiple Choice or Open Ended)
    def create_quiz(self):
        while True:
            print("\n1. Multiple Choice Quiz")
            print("2. Open Ended Quiz")
            print("3. Back")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_mcq()
            elif choice == "2":
                self.create_open_ended()
            elif choice == "3":
                return
            else:
                print("Invalid choice, Please try again!!")

    # Create a Multiple Choice Quiz
    def create_mcq(self):
        subject = input("Enter the course/subject name: ").lower()
        level = input("Enter the level (Beginner, Intermediate, Advanced): ").lower()
        num_questions = int(input("How many questions do you want to add (max 10)? "))
        
        if num_questions > 10:
            print("Max 10 questions allowed.")
            return
        
        for _ in range(num_questions):
            question = input("Question: ")
            options = [input(f"Option {i+1}: ") for i in range(4)]
            correct_answer = int(input("Enter the correct option (1-4): ")) - 1
            
            self.db.insert_quiz(subject, level, question, ",".join(options), correct_answer, "mcq")
        print("Quiz created successfully!")

    # Create an Open Ended Quiz
    def create_open_ended(self):
        subject = input("Enter the course/subject name: ").lower()
        level = input("Enter the level (Beginner, Intermediate, Advanced): ").lower()
        num_questions = int(input("How many questions do you want to add (max 10)? "))
        
        if num_questions > 10:
            print("Max 10 questions allowed.")
            return
        
        for _ in range(num_questions):
            question = input("Question: ")
            answer = input("Correct answer: ")
            
            self.db.insert_quiz(subject, level, question, answer, None, "open")
        print("Quiz created successfully!")

    # Delete a quiz from the database
    def delete_quiz(self):
        admin_pass = input("Enter admin passcode to delete a quiz: ")
        if admin_pass == "33333":
            subject = input("Enter the subject of the quiz to delete: ").lower()
            level = input("Enter the level of the quiz to delete: ").lower()
            quizzes = self.db.fetch_quizzes(subject, level)
            
            if not quizzes:
                print("No quizzes found for this subject and level.")
                return
            
            print("Available quizzes:")
            for quiz in quizzes:
                print(f"ID: {quiz[0]}, Question: {quiz[3]}")
            
            quiz_id = int(input("Enter the quiz ID to delete: ")).lower()
            self.db.delete_quiz(quiz_id)
            print("Quiz deleted successfully!")
        else:
            print("Incorrect passcode. Access denied.")

    # Edit a quiz in the database
    def edit_quiz(self):
        admin_pass = input("Enter admin passcode to edit a quiz: ")
        if admin_pass == "33333":
            subject = input("Enter the subject of the quiz to edit: ").lower()
            level = input("Enter the level of the quiz to edit: ").lower()
            quizzes = self.db.fetch_quizzes(subject, level)
            
            if not quizzes:
                print("No quizzes found for this subject and level.")
                return
            
            print("Available quizzes:")
            for quiz in quizzes:
                print(f"ID: {quiz[0]}, Question: {quiz[3]}")
            
            quiz_id = int(input("Enter the quiz ID to edit: "))
            question = input("Enter new question: ")
            options = ",".join([input(f"Option {i+1}: ") for i in range(4)])
            correct_answer = int(input("Enter the correct option (1-4): ")) - 1
            self.db.update_quiz(quiz_id, question, options, correct_answer)
            print("Quiz updated successfully!")
        else:
            print("Incorrect passcode. Access denied.")

    # Take a quiz (user answers the questions)
    def take_quiz(self):
        subject = input("Enter the subject you want to take: ").lower()
        level = input("Enter the level (Beginner, Intermediate, Advanced): ").lower()
        quizzes = self.db.fetch_quizzes(subject, level)
        
        if not quizzes:
            print("No quizzes available for this subject and level.")
            return
        
        score = 0
        total = len(quizzes)
        
        for quiz in quizzes:
            question, options, correct_answer, q_type = quiz[3], quiz[4], quiz[5], quiz[6]
            print(f"\n{question}")
            
            if q_type == "mcq":
                options_list = options.split(",")
                for idx, option in enumerate(options_list, 1):
                    print(f"{idx}. {option}")
                answer = int(input("Enter your choice (1-4): ")) - 1
                if answer == correct_answer:
                    score += 1
            else:
                answer = input("Your answer: ").lower()
                if answer == options.lower():
                    score += 1
        
        percentage = (score / total) * 100
        print(f"Your final score: {percentage:.2f}% ({score}/{total})")
        
        name = input("Enter your name: ")
        self.db.insert_grade(name, subject, level, score, total, percentage)

    # View grades of all users
    def view_grades(self):
        grades = self.db.fetch_grades()
        if not grades:
            print("No grades available.")
            return
        
        print("\nGrades:")
        for grade in grades:
            print(f"{grade[1]} - {grade[2]} ({grade[3]}): {grade[4]}/{grade[5]} ({grade[6]:.2f}%)")

# Running the application
app = QuizApp().main_menu()