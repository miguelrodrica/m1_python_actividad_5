students = []
subjects = []

while True:
    print("")
    print("-- MENÚ ACADÉMICO --")
    print("1. Gestión de estudiantes")
    print("2. Gestión de materias")
    print("3. Asignaciones")
    print("4. Notas y calificaciones")
    print("5. Reportes y estadísticas")
    print("6. Salir")
    print("")
    try:
        user_choice = int(input("Escriba el número de la opción seleccionada: "))
        print("")
        if user_choice <= 0 or user_choice > 6:
            print("¡ERROR!. Número no contemplado en la lista.")
        elif user_choice == 1:
            while True:
                print("")
                print("-- GESTIÓN ESTUDIANTES --")
                print("1. Registrar estudiantes")
                print("2. Listar estudiantes")
                print("3. Consultar estudiante con ID")
                print("4. Eliminar estudiante")
                print("5. Atrás")
                print("")
                try:
                    students_management_choice = int(input("Escriba el número de la opción seleccionada: "))
                    print("")
                    if students_management_choice <= 0 or students_management_choice > 5:
                        print("¡ERROR!. Número no contemplado en la lista.")
                    elif students_management_choice == 1:
                        while True:
                            try:
                                qty_in_stu = int(input("¿Cuántos estudiantes desea ingresar?: "))
                                if qty_in_stu <= 0:
                                    print("¡ERROR!. Ingrese un número positivo y diferente a 0.")
                                else:
                                    for i in range(qty_in_stu):
                                        student = {}
                                        print("")
                                        print(f"Estudiante #{i+1}")
                                        name_student = input("Nombre: ")
                                        student["name"] = name_student
                                        while True:
                                            try:
                                                age_student = int(input("Edad: "))
                                                if age_student <= 0:
                                                    print("¡ERROR!. La edad debe ser mayor a 0.")
                                                    continue
                                                else:
                                                    student["age"] = age_student
                                                break
                                            except ValueError:
                                                print("¡ERROR!. La edad debe ser un número.")
                                        id_student = input("ID: ")
                                        student["id"] = id_student
                                        students.append(student)
                                break
                            except ValueError:
                                print("¡ERROR!. Debe ingresar un número entero.")
                    elif students_management_choice == 2:
                        if len(students) == 0:
                            print("¡VACÍO! Aún no se registra ningún estudiante.")
                        else:
                            for student in students:
                                print(f"Nombre: {student["name"]} | Edad: {student["age"]} | ID: {student["id"]}")
                    elif students_management_choice == 3:
                        found = True
                        while found:
                            id_consult = input("Escriba el ID del estudiante a consultar: ")
                            for student in students:
                                if student["id"] == id_consult:
                                    print(f"Nombre: {student["name"]} | Edad: {student["age"]} | ID: {student["id"]}")
                                    break
                            found = False
                            if student["id"] != id_consult:
                                print("El ID es incorrecto o inexistente. Intente de nuevo")
                                print("")
                                found = True
                    elif students_management_choice == 4:
                        repeat = True
                        while repeat:
                            delete_student_id = input("Escriba el ID del estudiante a eliminar: ")
                            for student in students:
                                if delete_student_id == student["id"]:
                                    students.remove(student)
                                    print(f"Se eliminó al estudiante {student["name"]} de la base de datos")
                                    break
                            repeat = False
                            if delete_student_id != student["id"]:
                                print("El ID es incorrecto o inexistente. Intente de nuevo")
                                print("")
                                repeat = True
                    elif students_management_choice == 5:
                        break
                except ValueError:
                    print("¡ERROR!. Debe ingresar un número entero.")

        elif user_choice == 2:
            while True:
                print("")
                print("-- GESTIÓN MATERIAS --")
                print("1. Registrar materias")
                print("2. Listar materias")
                print("3. Consultar materia por código")
                print("4. Eliminar materia")
                print("5. Atrás")
                print("")
                try:
                    subjects_management_choice = int(input("Escriba el número de la opción seleccionada: "))
                    print("")
                    if subjects_management_choice <= 0 or subjects_management_choice > 5:
                        print("¡ERROR!. Número no contemplado en la lista.")
                    elif subjects_management_choice == 1:
                        while True:
                            try:
                                qty_in_subjects = int(input("¿Cuántas materias desea ingresar?: "))
                                if qty_in_subjects <= 0:
                                    print("¡ERROR!. Ingrese un número positivo y diferente a 0.")
                                else:
                                    for i in range(qty_in_subjects):
                                        subject = {}
                                        print("")
                                        print(f"Materia #{i+1}")
                                        name_subject = input("Nombre: ")
                                        subject["name"] = name_subject
                                        code_subject = input("Código: ")
                                        subject["code"] = code_subject
                                        subjects.append(subject)
                                break
                            except ValueError:
                                print("¡ERROR!. Debe ingresar un número entero.")
                    elif subjects_management_choice == 2:
                        if len(subjects) == 0:
                            print("¡VACÍO! Aún no se registra ninguna materia.")
                        else:
                            for subject in subjects:
                                print(f"Nombre: {subject["name"]} | Código: {subject["code"]}")
                    elif subjects_management_choice == 3:
                        found2 = True
                        while found2:
                            code_consult = input("Escriba el código de la materia a consultar: ")
                            for subject in subjects:
                                if subject["code"] == code_consult:
                                    print(f"Nombre: {subject["name"]} | Código: {subject["code"]}")
                                    break
                            found2 = False
                            if subject["code"] != code_consult:
                                print("El código es incorrecto o inexistente. Intente de nuevo")
                                print("")
                                found2 = True
                    elif subjects_management_choice == 4:
                        repeat2 = True
                        while repeat2:
                            delete_subject_code = input("Escriba el código del estudiante a eliminar: ")
                            for sucject in subjects:
                                if delete_subject_code == subject["code"]:
                                    subjects.remove(subject)
                                    print(f"Se eliminó la materia {subject["name"]} de la base de datos")
                                    break
                            repeat2 = False
                            if delete_subject_code != subject["code"]:
                                print("El código es incorrecto o inexistente. Intente de nuevo")
                                print("")
                                repeat2 = True
                    elif students_management_choice == 5:
                        break
                except ValueError:
                    print("¡ERROR!. Debe ingresar un número entero.")

        elif user_choice == 3:
            print("Hola Mundo")

        elif user_choice == 6:
            break
    except ValueError:
        print("¡ERROR!. Debe ingresar un número entero.")