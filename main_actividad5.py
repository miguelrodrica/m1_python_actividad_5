from funciones_actividad5 import *

students = [{"name": "miguel", "age": 27, "id": "1010"}, {"name": "angel", "age": 28, "id": "1212"}]
subjects = [{"name_subject": "Matemáticas", "code": "7878"}, {"name_subject": "Química", "code": "7979"}]
assigments = [{"id_student": "1010", "code_subject1": "7878", "code_subject2": "7979"}]

while True:
    main_choice = main_menu()
    if main_choice == 1:
        while True:
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
                break
    elif main_choice == 2:
        while True:
            subjects_choice = subjects_menu()
            if subjects_choice == 1:
                new_subject = add_subject()
                subjects.append(new_subject)
            elif subjects_choice == 2:
                show_subjects(subjects)
            elif subjects_choice == 3:
                search_subject(subjects)
            elif subjects_choice == 4:
                delete_subjects(subjects)
            elif subjects_choice == 5:
                break
    elif main_choice == 3:
        while True:
            assigments_choice = assigments_menu()
            if assigments_choice == 1:
                new_assignment = assign_subject_to_student(students,subjects)
                assigments.append(new_assignment)
            elif assigments_choice == 2:
                show_student_subjects(students,subjects,assigments)
            elif assigments_choice == 3:
                show_subject_students(students, subjects, assigments)
    elif main_choice == 6:
        break
