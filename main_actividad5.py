from funciones_actividad5 import *

students = [{"name": "miguel", "age": 27, "id": "1010"}, {"name": "angel", "age": 28, "id": 1212}]
subjects = [{"name_subject": "Matemáticas", "code": "7878"}, {"name_subject": "Química", "code": "7979"}]
assigments = []

main_choice = main_menu()
while True:
    if main_choice == 1:
        students_choice = students_menu()
        if students_choice == 1:
            new_student = add_students()
            students.append(new_student)
        elif students_choice == 2:
            show_students(students)
        elif students_choice == 3:
            search_student(students)
        elif students_choice == 4:
            delete_student(students)
        elif students_choice == 5:
            print("Chao Mundo")
            break

    elif main_choice == 2:
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
                                    subject["name_subject"] = name_subject
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
                            print(f"Nombre: {subject["name_subject"]} | Código: {subject["code"]}")
                elif subjects_management_choice == 3:
                    found2 = True
                    while found2:
                        code_consult = input("Escriba el código de la materia a consultar: ")
                        for subject in subjects:
                            if subject["code"] == code_consult:
                                print(f"Nombre: {subject["name_subject"]} | Código: {subject["code"]}")
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
                                print(f"Se eliminó la materia {subject["name_subject"]} de la base de datos")
                                break
                        repeat2 = False
                        if delete_subject_code != subject["code"]:
                            print("El código es incorrecto o inexistente. Intente de nuevo")
                            print("")
                            repeat2 = True
                elif subjects_management_choice == 5:
                    break
            except ValueError:
                print("¡ERROR!. Debe ingresar un número entero.")

    elif main_choice == 3:
        while True:
            print("")
            print("-- ASIGNACIONES --")
            print("1. Asignar materia a estudiante")
            print("2. Ver materias de un estudiante")
            print("3. Ver estudiantes por materia")
            print("4. Quitar materia a un estudiante")
            print("5. Atrás")
            print("")
            try:
                assigments_choice = int(input("Escriba el número de la opción seleccionada: "))
                print("")
                if assigments_choice <= 0 or assigments_choice > 5:
                    print("¡ERROR!. Número no contemplado en la lista.")
                elif assigments_choice == 1:
                    found3 = True
                    while found3:
                        assigments_student = input("Ingrese el documento del estudiante: ")
                        for student in students:
                            if student["id"] == assigments_student:
                                print("El estudiante SI existe")
                                found3 = False
                                break
                            elif student["id"] != assigments_student:
                                print("El ID es incorrecto o inexistente. Intente de nuevo")
                                print("")
                                found3 = True
                    found4 = True
                    while found4:
                        assigments_subject = input("Ingrese el código de la materia: ")
                        for subject in subjects:
                            if subject["code"] == assigments_subject:
                                print("La materia SI existe")
                                found4 = False
                                break
                            elif subject["code"] != assigments_subject:
                                print("El código es incorrecto o inexistente. Intente de nuevo")
                                print("")
                                found4 = True

            except ValueError:
                print("¡ERROR!. Debe ingresar un número entero.")

    elif main_choice == 6:
        print("Chao Mundo")
