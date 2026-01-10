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
        print()
    return

def view_specific_student():

   while True:
    try:
        student_id = int(input("Student ID: ")) #Checking if correct a number was entered

        #Converting into 3 digit format
        student_id = str(student_id)
        while len(student_id) < 3:
            student_id = "0" + student_id 
        break
    except:
        print("Please enter a valid number")

    for x in Studentlist:
        if x.student_id == student_id :
            x.view()
            return #returning since Student_ID is unique for each student and it has been found
    
    
    print("Student ID not found. Please check and enter again.") #Will run if student not found so program did not return
    
    return
    

    


