import os

# Nombre del archivo - Name File
archivo_db = "database.txt"

# -----------------------------
# CREATE (Append - agregar datos)
# -----------------------------
def agregar_blocker():
    blocker = input("Enter your daily blocker: ")

    # Modo "a" = append (agrega sin borrar lo anterior)
    with open(archivo_db, "a", encoding="utf-8") as archivo:
        archivo.write(blocker + "\n")

    print("Blocker saved successfully.\n")


# -----------------------------
# READ (Fetch - leer datos)
# -----------------------------
def mostrar_blockers():
    # Verificar si el archivo existe
    if os.path.exists(archivo_db):
        with open(archivo_db, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            if len(lineas) == 0:
                print("No blockers found.\n")
            else:
                print("\n--- Team Daily Blockers ---")
                for linea in lineas:
                    print("- " + linea.strip())
                print()
    else:
        print("Error: database file does not exist.\n")


# -----------------------------
# WARNING (Overwrite protección)
# -----------------------------
def sobrescribir_archivo():
    if os.path.exists(archivo_db):
        confirmacion = input("Warning: This will overwrite the file. Continue? (yes/no): ")

        if confirmacion.lower() == "yes":
            with open(archivo_db, "w", encoding="utf-8") as archivo:
                archivo.write("")  # borra todo (bendito codigo)
            print("File overwritten.\n")
        else:
            print("Operation cancelled.\n")
    else:
        print("File does not exist.\n")


# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def menu():
    valid = False
    while not valid:
        print("=== Team Daily Status ===")
        print("1. Add blocker")
        print("2. Fetch blockers")
        print("3. Overwrite file")
        print("4. Exit")

        opcion = input("Choose an option: ")

        if opcion == "1":
            agregar_blocker()
        elif opcion == "2":
            mostrar_blockers()
        elif opcion == "3":
            sobrescribir_archivo()
        elif opcion == "4":
            print("Goodbye!")
            valid = True
        else:
            print("Invalid option.\n")


# Ejecutar programa - Loop
menu()


# ==========================================================
# ENGLISH TASK (COMMENTS)
# ==========================================================

"""
Protocol Selection (3-C Rule):

1. I will reach out to the team via Slack because the issue is an immediate blocker that requires quick attention.
2. I would use Email if the problem needs detailed explanation and documentation.
3. I would report the issue in Jira to properly track the bug and ensure it is resolved systematically.


Vocabulary Integration:

This script demonstrates Persistence by saving user input into a text file so data remains available after execution. 
It allows the user to Fetch stored blockers by reading the file contents and displaying them. 
The program includes a warning before performing an Overwrite operation to prevent accidental data loss. 
If any issue occurs, I would Reach out to the team using the appropriate communication channel.
"""