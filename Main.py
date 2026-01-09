import Menu
import StudentAdder
import PaymentRecorder
import StudentViewer
import ReportViewer
import ExitSystem

#from fee_manager import FeeManager

def main():
    #manager = FeeManager()

    while True:
        Menu.show_menu()
        choice = input("Choice: ")

        try:
            if choice == "1":
                StudentAdder.new_student()
            elif choice == "2":
                PaymentRecorder.record_payment()
            elif choice == "3":
                StudentViewer.view_student()
            elif choice == "4":
                ReportViewer.view_reports()
            elif choice == "0":
               ExitSystem.ExitProgram()
            else:
                print(" Invalid choice. Please enter a 'number' from 0-4 (inclusive)")

        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
