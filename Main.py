import Menu
import StudentAdder
import PaymentRecorder
import StudentViewer
import ReportViewer

#from fee_manager import FeeManager

def main():
    #manager = FeeManager()

    while True:
        Menu.show_menu()
        choice = input("Choice: ")

        try:
            if choice == "1":
                StudentAdder.add_student(manager)
            elif choice == "2":
                PaymentRecorder.record_payment(manager)
            elif choice == "3":
                StudentViewer.view_student(manager)
            elif choice == "4":
                ReportViewer.view_reports(manager)
            elif choice == "0":
                manager.save_data_to_file()
                print(" Data saved. Exiting system.")
                break
            else:
                print(" Invalid choice")
        except ValueError as e:
            print(" Input error:", e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
