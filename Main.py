import Menu
import StudentAdder
import PaymentAdder
import StudentViewer
import ReportViewer
import PopulateList
import ExitSystem
from FileHandler import ReadFile

def main():

    PopulateList.populatinglists()

    modified_Student_list = False
    modified_payment_list = False

    while True:
        Menu.show_main_menu()
        choice = input("Choice: ")

        try:
            if choice == "1":
                modified_Student_list = StudentAdder.new_student()
            elif choice == "2":
                modified_payment_list = PaymentAdder.record_new_payment()
            elif choice == "3":
                StudentViewer.view_student()
            elif choice == "4":
                ReportViewer.view_reports()
            elif choice == "0":
               ExitSystem.ExitProgram(modified_Student_list, modified_payment_list)
            else:
                print(" Invalid choice. Please enter a 'number' from 0-4 (inclusive)")

        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
