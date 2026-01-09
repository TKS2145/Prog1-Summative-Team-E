def view_reports(manager):
    print("Fully Paid:", len(manager.get_fully_paid_students()))
    print("Partially Paid:", len(manager.get_partially_paid_students()))
    print("Unpaid:", len(manager.get_unpaid_students()))
