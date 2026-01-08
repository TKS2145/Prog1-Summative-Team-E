# menu.py
from fee_manager import FeeManager

def show_menu():
    print("\n--- School Fee Payment System ---")
    print("1. Add Student")
    print("2. Record Payment")
    print("3. View Student Details")
    print("4. View Reports")
    print("0. Exit")

def add_student(manager):
    student_id = input("Student ID: ")
    name = input("Name: ")
    class_name = input("Class: ")
    total_fee = float(input("Total Fee: "))
    manager.add_student(student_id, name, class_name, total_fee)
    print(" Student added successfully")

def record_payment(manager):
    student_id = input("Student ID: ")
    amount = float(input("Payment Amount: "))
    manager.record_payment(student_id, amount)
    print("Payment recorded successfully")

def view_student(manager):
    student_id = input("Student ID: ")
    student = manager.find_student(student_id)
    if student:
        print(f"ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Class: {student.class_name}")
        print(f"Total Fee: {student.total_fee}")
        print(f"Paid: {student.amount_paid}")
        print(f"Balance: {student.balance}")
    else:
        print(" Student not found")

def view_reports(manager):
    print("Fully Paid:", len(manager.get_fully_paid_students()))
    print("Partially Paid:", len(manager.get_partially_paid_students()))
    print("Unpaid:", len(manager.get_unpaid_students()))

def main():
    manager = FeeManager()

    while True:
        show_menu()
        choice = input("Choice: ")
        try:
            if choice == "1":
                add_student(manager)
            elif choice == "2":
                record_payment(manager)
            elif choice == "3":
                view_student(manager)
            elif choice == "4":
                view_reports(manager)
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
