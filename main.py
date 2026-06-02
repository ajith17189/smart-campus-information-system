import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Student Class
# -----------------------------
class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
        self.courses = []
        self.marks = []

    def add_course(self, course):
        self.courses.append(course)

    def add_marks(self, marks):
        self.marks = marks

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def calculate_fee(self):
        return len(self.courses) * 5000

    def to_dict(self):
        return {
            "ID": self.sid,
            "Name": self.name,
            "Age": self.age,
            "Courses": self.courses,
            "Marks": self.marks,
            "Grade": self.calculate_grade(),
            "Fee": self.calculate_fee()
        }


# -----------------------------
# Campus Management System
# -----------------------------
class SmartCampus:
    def __init__(self):
        self.students = {}

    # Student Registration
    def register_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        self.students[sid] = Student(sid, name, age)

        print("Student Registered Successfully!")

    # Course Enrollment
    def enroll_course(self):
        sid = input("Enter Student ID: ")

        if sid in self.students:
            course = input("Enter Course Name: ")
            self.students[sid].add_course(course)

            print("Course Enrolled Successfully!")
        else:
            print("Student Not Found!")

    # Marks Entry
    def enter_marks(self):
        sid = input("Enter Student ID: ")

        if sid in self.students:
            marks = list(map(int,
                             input("Enter marks (space separated): ").split()))

            self.students[sid].add_marks(marks)

            print("Marks Added Successfully!")
        else:
            print("Student Not Found!")

    # Display Records
    def display_students(self):
        if not self.students:
            print("No Student Records Found")
            return

        for student in self.students.values():
            print(student.to_dict())

    # Search Student
    def search_student(self):
        sid = input("Enter Student ID to Search: ")

        if sid in self.students:
            print(self.students[sid].to_dict())
        else:
            print("Student Not Found")

    # Sort Students
    def sort_students(self):
        sorted_students = sorted(
            self.students.values(),
            key=lambda x: x.name
        )

        print("\nSorted Student Records:")
        for s in sorted_students:
            print(s.to_dict())

    # Save Records
    def save_file(self):
        data = [s.to_dict() for s in self.students.values()]

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Records Saved Successfully!")

    # Load Records
    def load_file(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

            print("\nLoaded Student Records")
            for student in data:
                print(student)

        except FileNotFoundError:
            print("No Saved File Found!")

    # Directory Scanning
    def scan_directory(self):
        path = input("Enter Directory Path: ")

        try:
            files = os.listdir(path)

            print("\nFiles in Directory:")
            for file in files:
                print(file)

        except FileNotFoundError:
            print("Directory Not Found!")

        except PermissionError:
            print("Permission Denied!")

    # Analytics using NumPy, Pandas, Matplotlib
    def analytics(self):

        if not self.students:
            print("No Data Available")
            return

        records = []

        for student in self.students.values():
            avg = np.mean(student.marks) if student.marks else 0

            records.append({
                "Name": student.name,
                "Average": avg
            })

        df = pd.DataFrame(records)

        print("\nStudent Performance Analysis")
        print(df)

        print("\nOverall Average:",
              np.mean(df["Average"]))

        print("Highest Score:",
              np.max(df["Average"]))

        print("Lowest Score:",
              np.min(df["Average"]))

        plt.figure(figsize=(8,5))
        plt.bar(df["Name"], df["Average"])
        plt.title("Student Performance")
        plt.xlabel("Students")
        plt.ylabel("Average Marks")
        plt.show()

    # Main Menu
    def menu(self):

        while True:
            print("\n====== SMART CAMPUS INFORMATION SYSTEM ======")
            print("1. Register Student")
            print("2. Enroll Course")
            print("3. Enter Marks")
            print("4. Display Students")
            print("5. Search Student")
            print("6. Sort Students")
            print("7. Save Records")
            print("8. Load Records")
            print("9. Scan Directory")
            print("10. Performance Analytics")
            print("11. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.register_student()

            elif choice == "2":
                self.enroll_course()

            elif choice == "3":
                self.enter_marks()

            elif choice == "4":
                self.display_students()

            elif choice == "5":
                self.search_student()

            elif choice == "6":
                self.sort_students()

            elif choice == "7":
                self.save_file()

            elif choice == "8":
                self.load_file()

            elif choice == "9":
                self.scan_directory()

            elif choice == "10":
                self.analytics()

            elif choice == "11":
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")


# -----------------------------
# Driver Program
# -----------------------------
campus = SmartCampus()
campus.menu()