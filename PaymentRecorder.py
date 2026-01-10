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

            if int(student_id) > Globals.StudentCount:
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
                    if amount <= 0:
                        print("Payment must be greater than zero")
                        choice = input("Enter 0 to cancel: ")
                        if choice == 0:
                            return
                        else:
                            continue
                    break
                except:
                    print("Please enter payment account in digets (Decimal accepted")

            index = int(student_id) -1 #Since student id is incremented before adding new student, index of student is 1 less than student id
 
            new_payment = Payment(student_id, amount)
            Globals.PaymentList.append(new_payment)
            Globals.Studentlist[index].add_payment(amount, new_payment)


        print("Payment recorded successfully")
        return