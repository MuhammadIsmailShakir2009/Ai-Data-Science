def srms_list():
    records = []
    while True:
        print("\n--- SRMS using Nested List ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Sort Records")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            records.append([name, roll, subject, marks])

        elif choice == "2":
            for r in records:
                print(r)

        elif choice == "3":
            roll = input("Enter roll number: ")
            for r in records:
                if r[1] == roll:
                    print(r)

        elif choice == "4":
            roll = input("Enter roll number: ")
            for r in records:
                if r[1] == roll:
                    r[3] = int(input("Enter new marks: "))

        elif choice == "5":
            roll = input("Enter roll number: ")
            for r in records:
                if r[1] == roll:
                    records.remove(r)

        elif choice == "6":
            records.sort(key=lambda x: x[3], reverse=True)

        elif choice == "7":
            break


def srms_dict():
    records = []
    while True:
        print("\n--- SRMS using List of Dictionaries ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Sort Records")
        print("7. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            student = {
                "name": input("Enter name: "),
                "roll": input("Enter roll number: "),
                "subject": input("Enter subject: "),
                "marks": int(input("Enter marks: "))
            }
            records.append(student)

        elif choice == "2":
            for r in records:
                print(r)

        elif choice == "3":
            roll = input("Enter roll number: ")
            for r in records:
                if r["roll"] == roll:
                    print(r)

        elif choice == "4":
            roll = input("Enter roll number: ")
            for r in records:
                if r["roll"] == roll:
                    r["marks"] = int(input("Enter new marks: "))

        elif choice == "5":
            roll = input("Enter roll number: ")
            for r in records:
                if r["roll"] == roll:
                    records.remove(r)

        elif choice == "6":
            records.sort(key=lambda x: x["marks"], reverse=True)

        elif choice == "7":
            break


while True:
    print("\n=== Main Menu ===")
    print("1. SRMS using Nested List")
    print("2. SRMS using List of Dictionaries")
    print("3. Exit")

    main_choice = input("Enter choice: ")

    if main_choice == "1":
        srms_list()
    elif main_choice == "2":
        srms_dict()
    elif main_choice == "3":
        break
