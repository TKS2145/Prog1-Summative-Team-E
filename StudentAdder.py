import Globals
from Classes import Student
from Menu import show_class

def new_student():
    print("\nEnter details of student")
    name = input("Name: ")

    Class_Fees = {
    "1": ("Computer Science ", 50000),
    "2": ("Software Engineering ", 50000),
    "3": ("International Business Trade ", 45000),
    "4": ("Entrepreneurial Leadership ", 42000)
}


    while True:

        show_class() #Displays available classes with fixed prices
        class_choice = input("Enter class number: ")

        # Validate class selection
        if class_choice in Class_Fees:
            class_name, total_fee = Class_Fees[class_choice]
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

    # Add student with fixed class fee
    add_student(name, class_name, total_fee)
    print("\nStudent added successfully")
    return True

def add_student(name, class_name, total_fee, student_id = "0"):
    """
    Creates a new Student object and adds it to the global Studentlist
    """

    # Increment student count
    Globals.StudentCount += 1

    #Checks if student id already exist and creates a new one if it does not exist
    if student_id == "0":

        student_id = str(Globals.StudentCount)

        # Format student ID to 3 digits (e.g. 001, 002)
        while len(student_id) < 3:
            student_id = "0" + student_id

    # Create student object and store it
    Globals.Studentlist.append(
        Student(student_id, name, class_name, total_fee)
    )
