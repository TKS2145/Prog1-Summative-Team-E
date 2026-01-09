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