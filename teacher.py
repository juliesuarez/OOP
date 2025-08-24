#  illustrates polymorphism (duck typing) by defining a function that works with both Student and Teacher objects.

from student_oop import Student

class Teacher:
    """Represents a single teacher with a name, ID, and a subject."""

    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}")
        print(f"Teacher ID:   {self.teacher_id}")
        print(f"Subject:      {self.subject}")

def display_directory(people):
    """
    Prints information for a list of people (students or teachers).
    This function demonstrates polymorphism (duck typing).
    """
    print("\n--- University Directory ---")
    for person in people:
        person.display_info() # This works on both Student and Teacher objects!
        print("--------------------------")

student1 = Student("Alice Nakato", "S001")
teacher1 = Teacher("Dr. Okello", "T01", "Computer Science")

# Create a list containing different types of objects
directory_list = [student1, teacher1]

# Call our polymorphic function
display_directory(directory_list)