
#---------------
#  Validate
#---------------

def validate_data(message, types=str, condition=None, error="Value Error", enter_okay=False):
    okay= False

    while not okay:
        try:
            entry = input(message)
            entry = entry.replace(",", ".")

            if enter_okay and entry.strip() == "":
                return None
            
            info = types(entry)

            if condition and not condition(info):
                print(error)
                continue
            
            okay = True
            return info
        
        except ValueError:
            print("That value is incorrect")

#---------------
#   ADD DATE 1
#---------------

def add_student(data, id_student, name, last_name, age, ratings, course, statu):
    if age >= 0:
        student = {
            "id_student": id_student,
            "name": name,
            "last name": last_name,
            "age": age,
            "ratings": ratings,
            "course": course,
            "statu": statu
        }
        data.append(student)
        print("Student add corretly.")
        return


#--------------
# Wath list 2
#--------------

def wathing_list(data):

    if not data:
        print("There are NO students")
        return

    print("\n----LIST STUDENTS----\n")
    for i in data:
        print(f"\nID:", i['id_student'])
        print(f"Names:", i['name'].lower())
        print(f"Last name:", i['last name'].lower())
        print(f"Age:", i['age'])
        print(f"ratings:{i['ratings']:.2f}")
        print(f"Program:", i['course'].lower())
        print(f"statu:", i['statu'].lower())

#--------------
# Search 3
#-------------

def looking_for(data, seek):

    if not data:
        print("There are NO students")
        return

    for i in data:
        if i["id_student"] == seek:
            print("Student Found: ")
            print(f"\nID:", i['id_student'])
            print(f"Names:", i['name'].lower())
            print(f"Last name:", i['last name'].lower())
            print(f"Age:", i['age'])
            print(f"ratings:{i['ratings']:.2f}")
            print(f"Program:", i['course'].lower())
            print(f"statu:", i['statu'].lower())
            return i
        
    print("This student no exit")
    return None
        

#-------------
# Update 4
#-------------

def update_value(data, change, new_age, new_ratings, new_course, new_statu):
    if not data:
        print("There are NO students")
        return

    for i in data:

        if change == i["id_student"]:

            if new_age is not None:
                i["age"] = new_age

            if new_ratings is not None:
                i["ratings"]

            if new_course is not None:
                i["course"]
            
            if new_statu is not None:
                i["statu"]
            
            print("--Updated--")
            print(f"\nID:", i['id_student'])
            print(f"Names:", i['name'].lower())
            print(f"Last name:", i['last name'].lower())
            print(f"Age:", i['age'])
            print(f"ratings:{i['ratings']:.2f}")
            print(f"Program:", i['course'].lower())
            print(f"statu:", i['statu'].lower())
            return
    
    return
    print("No found Student")
    return    


#------------
#  Delete 5
#------------

def delete_student(data, delete):
    if not data:
        print("There are NO students")
        return
    
    for i in data:
        if i["id_student"] == delete:
            print("Student Found: ")
            print(f"\nID:", i['id_student'])
            print(f"Names:", i['name'].lower())
            print(f"Last name:", i['last name'].lower())
            print(f"Age:", i['age'])
            print(f"ratings:{i['ratings']:.2f}")
            print(f"Program:", i['course'].lower())
            print(f"statu:", i['statu'].lower())

            confirm = validate_data("Are you sure you want to delete this student? (y/n): ", str, lambda x: x.lower() in ["y", "n"])

            if confirm == "y":
                data.remove(i)
                print("The student was deleted from the database.")
                return

            elif confirm == "n":
                print("Canceled")
                return
    
    print("The student was not found")
    return None


    


