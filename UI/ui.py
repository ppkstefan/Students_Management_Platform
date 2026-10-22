from Domain.validators.student_validator import ValidationException
from Repository.repository_Exception import RepositoryExceptionStudent, RepositoryExceptionProblemaLaborator, RepositoryExceptionAssign


class UI:
    def __init__(self, serviceStudent, serviceProblema, serviceAssignment, serviceNota):
        self.__serviceStudent=serviceStudent
        self.__serviceProblema=serviceProblema
        self.__serviceAssignment = serviceAssignment
        self.__serviceNota = serviceNota

    def read_type(self, text, expected_type):
        while True:
            data = input(text)
            try:
                data = expected_type(data)
                return data
            except ValueError:
                print("Invalid type!")

    def start(self):
        while True:
            print("______________________________________________")
            print("Alege cu ce clasa vrei sa lucrezi:")
            print("1)Studenti")
            print("2)Problema Laborator")
            print("3)Assignment")
            print("4)Nota")
            print("______________________________________________")
            choice=self.read_type("Enter choice >>>", int)
            match choice:
                case 1:
                    while True:
                        print("______________________________________________")
                        print("Comenzi valabile:")
                        print("1)( ADD ) Adauga student")
                        print("2)( PRINT ) Printeaza studenti")
                        print("3)( UPDATE ) Update student ")
                        print("4)( DELETE ) Delete student ")
                        print("5)( SORTGEN ) Sorteaza studenti bazat pe gen")
                        print("6)( CAUTARE ) Cauta student")
                        print("7)( RANDOM ) Adauga X studenti random")
                        print("8)( EXIT ) Exit")
                        print("______________________________________________")
                        comanda = self.read_type("Comanda >>> : ", str).upper()
                        try:
                            match comanda:
                                case "ADD":
                                    id = self.read_type("Da id: ", int)
                                    nume = self.read_type("Da nume: ", str)
                                    grupa = self.read_type("Da grupa: ", str)
                                    gen = self.read_type("Da gen: ", str)
                                    self.__serviceStudent.adauga(id, nume, grupa,gen)
                                case "PRINT":
                                    for student in self.__serviceStudent.get_all():
                                        print(student)
                                case "UPDATE":
                                    id = self.read_type("Da id pentru update: ", int)
                                    nume = self.read_type("Da un nou nume: ", str)
                                    grupa = self.read_type("Da o noua grupa: ", str)
                                    gen = self.read_type("Da gen: ", str)
                                    self.__serviceStudent.update_student(id, nume, grupa, gen)
                                case "DELETE":
                                    id = self.read_type("Da id pentru delete: ", int)
                                    self.__serviceStudent.delete_student(id)

                                case "SORTGEN":
                                    gen = self.read_type("Da gen pentru filtrare (ex: M/F): ", str)
                                    studenti_gen = self.__serviceStudent.sort_gen(gen)
                                    if not studenti_gen:
                                        print(f"Nu există studenți cu genul '{gen}'.")
                                    else:
                                        print(f"Studenți cu genul '{gen}':")
                                        for student in studenti_gen:
                                            print(student)
                                case "CAUTARE":
                                    id= self.read_type("Da id pentru cautare: ", int)
                                    student = self.__serviceStudent.cautareStudent(id)
                                    if student is None:
                                        print("Studentul nu exista!")
                                    else:
                                        print(student)
                                case "RANDOM":
                                    userChoice = self.read_type("Enter how much students do you want to generate >>>", int)
                                    self.__serviceStudent.random_student(userChoice)
                                case "EXIT":
                                    break
                        except (RepositoryExceptionStudent, ValidationException) as ex:
                            print(ex.get_message())
                case 2:
                    while True:
                        print("______________________________________________")
                        print("Comenzi valabile:")
                        print("1)( ADD ) Adauga problema")
                        print("2)( PRINT ) Printeaza probleme")
                        print("3)( UPDATE ) Update problema ")
                        print("4)( DELETE ) Delete problema ")
                        print("5.( CAUTARE ) Cauta problema")
                        print("6)( RANDOM ) Adauga X probleme random")
                        print("7)( EXIT ) Exit")
                        print("______________________________________________")
                        comanda = self.read_type("Comanda >>> : ", str).upper()

                        try:
                            match comanda:

                                case "ADD":
                                    NumarLaborator = self.read_type("Da nr lab: ", int)
                                    NumarProblema = self.read_type("Da nr problema: ", int)
                                    descriere = self.read_type("Da descriere: ", str)
                                    deadline = self.read_type("Da deadline: ", str)
                                    self.__serviceProblema.adaugaProblema(NumarLaborator, NumarProblema, descriere,
                                                                          deadline)
                                case "PRINT":
                                    for problema in self.__serviceProblema.get_all():
                                        print(problema)
                                case "UPDATE":
                                    NumarLaborator = self.read_type("Lab: ", int)
                                    NumarProblema = self.read_type("Problema: ", int)
                                    descriere = self.read_type("Noua descriere: ", str)
                                    deadline = self.read_type("Noul deadline: ", str)
                                    self.__serviceProblema.update_problema(NumarLaborator, NumarProblema, descriere,
                                                                           deadline)
                                case "DELETE":
                                    NumarLaborator = self.read_type("Lab: ", int)
                                    NumarProblema = self.read_type("Problema: ", int)
                                    self.__serviceProblema.delete_problema(NumarLaborator, NumarProblema)
                                case "CAUTARE":
                                    NumarLaborator = self.read_type("Da nr laborator pentru cautare: ", int)
                                    NumarProblema = self.read_type("Da nr problema pentru cautare: ", int)
                                    problema = self.__serviceProblema.cautareProblema(NumarLaborator, NumarProblema)
                                    if problema is None:
                                        print("Problema nu exista!")
                                    else:
                                        print(problema)
                                case "RANDOM":
                                    userChoice = self.read_type("Enter how much problems do you want to generate >>>", int)
                                    self.__serviceProblema.random_problema(userChoice)
                                case "EXIT":
                                    break
                        except (RepositoryExceptionProblemaLaborator, ValidationException) as ex:
                            print(ex.get_message())
                case 3:
                    while True:
                        print("1) ( ASSIGN ) ASSIGN STUDENT PROBLEMA")
                        print("2) ( DELETE ) DELETE ASSIGNMENT")
                        print("3) ( STUDENT )CAUTARE DUPA STUDENT")
                        print("4) ( PROBLEMA )CAUTARE DUPA PROBLEMA")
                        print("5) ( PRINT )PRINT ASSIGNMENTS")
                        print("6) ( EXIT ) EXIT")

                        cmd = self.read_type("Comanda >>> ", str).upper()
                        try:
                            match cmd:
                                case "ASSIGN":
                                    id = self.read_type("ID student: ", int)
                                    lab = self.read_type("Lab: ", int)
                                    prob = self.read_type("Problema: ", int)
                                    self.__serviceAssignment.assign(id, lab, prob)

                                case "DELETE":
                                    id = self.read_type("ID student: ", int)
                                    lab = self.read_type("Lab: ", int)
                                    prob = self.read_type("Problema: ", int)
                                    self.__serviceAssignment.delete(id, lab, prob)

                                case "STUDENT":
                                    id = self.read_type("ID student: ", int)
                                    rez = self.__serviceAssignment.cauta_dupa_student(id)
                                    for a in rez: print(a)

                                case "PROBLEMA":
                                    lab = self.read_type("Lab: ", int)
                                    prob = self.read_type("Problema: ", int)
                                    rez = self.__serviceAssignment.cauta_dupa_problema(lab, prob)
                                    for a in rez: print(a)

                                case "PRINT":
                                    for a in self.__serviceAssignment.get_all():
                                        print(a)
                                case "EXIT":
                                    break
                        except (RepositoryExceptionAssign, ValidationException) as ex:
                            print(ex.get_message())
                case 4:
                    while True:
                        print("1) ADD - Adauga nota")
                        print("2) PRINT - Afiseaza toate notele")
                        print("3) STUDENT - Afiseaza notele unui student")
                        print("4) STATISTICATOTI - Statistica dupa nume/nota")
                        print("5) STATISTICASUB5 - Statistica elevi sub 5")
                        print("6) STATISTICAPESTE5 - Statistica elevi peste 5")
                        print("7) ( EXIT ) Exit ")

                        cmd = self.read_type("Comanda >>> ", str).upper()
                        try:
                            match cmd:
                                case "ADD":
                                    id = self.read_type("ID student: ", int)
                                    lab = self.read_type("Lab: ", int)
                                    prob = self.read_type("Problema: ", int)
                                    nota = self.read_type("Nota (1-10): ", float)
                                    self.__serviceNota.adauga_nota(id, lab, prob, nota)

                                case "PRINT":
                                    for n in self.__serviceNota.get_all():
                                        print(n)

                                case "STUDENT":
                                    id = self.read_type("ID student: ", int)
                                    rez = self.__serviceNota.cauta_dupa_student(id)
                                    for n in rez:
                                        print(n)

                                case "STATISTICATOTI":
                                    lab = self.read_type("Lab: ", int)
                                    prob = self.read_type("Problema: ", int)
                                    criteriu = self.read_type("Sortare dupa (nume/nota): ", str)

                                    rez = self.__serviceNota.statistica_problema(lab, prob, criteriu)
                                    if not rez:
                                        print("Nu exista note pentru aceasta problema.")
                                    else:
                                        for student, nota in rez:
                                            print(f"{student.get_nume()} - Nota: {nota}")

                                case "STATISTICASUB5":
                                    rez = self.__serviceNota.statistica_medii_sub5()
                                    if not rez:
                                        print("Niciun student nu are media sub 5.")
                                    else:
                                        for student, medie in rez:
                                            print(f"{student.get_nume()} - Media: {medie:.2f}")
                                case "STATISTICAPESTE5":
                                    rez = self.__serviceNota.statistica_medii_peste5()
                                    if not rez:
                                        print("Niciun student nu are media peste 5.")
                                    else:
                                        for student, medie in rez:
                                            print(f"{student.get_nume()} - Media: {medie:.2f}")
                                case "EXIT":
                                    break
                        except (RepositoryExceptionStudent, ValidationException) as ex:
                            print(ex.get_message())
                case _:
                    print("Invalid choice!")
