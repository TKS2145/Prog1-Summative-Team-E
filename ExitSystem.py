import sys
import FileHandler


def ExitProgram(ModifiedStudentList, ModifiedPaymentList): 

        if ModifiedStudentList:
                print("\nSaving new data into Student Record")
                FileHandler.WriteFile("StudentRecords.json") #

        if ModifiedPaymentList:
                print("\nSaving new data into PaymentRecords")
                FileHandler.AppendFile("PaymentRecords.json") #Appending to the PaymentRecord

        print("Saving done")
        print("Exiting now")
        sys.exit(0)