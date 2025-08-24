# The Student class serves as a blueprint for creating student objects.
# Each object created from this class will have its own name, id, and list of courses.
class Student:
    """Represents a single student with a name, ID, and a list of courses."""

    def __init__(self, name, student_id):
        """
        This is the constructor method. It runs when a new Student object is created.
        'self' refers to the specific instance of the object being created.
        """
        self.name = name
        self.student_id = student_id
        self.courses = []  # Starts as an empty list for each new student

    def display_info(self):
        """Prints the details of the student in a readable format."""
        print(f"Student Name: {self.name}")
        print(f"Student ID:   {self.student_id}")
        # self.courses.append("Introduction to Python")
        print(f"Courses:      {', '.join(self.courses) if self.courses else 'Not enrolled in any courses'}")

# The StudentManagementSystem class will manage all the Student objects.
# It holds a list of students and provides methods to interact with that list.
class StudentManagementSystem:
    """Manages a collection of Student objects."""

    def __init__(self):
        """Initializes the management system with an empty list of students."""
        self.students = [] # This list will store all the Student objects

    def add_student(self, name, student_id):
        """Creates a new Student object and adds it to the list."""
        # First, check if a student with this ID already exists to avoid duplicates.
        for student in self.students:
            if student.student_id == student_id:
                print(f"Error: Student with ID {student_id} already exists.")
                return # Exit the method if a duplicate is found

        # If no duplicate is found, create a new student and add them.
        new_student = Student(name, student_id)
        self.students.append(new_student)
        print(f"✅ Student '{name}' added successfully!")

    def list_students(self):
        """Displays information for all students in the system."""
        if not self.students:
            print("No students in the system yet.")
            return

        print("\n--- List of All Students ---")
        for student in self.students:
            student.display_info()
            print("----------------------------") # Separator for clarity

    def search_student(self, student_id):
        """Searches for a student by their ID and displays their info if found."""
        for student in self.students:
            if student.student_id == student_id:
                print("\n--- Student Found ---")
                student.display_info()
                return # Exit the method once the student is found

        # This line will only be reached if the loop completes without finding the student.
        print(f"❌ Student with ID '{student_id}' not found.")