# ReportViewer.py
from Globals import Studentlist

def view_reports():
    while True:
        print("""
  ---Reports Viewer---
1: View Fully Paid Students
2: View Partially Paid Students
3: View Unpaid Students
0: Cancel  """)
        choice = input("Enter choice: ")

        if choice == "0":
            print("Cancelling")
            return
        elif choice == "1":
            print("\n---Fully Paid Students---")
            display_students(lambda s: s.balance == 0) # Filter students with balance 0
        elif choice == "2":
            print("\n---Partially Paid Students---")
            display_students(lambda s: 0 < s.balance < s.total_fee) # Filter students with partial payments
        elif choice == "3":
            print("\n---Unpaid Students---")
            display_students(lambda s: s.balance == s.total_fee)  # Filter students with no payments
        else:
            print("Invalid input. Please enter again")

def display_students(condition):
    filtered = [s for s in Studentlist if condition(s)] # Create a list of students matching the condition
    if not filtered:
        print("No students found for this category.")  # If no students match, print a message and return
        return
    for s in filtered:
        s.view() # Call the view() method of the Student class to print details