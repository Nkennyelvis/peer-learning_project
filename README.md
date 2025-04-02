# Coding SQ Quiz Application

## Overview

The **Coding SQ Quiz Application** is a command line based quiz system built using **Python** and **SQLite**. It allows users to create, edit, delete, and take quizzes on various subjects and levels. The app also records scores and allows users to view their grades.

## Features

- **Create Quizzes:** Admins can create multiple-choice and open-ended quizzes.
- **Edit & Delete Quizzes:** Admins can modify or remove quizzes using a secure passcode.
- **Take Quizzes:** Users can select a subject and level, answer questions, and get graded.
- **Grade Storage:** Scores are stored in an SQLite database and can be retrieved anytime.

## Technologies Used

- **Python** (Core Logic)
- **SQLite** (Database Management)

## Installation & Setup

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/Nkennyelvis/peer-learning_project/
   cd quiz-app
   ```

2. **Ensure Python is Installed:**
   The app requires Python 3. Install it from [python.org](https://www.python.org/) if necessary.

3. **Run the Application:**

   ```sh
   python main.py
   ```

## Usage Guide

### Running the Quiz Application

Upon launching the app, you will see a menu with the following options:

1. **Create a Quiz** (Requires Admin Passcode: \*\*\*\*\*)
2. **Edit a Quiz** (Requires Admin Passcode)
3. **Delete a Quiz** (Requires Admin Passcode)
4. **Take a Quiz** (Answer questions and get scored)
5. **View Grades** (Check stored grades of all users)
6. **Quit** (Exit the application)

### Adding Questions

- **Multiple Choice:**
  - Enter the question and four answer choices.
  - Specify the correct option (1-4).
- **Open Ended:**
  - Enter the question and the correct answer.

### Taking a Quiz

- Select a **subject** and **level**.
- Answer the given questions.
- At the end, your score and percentage will be displayed.
- Your result is stored in the database.

## Contributing

1. **Fork the Repository**
2. **Create a New Branch** (`git checkout -b feature-branch`)
3. **Commit Changes** (`git commit -m "Added new feature"`)
4. **Push to GitHub** (`git push origin feature-branch`)
5. **Create a Pull Request**

## License

This project is open-source and free to use. Modify and distribute it as needed.

## Credits

This project was developed by **The Coding SQ Team:**

- **Ineza Manzi Arnaud**
- **Kenny Elvis**
- **Moaye Kouame**
- **Seth Iradukunda**
- **TitoSibo**
- **Julia Rubibi**
- **Lydvine Umutesi**

---

Created by **The Coding SQ Team** 🎉

