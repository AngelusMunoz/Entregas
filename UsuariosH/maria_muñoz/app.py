from system import validate_data, add_student, wathing_list, looking_for, update_value, delete_student

print("=" * 40)
print(" " * 12, "Data Base")
print("=" * 40)

data = []

option = ""

while option != 6:

    print("\n--Welcome to the system of data Studens--\n")
    print("Options:")
    print("1. Add Student")
    print("2. Show List")
    print("3. Search student")
    print("4. Update Data")
    print("5. Delete Student")
    print("6. Exit\n")

    option = validate_data("What do you want to do? (1-6): ", int, lambda x: x in [1,2,3,4,5,6])

    if option == 1:

        print("=" * 40)
        print("You selected: Add Student\n")
        id_student = validate_data("ID: ", int, lambda x: x > 0)
        name = validate_data("Names: ", str, lambda x: x.strip() != "")
        last_name = validate_data("Last Name: ", str, lambda x: x.strip() != "")
        age = validate_data("Age: ", int, lambda x: x >= 7)
        ratings = validate_data("Final Grade: ", float, lambda x: x > 0)
        course = validate_data("Curse: ", str, lambda x: x != "")
        statu = validate_data("Status (write: active or inactive): ", str, lambda x: x.lower() in ["active", "inactive"])

        add_student(data, id_student, name, last_name, age, ratings, course, statu)

    elif option == 2:
        print("You selected: Show List\n")
        wathing_list(data)

    elif option == 3:
        print("You selected: Search Student\n")
        seek = validate_data("Write the ID student: ", int, lambda x: x != "")
        looking_for(data, seek)

    elif option == 4:
        print("You selected: Update Data\n")
        print("Starting update..\n")
        change = validate_data("Write the ID student: ", int, lambda x: x > 0)

        print("---UPDATING---")
        
        new_age = validate_data("Age (Enter pass): ", int, lambda x: x > 7, enter_okay=True)
        new_ratings = validate_data("Rating (Enter pass): ", int, lambda x: x > 7, enter_okay=True)
        new_course =  validate_data("Program (Enter pass): ", str, lambda x: x.strip(), enter_okay=True)
        new_statu =  validate_data("Statu (Enter pass): ", str, lambda x: x.lower() in ["active", "inactive"], enter_okay=True)

        update_value(data, change, new_age, new_ratings, new_course, new_statu)
        
    elif option == 5:
        print("You selected: Delete Student\n")

        delete = validate_data("Write the ID student: ", int, lambda x: x > 0)

        delete_student(data, delete)

print("Exiting the system...")



        



