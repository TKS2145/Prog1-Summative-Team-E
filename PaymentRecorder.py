import Globals
from Classes import Payment

def record_payment():

    if Globals.StudentCount == 0: 
        print("There are no students to reocrd any payments. Please register at least one student.")
        return
    
    else:

        while True: #Loop used to check if student id exist or not
    
            breaking = False #Used to exit loop is student id exist
            student_id = input("Student ID: ")
            for x in Globals.Studentlist:
                if x.student_id == student_id :
                    breaking = True
                    break
            
            if breaking :
                break
            else:
                print("Student ID does not exist. Press 1 to continue and 0 to exist.")
                while True:
                    choice = input("Enter 1 to continue or any other key to cancel.")
                    if choice ==  1 :
                        break
                    else:
                        return
                    

            while True:
                try:
                    amount = float(input("Payment Amount: "))
                    break
                except:
                    print("Please enter payment account in digets (Decimal accepted")

            new_payment = Payment(student_id, amount)

        print("Payment recorded successfully")
        return