import Globals
from Classes import Payment

def record_new_payment():
    
    if Globals.StudentCount == 0: 
        print("There are no students to record any payments. Please register at least one student.")
        return
    
    else:

        while True: #Loop used to check if student id exist or not
    
            breaking = False #Used to exit loop is student id exist
            
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

            if int(student_id) > Globals.StudentCount: #Checking if ID entered exist. Since student id is automatically incremented, it cannot be greater than current  student count
              
                print("Student ID does not exist.")
                while True:
                    choice = input("Enter 1 to continue or any other key to cancel.")
                    if choice ==  "1" :
                        break
                    else:
                        return
                continue
            else:

                break #If not greater, program continues

        while True: #Looping to enter correct value amount
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
                print("Please enter payment account in digits (Decimal accepted")

        add_payment(student_id, amount)

        print("\nPayment recorded successfully")

        return
    

def add_payment(student_id, amount):

    index = int(student_id) -1 #Since student id is incremented before adding new student, index of student is 1 less than student id

    new_payment = Payment(student_id, amount)
    Globals.PaymentList.append(new_payment)
    Globals.Studentlist[index].add_payment(amount)

    return True
