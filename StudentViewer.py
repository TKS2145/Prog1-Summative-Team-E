from Globals import Studentlist

def view_student(manager):

    #Menu to be presented
    view_all_Student()



 
def view_all_Student():
    for x in Studentlist:
        print(x)

def view_specific_student():

    student_id = input("Student ID: ")
    for x in Studentlist:
        if x.student_id == student_id :
             print(f"ID: {x.student_id}")
             print(f"Name: {x.name}")
             print(f"Class: {x.class_name}")
             print(f"Total Fee: {x.total_fee}")
             print(f"Paid: {x.amount_paid}")
             print(f"Balance: {x.balance}")

