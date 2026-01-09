import Globals

def record_payment():

    if Globals.StudentCount == 0: 
       print("There are no students to reocrd any payments. Please register at least one student.")
    
    else:

        student_id = input("Student ID: ")
        amount = float(input("Payment Amount: "))

        print("Payment recorded successfully")