import sqlite3

# Database class to interact with SQLite database
class QuizDatabase:
    def __init__(self, db_name="quiz.db"):
        self.db_name = db_name
        self.initialize_db()

    # Establish a connection to the SQLite database
    def connect(self):
        return sqlite3.connect(self.db_name)
    
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
if __name__ == "__main__":
    app = QuizApp()
    app.main_menu()
