from Globals import Studentlist

def view_student():

    #Menu to be presented
     
    while True:

        print("""
        ---Student Viewer---
        1: View all student records
        2: View only a specific student's record
        0: Cancel          
              """)
    
        choice = input("Enter choice: ")
        
        if choice == 0:
            return
        elif choice == 1:
            view_all_Student()
            return
        elif choice == 2:
            view_specific_student()
            return



 
def view_all_Student():
    for x in Studentlist:
        x.view()

def view_specific_student():

    student_id = input("Student ID: ")
    found = False
    for x in Studentlist:
        if x.student_id == student_id :
            x.view()
            found = True
    
    if not found:
        print("Student ID not found. Please check and enter again.")
        return
    else:
        return
    

    


