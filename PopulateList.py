from FileHandler import ReadFile
from StudentAdder import add_student
from PaymentAdder import add_payment

def populatinglists():

    DictListStudent = ReadFile("StudentRecords.json") #List of the dictionaries holding student data
    DictListPayment = ReadFile("PaymentRecords.json") #List of the dictionaries holding the payment data

    if DictListStudent != None:

        for x in DictListStudent:

            add_student(x["Name"], x["Class Name"], x["Total Fee"],x["Student ID"] ) 

    if DictListPayment != None:
        for y in DictListPayment:

            add_payment(y["student_id"],y["amount"], y["date"])

    
