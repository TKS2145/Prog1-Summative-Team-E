#Student Class

class Student:
    def __init__(self, student_id, name, class_name, total_fee, amount_paid):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.total_fee = float(total_fee)
        self.amount_paid = amount_paid
        self.balance = self.total_fee - self.amount_paid
    #    self.payment_history = []  # list of payments 


    # Add a payment to the student
    def add_payment(self, amount):
        self.amount_paid += amount
        self.balance = self.total_fee - self.amount_paid # Calculate balance remaining
    #    self.payment_history.append(payment)
        

    # Convert to dictionary for saving
    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Class Name": self.class_name,
            "Total Fee": self.total_fee,
            "Amount Paid": self.amount_paid,
            "Balance left": self.balance,
        #    "Payment History": self.payment_history
        }

    def view(self):
            print(f"ID: {self.student_id}")
            print(f"Name: {self.name}")
            print(f"Class: {self.class_name}")
            print(f"Total Fee: {self.total_fee}")
            print(f"Paid: {self.amount_paid}")
            print(f"Balance left: {self.balance}")


# payment class
from datetime import datetime

class Payment:
    def __init__(self, student_id, amount):
        self.student_id = student_id
        self.amount = float(amount) #hardcoding it as float just to make sure
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "amount": self.amount,
            "date": self.date
        }
