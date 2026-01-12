import Globals
from Classes import Student

def new_student():
    print("\nEnter details of student")
    name = input("Name: ")

    # Display available classes with fixed fees
    print("""
Choose Class:
1: Computer Science ($ 5000)
2: Software Engineering ($ 5000)
3: International Business Trade ($ 4500)
4: Entrepreneurial Leadership ($ 4200)
    """)

    Class_Fees = {
    "1": ("Computer Science", 5000),
    "2": ("Software Engineering", 5000),
    "3": ("International Business Trade", 4500),
    "4": ("Entrepreneurial Leadership", 4200)
}



    while True:
        class_choice = input("Enter class number: ")

        # Validate class selection
        if class_choice in Class_Fees:
            class_name, total_fee = Class_Fees[class_choice]
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

    # Add student with fixed class fee
    add_student(name, class_name, total_fee)
    print("Student added successfully")

    add_student(name, class_name, total_fee)
    print("\nStudent added successfully")
    return True

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
