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
    while True:
            delete_student_id = (input("\nEscriba el ID del estudiante a eliminar: "))
            found = False
            for student in students:
                if delete_student_id == student["id"]:
                    students.remove(student)
                    print(Fore.GREEN + f"\nSe eliminó al estudiante '{student['name']}' de la base de datos" + Style.RESET_ALL)
                    found = True
                    break
            if found == True:
                break
            print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)

def subjects_menu():
    while True:
        print(Fore.MAGENTA + "\n-- GESTIÓN MATERIAS --" + Style.RESET_ALL)
        print("1. Registrar materias")
        print("2. Listar materias")
        print("3. Consultar materia por código")
        print("4. Eliminar materia")
        print("5. Atrás")
        try:
            subjects_choice = int(input("\nEscriba el número de la opción seleccionada: "))
            if subjects_choice <= 0 or subjects_choice > 5:
                print(Fore.RED + "\n¡ERROR!. Número no contemplado en la lista." + Style.RESET_ALL)
            else:
                return subjects_choice
        except ValueError:
            print(Fore.RED + "\n¡ERROR!. Debe ingresar un número entero." + Style.RESET_ALL)

def add_subject():
    while True:
        try:
            qty_subjects = int(input("\n¿Cuántas materias desea ingresar?: "))
            if qty_subjects <= 0:
                print(Fore.RED + "\n¡ERROR!. Ingrese un número positivo y diferente a 0." + Style.RESET_ALL)
            else:
                for i in range(qty_subjects):
                    subject = {}
                    print("")
                    print(Fore.CYAN + f"Materia #{i+1}" + Style.RESET_ALL)
                    name_subject = input("Nombre: ").lower()
                    subject["name_subject"] = name_subject
                    code_subject = input("Código: ").lower()
                    subject["code"] = code_subject
                    return subject
            break
        except ValueError:
            print(Fore.RED + "\n¡ERROR!. Debe ingresar un número entero." + Style.RESET_ALL)
def show_subjects(subjects):
    if len(subjects) == 0:
        print(Fore.YELLOW + "¡VACÍO! Aún no se registra ninguna materia." + Style.RESET_ALL)
    else:
        print("")
        for subject in subjects:
            print(Fore.GREEN + f"Nombre: {subject["name_subject"]} | Código: {subject["code"]}" + Style.RESET_ALL)

def search_subject(subjects):
    found = True
    while found:
        code_consult = input("\nEscriba el código de la materia a consultar: ")
        for subject in subjects:
            if subject["code"] == code_consult:
                print(Fore.GREEN + f"\nNombre: {subject["name_subject"]} | Código: {subject["code"]}" + Style.RESET_ALL)
                break
        found = False
        if subject["code"] != code_consult:
            print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)
            found = True

def delete_subjects(subjects):
    while True:
            delete_subjects_code = (input("\nEscriba el código de la materia a eliminar: "))
            found = False
            for subject in subjects:
                if delete_subjects_code == subject["code"]:
                    subjects.remove(subject)
                    print(Fore.GREEN + f"\nSe eliminó la materia '{subject['name_subject']}' de la base de datos" + Style.RESET_ALL)
                    found = True
                    break
            if found == True:
                break
            print(Fore.RED + "\n¡ERROR! El código es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)

def assigments_menu():
    while True:
            print(Fore.MAGENTA + "\n-- ASIGNACIONES --" + Style.RESET_ALL)
            print("1. Asignar materia a estudiante")
            print("2. Ver materias de un estudiante")
            print("3. Ver estudiantes por materia")
            print("4. Quitar materia a un estudiante")
            print("5. Atrás")
            try:
                assigments_choice = int(input("\nEscriba el número de la opción seleccionada: "))
                if assigments_choice <= 0 or assigments_choice > 5:
                    print(Fore.RED + "\n¡ERROR!. Número no contemplado en la lista." + Style.RESET_ALL)
                else:
                    return assigments_choice
            except ValueError:
                print("¡ERROR!. Debe ingresar un número entero.")

def assign_subject_to_student(students,subjects):
    assignment = {}
    validate_id = False
    validate_code = False
    while True:
        id_student = input("\nIngrese el documento del estudiante: ").lower()
        for student in students:
            if student["id"] == id_student:
                validate_id = True
                break
            elif student["id"] != id_student:
                validate_id = False
        if validate_id == True:
            assignment["id_student"] = id_student
            break
        else:
            print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)
    while True:
        try:
            qty_subjects = int(input("\n¿Cuántas materias desea ingresar?: "))
            if qty_subjects <= 0:
                print(Fore.RED + "\n¡ERROR!. Ingrese un número positivo y diferente a 0." + Style.RESET_ALL)
                continue
            else:
                print("")
                for i in range(qty_subjects):
                    while True:
                        code_subject = input(f"Código materia #{i+1}: ").lower()
                        for subject in subjects:
                            if subject["code"] == code_subject:
                                validate_code = True
                                break
                            elif subject["code"] != code_subject:
                                validate_code = False
                        if validate_code == True:
                            assignment[f"code_subject{i+1}"] = code_subject
                            break
                        else:
                            print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo" + Style.RESET_ALL)
            break
        except ValueError:
            print(Fore.RED + "\n¡ERROR!. Debe ingresar un número entero." + Style.RESET_ALL)
    print(Fore.GREEN + f"\nSe hizo la asignación exitosamente." + Style.RESET_ALL)
    return assignment

def show_student_subjects(students, subjects, assigments): #Esta función me la dió ChatGPT, porque después de muchos intentos no supe como hacerla.
    # --- 1. Solicitar ID del estudiante ---
    while True:
        id_student = input("\nIngrese el documento del estudiante: ").lower()
        # Buscar estudiante
        student_found = None
        for st in students:
            if st["id"] == id_student:
                student_found = st
                break
        if student_found is None:
            print(Fore.RED + "\n¡ERROR! El ID es incorrecto o inexistente. Intente de nuevo." + Style.RESET_ALL)
        else:
            break
    # --- 2. Buscar asignaciones del estudiante ---
    assigment_found = None
    for assignment in assigments:
        if assignment["id_student"] == id_student:
            assigment_found = assignment #Guarda todo el diccionario de la asignación de dicho ID en esa variable
            break
    if assigment_found is None:
        print(Fore.YELLOW + f"\nAl estudiante '{student_found['name']}' no se le ha asignado ninguna materia." 
              + Style.RESET_ALL)
        return #Hace que la función termine ahí mismo y no siga ejecutando nada más.
    # --- 3. Convertir códigos en nombres de materias ---
    subjects_list = []
    # recorrer solo las claves que sean code_subjectX
    for key in assigment_found:
        if key.startswith("code_subject"):
            code = assigment_found[key]
            # buscar materia en subjects
            for sub in subjects:
                if sub["code"] == code:
                    subjects_list.append(sub["name_subject"])
                    break
    # --- 4. Mostrar resultado ---
    print(Fore.GREEN + f"\nNombre del estudiante: {student_found['name']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Materias asignadas: {subjects_list}" + Style.RESET_ALL)

def show_subject_students(students, subjects, assigments):
    while True:
        code_subject = input("\nIngrese el código de la materia: ").lower()
        subject_found = None
        for sub in subjects:
            if sub["code"] == code_subject:
                subject_found = sub
                break
        if subject_found is None:
            print(Fore.RED + "\n¡ERROR! El código es incorrecto o inexistente. Intente de nuevo." + Style.RESET_ALL)
        else:
            break
