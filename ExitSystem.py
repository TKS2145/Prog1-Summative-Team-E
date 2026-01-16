import sys
import FileHandler
import Globals


def ExitProgram(ModifiedStudentList, ModifiedPaymentList): 

        if ModifiedStudentList:
                print("\nSaving new data into Student Record")
                FileHandler.WriteFile("StudentRecords.json", Globals.Studentlist) #
                print("\nSaving done")
                
        if ModifiedPaymentList:
                print("\nSaving new data into PaymentRecords")
                FileHandler.WriteFile("PaymentRecords.json", Globals.PaymentList) #Appending to the PaymentRecord
                print("\nSaving done")
        
        print("Exiting now")
        sys.exit(0)