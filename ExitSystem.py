import sys
import FileHandler
from Globals import ModifiedStudentList
from Globals import ModifiedPaymentList


def ExitProgram():

        if ModifiedStudentList:
                print("Saving new data into Student Record")
                FileHandler.WriteFile("StudentRecords") #

        if ModifiedPaymentList:
                print("\nSaving new data into PaymentRecords")
                FileHandler.AppendFile("PaymentRecords.py")

        print("Saving done")
        print("Exiting now")
        sys.exit(0)