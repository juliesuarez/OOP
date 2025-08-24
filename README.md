Student Management System built using Python. It demonstrates fundamental Object-Oriented Programming (OOP) principles by organizing the code into logical, reusable classes.
Description

The application allows a user to manage a list of students. The user can perform three main operations:

    Add a new student to the system.

    List all students currently in the system.

    Search for a specific student using their unique ID.

This project was created to fulfill an assignment focused on applying core OOP concepts in a practical way.
Features

    Add Student: Prompts the user for a name and a unique student ID, then creates a new student record. Includes a check to prevent duplicate student IDs.

    List Students: Displays the details (Name, ID, and Courses) for every student registered in the system.

    Search for Student: Allows the user to find and display the information of a single student by entering their ID.

    User-Friendly Menu: A simple, interactive menu that runs in a loop, making the application easy to use.

Core OOP Concepts Demonstrated

This project is built around two primary classes, showcasing several key OOP concepts:
1. Classes and Objects

    Student Class: Acts as a blueprint for creating individual student objects. Each object has its own attributes (name, student_id, courses).

    StudentManagementSystem Class: A blueprint for a single management object that contains and manages the Student objects.

    Objects: When you add a student like "Alice Nakato," you are creating an instance (an object) of the Student class. The sms variable in the main function is an instance of the StudentManagementSystem class.

2. Encapsulation

    The data (attributes like name and student_id) and the operations that can be performed on that data (methods like display_info) are bundled together within the Student class. The management system doesn't need to know the internal details of how a student is structured; it just interacts with the Student object through its methods.

3. Methods

    __init__ (Constructor): Used to initialize a new object's state (e.g., setting the name and ID when a new Student is created).

    Instance Methods: Functions defined inside a class that operate on an instance of that class (e.g., add_student, list_students, search_student, and display_info).

4. Polymorphism (A Potential Extension)

While not implemented in the base assignment, the project could easily be extended to demonstrate polymorphism. Polymorphism (from Greek, meaning "many forms") is the principle that different classes can be treated as a single, general type and respond to the same method call in their own unique ways.

For example, we could introduce a Teacher class. Both Student and Teacher are types of "people" in the university, and both might need a display_info() method.

class Teacher:
    """Represents a teacher with their own details."""
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject

    # Same method name, but different implementation
    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Subject:      {self.subject}")

# A single function can now handle a list of different object types
def display_directory(people):
    for person in people:
        # Python calls the correct display_info() for each object
        person.display_info()

In this example, the display_directory function is polymorphic. It can operate on a list containing both Student and Teacher objects without needing to know the specific type of each object. It simply calls the display_info() method, and each object knows how to display itself correctly.
How to Run

    Prerequisites: Ensure you have Python 3 installed on your system.

    Save the Code: Save the complete Python code in a file named student_system.py.

    Open Terminal: Open a terminal or command prompt.

    Navigate to Directory: Use the cd command to navigate to the folder where you saved the file.

    Execute the Script: Run the program using the following command:

    python student_system.py

    Follow the Menu: The program will display a menu with options. Enter a number (1-4) to perform an action.