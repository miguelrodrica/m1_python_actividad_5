from colorama import init, Fore, Back, Style
init()

def main_menu():
    while True:
        print(Fore.MAGENTA + "\n-- MENÚ ACADÉMICO --" + Style.RESET_ALL)
        print("1. Gestión de estudiantes")
        print("2. Gestión de materias")
        print("3. Asignaciones")
        print("4. Notas y calificaciones")
        print("5. Reportes y estadísticas")
        print("6. Salir")
        try:
            main_choice = int(input("\nEscriba el número de la opción seleccionada: "))
            if main_choice <= 0 or main_choice > 6:
                print(Fore.RED + "\n¡ERROR!. Número no contemplado en la lista." + Style.RESET_ALL)
            else:
                return main_choice
        except ValueError:
            print(Fore.RED + "\n¡ERROR!. Debe ingresar un número entero." + Style.RESET_ALL)

def students_menu():
    while True:
        print(Fore.MAGENTA + "\n-- GESTIÓN ESTUDIANTES --" + Style.RESET_ALL)
        print("1. Registrar estudiantes")
        print("2. Listar estudiantes")
        print("3. Consultar estudiante con ID")
        print("4. Eliminar estudiante")
        print("5. Atrás")
        try:
            students_choice = int(input("\nEscriba el número de la opción seleccionada: "))
            if students_choice <= 0 or students_choice > 5:
                print(Fore.RED + "\n¡ERROR!. Número no contemplado en la lista." + Style.RESET_ALL)
            else:
                return students_choice
        except ValueError:
            print(Fore.RED + "\n¡ERROR!. Debe ingresar un número entero." + Style.RESET_ALL)

def add_students():
    while True:
        try:
            qty_students = int(input("\n¿Cuántos estudiantes desea ingresar?: "))
            if qty_students <= 0:
                print(Fore.RED + "\n¡ERROR!. Ingrese un número positivo y diferente a 0." + Style.RESET_ALL)
                continue
            else:
                for i in range(qty_students):
                    student = {}
                    print(Fore.CYAN + f"\nEstudiante #{i+1}" + Style.RESET_ALL)
                    name_student = input("Nombre: ").lower()
                    student["name"] = name_student
                    while True:
                        try:
                            age_student = int(input("Edad: "))
                            if age_student <= 0:
                                print(Fore.RED + "¡ERROR!. La edad debe ser mayor a 0." + Style.RESET_ALL)
                                continue
                            else:
                                student["age"] = age_student
                            break
                        except ValueError:
                            print(Fore.RED + "¡ERROR!. La edad debe ser un número." + Style.RESET_ALL)
                    id_student = input("ID: ").lower()
                    student["id"] = id_student
                    return student
            break
        except ValueError:
            print(Fore.RED + "\n¡ERROR! Debe ingresar un número entero." + Style.RESET_ALL)

def show_students(students):
    if len(students) == 0:
        print(Fore.YELLOW + "\n¡VACÍO! Aún no se registra ningún estudiante." + Style.RESET_ALL)
    else:
        print("")
        for student in students:
            print(Fore.GREEN + f"Nombre: {student["name"]} | Edad: {student["age"]} | ID: {student["id"]}" + Style.RESET_ALL)

def search_student(students):
    found = True
    while found:
        id_consult = input("\nEscriba el ID del estudiante a consultar: ")
        for student in students:
            if student["id"] == id_consult:
                print(Fore.GREEN + f"\nNombre: {student["name"]} | Edad: {student["age"]} | ID: {student["id"]}" + Style.RESET_ALL)
                break
        found = False
        if student["id"] != id_consult:
            print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)
            found = True

def delete_student(students):
    repeat = True
    while repeat:
        try:
            delete_student_id = int(input("\nEscriba el ID del estudiante a eliminar: "))
            for student in students:
                if delete_student_id == student["id"]:
                    students.remove(student)
                    print(Fore.GREEN + f"\nSe eliminó al estudiante '{student["name"]}' de la base de datos" + Style.RESET_ALL)
                    repeat = False
                    break
                elif delete_student_id != student["id"]:
                    validate = False
            if validate == False:
                print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.RED + "\n¡ERROR! Debe ingresar un número entero." + Style.RESET_ALL)