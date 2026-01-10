import Globals
from Classes import Student

def new_student():

    print("Enter details of student")
    name = input("Name: ")
    class_name = input("Class: ")
    while True:

        try:
            total_fee = float(input("Total Fee: "))
            break
        except:
            print("Please only enter digits, decimal numbers accepted.")

    add_student(name, class_name, total_fee) #Since total fee should be fixed for classes, should I add a Class class for each class
    print("\nStudent added successfully")
    return True

def add_student(name, class_name, total_fee):

    #increments studentcount to know the number of students available
    Globals.StudentCount += 1
    student_id = str(Globals.StudentCount) #Generates student ID from Student Count

    #formats student_id into a 3 digit string
    while len(student_id) < 3:
        student_id = "0" + student_id

    Globals.Studentlist.append(Student(student_id, name, class_name, total_fee,))
