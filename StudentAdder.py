import Globals
from Classes import Student

def new_student():
    print("\nEnter details of student")
    name = input("Name: ")

    # Display available classes with fixed fees
    print("""
Choose Class:
1: Computer Science (Rs 5000)
2: Software Engineering (Rs 5000)
3: International Business Trade (Rs 4500)
4: Entrepreneurial Leadership (Rs 4200)
    """)

    while True:
        class_choice = input("Enter class number: ")

        # Validate class selection
        if class_choice in Globals.CLASS_FEES:
            class_name, total_fee = Globals.CLASS_FEES[class_choice]
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

    # Add student with fixed class fee
    add_student(name, class_name, total_fee)
    print("Student added successfully")


def add_student(name, class_name, total_fee):
    """
    Creates a new Student object and adds it to the global Studentlist
    """

    # Increment student count
    Globals.StudentCount += 1
    student_id = str(Globals.StudentCount)

    # Format student ID to 3 digits (e.g. 001, 002)
    while len(student_id) < 3:
        student_id = "0" + student_id

    # Create student object and store it
    Globals.Studentlist.append(
        Student(student_id, name, class_name, total_fee)
    )
