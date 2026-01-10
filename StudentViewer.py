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
        
        if choice == "0":
            print("Cancelling")
            return
        elif choice == "1":
            print("\n ---Viewing all Students---")
            view_all_Student()
            return
        elif choice == "2":
            print("\n Viewing specific student")
            view_specific_student()
            return
        else:
            print("Invalid input. Please enter again")


 
def view_all_Student():
    for x in Studentlist:
        x.view()
    return

def view_specific_student():

    student_id = input("Student ID: ")
    for x in Studentlist:
        if x.student_id == student_id :
            x.view()
            return #returning since Student_ID is unique for each student and it has been found
    
    
    print("Student ID not found. Please check and enter again.") #Will run if student not found so program did not return
    
    return
    

    


