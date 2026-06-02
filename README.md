# Smart Campus Information System

A Python-based mini project that demonstrates a complete **Smart Campus Information System** integrating student registration, course enrollment, academic record management, analytics, and file handling.

## Features

- Student Registration
- Course Enrollment Management
- Marks Entry and Grade Evaluation
- Student Record Display
- Student Search Functionality
- Sorting Student Records
- JSON File Storage and Loading
- Directory Scanning with Exception Handling
- Performance Analytics using:
  - NumPy
  - Pandas
  - Matplotlib

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- JSON
- OS Module

---

## Project Structure

Smart-Campus-System/
│
├── main.py
├── students.json
├── requirements.txt
└── README.md

---

## Installation

### 1. Clone the Repository

git clone https://github.com/ajith17189/smart-campus-information-system

cd smart-campus-system

### 2. Install Required Libraries

pip install -r requirements.txt

---

## How to Run

python main.py

---

## Main Functionalities

### 1. Student Registration
Register students with:
- Student ID
- Name
- Age

### 2. Course Enrollment
Enroll students into multiple courses.

### 3. Marks Entry
Enter marks for students and automatically calculate grades.

### 4. Grade Calculation

| Average Marks | Grade |
|---|---|
| 90+ | A+ |
| 80+ | A |
| 70+ | B |
| 60+ | C |
| Below 60 | F |

### 5. Fee Calculation

Total Fee = Number of Courses × 5000

### 6. File Handling
- Save student records to students.json
- Load saved records from file

### 7. Performance Analytics
Displays:
- Student averages
- Highest score
- Lowest score
- Bar chart visualization

---

## Example Menu

====== SMART CAMPUS INFORMATION SYSTEM ======
1. Register Student
2. Enroll Course
3. Enter Marks
4. Display Students
5. Search Student
6. Sort Students
7. Save Records
8. Load Records
9. Scan Directory
10. Performance Analytics
11. Exit

---

## Future Improvements

- GUI using Tkinter or PyQt
- Database integration (MySQL/SQLite)
- User Authentication
- Attendance Management
- Web-based Dashboard

---

## Author

Ajith Reddy

---

## License

This project is for educational purposes.
