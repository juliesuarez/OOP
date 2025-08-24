# This is the main part of the program that the user interacts with.
from student_oop import StudentManagementSystem
def main():
    """Runs the main user interface for the student management system."""
    # Create an instance of our management system
    sms = StudentManagementSystem()

    # Add a few sample students to start with
    sms.add_student("Alice Nakato", "S001")
    sms.add_student("Bob Mwesigwa", "S002")
    print("\nWelcome to the Student Management System!")

    # This loop keeps the program running until the user chooses to exit.
    while True:
        print("\nPlease choose an option:")
        print("1. Add a new Student")
        print("2. List all Students")
        print("3. Search for a Student by ID")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID (e.g., S003): ")
            sms.add_student(name, student_id)

        elif choice == '2':
            sms.list_students()

        elif choice == '3':
            student_id = input("Enter the Student ID to search for: ")
            sms.search_student(student_id)

        elif choice == '4':
            print("Thank you for using the system. Goodbye! ")
            break # Exits the while loop, ending the program

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# This standard Python construct ensures the main() function is called
# only when this script is executed directly.
if __name__ == "__main__":
    main()