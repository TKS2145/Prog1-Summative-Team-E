#Student Class

class Student:
    def __init__(self, student_id, name, class_name, total_fee,):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.total_fee = float(total_fee)
        self.amount_paid = 0.0
        self.balance = self.total_fee - self.amount_paid
        self.payment_history = []  # list of payment amounts

    # Add a payment to the student
    def add_payment(self, amount):
        self.amount_paid += amount
        self.calculate_balance()
        self.payment_history.append(amount)

    # Calculate balance remaining
    def calculate_balance(self):
        self.balance = self.total_fee - self.amount_paid

    # Convert to dictionary for saving
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "class_name": self.class_name,
            "total_fee": self.total_fee,
            "amount_paid": self.amount_paid,
            "balance": self.balance,
            "payment_history": self.payment_history
        }

    def view(self):
            print(f"ID: {self.student_id}")
            print(f"Name: {self.name}")
            print(f"Class: {self.class_name}")
            print(f"Total Fee: {self.total_fee}")
            print(f"Paid: {self.amount_paid}")
            print(f"Balance: {self.balance}")


# payment class
from datetime import datetime

class Payment:
    def __init__(self, student_id, amount):
        self.student_id = student_id
        self.amount = float(amount)
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "amount": self.amount,
            "date": self.date
        }
