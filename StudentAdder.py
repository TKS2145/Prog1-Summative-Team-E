def add_student(manager):
    student_id = input("Student ID: ")
    name = input("Name: ")
    class_name = input("Class: ")
    total_fee = float(input("Total Fee: "))
    manager.add_student(student_id, name, class_name, total_fee)
    print(" Student added successfully")
