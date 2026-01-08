# payment.py
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
