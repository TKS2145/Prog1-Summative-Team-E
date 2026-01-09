def record_payment(manager):
    student_id = input("Student ID: ")
    amount = float(input("Payment Amount: "))
    manager.record_payment(student_id, amount)
    print("Payment recorded successfully")