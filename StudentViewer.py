from Globals import Studentlist

def view_student():

    #Menu to be presented
    view_all_Student()



 
def view_all_Student():
    for x in Studentlist:
        x.view()

def view_specific_student():

    student_id = input("Student ID: ")
    for x in Studentlist:
        if x.student_id == student_id :
            x.view()
            

