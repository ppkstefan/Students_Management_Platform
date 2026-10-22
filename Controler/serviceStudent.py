from Domain.studentClass import Studenti
from Domain.validators.student_validator import *
import random

class ServiceStudent:
    def __init__(self, repo, repoAssign, repoNota):
        self.__repo = repo
        self.__repoAssign = repoAssign
        self.__repoNota = repoNota

    def adauga(self, studentID, nume, grupa,gen):
        """

        :param studentID (int): student id
        :param nume (str): nume student
        :param grupa (float): grupa elev
        :param gen (str): gen M/F
        :return:
        """
        student= Studenti(studentID, nume, grupa, gen)
        StudentValidator(student).validate()
        self.__repo.add(student)

    def get_all(self):
        """
        :return:repo studenti
        """
        return self.__repo.get_all()

    def update_student(self, studentID, nume, grupa, gen):
        """

        :param studentID (int): student id:
        :param nume(str): nume student
        :param grupa (float): grupa elev
        :param gen(str): gen M/F
        :return:
        """
        student= Studenti(studentID, nume, grupa, gen)
        StudentValidator(student).validate()
        self.__repo.update(student)

    def delete_student(self, studentID):
        """
        deletes a student
        :param studentID (int): student id
        :return:
        """
        assigns = self.__repoAssign.cauta_dupa_student(studentID)
        for assign in assigns:
            lab= assign.get_problema().get_numar_laborator()
            prob = assign.get_problema().get_numar_problema()
            self.__repoNota.sterge_nota_pentru_assignment(studentID, lab, prob)
            self.__repoAssign.delete(studentID, lab, prob)

        self.__repo.delete(studentID)


    def sort_gen(self, gen):
        """
        sorteaza dupa gen
        :param gen (str): gen M/F :
        :return: rezultatul sortarii
        """
        studenti = self.__repo.get_all()
        rezultat = [s for s in studenti if s.get_gen().lower() == gen.lower()]
        return rezultat

    def cautareStudent(self, studentID):
        """
        cauta un student
        :param studentID (int): student id:
        :return: studentul al carui id corespunde
        """
        studenti = self.__repo.get_all()
        for s in studenti:
            if s.get_id() == studentID:
                return s
        return None

    def random_student(self,userChoice):
        """
        function for generating random students
        :param userChoice:
        :return: None
        """
        #generare ID
        for i in range(0, userChoice):

            while True:
                studentID = random.randint(1, 100)
                studenti = self.__repo.get_all()
                ok=True
                for s in studenti:
                    if s.get_id() == studentID:
                        ok=False
                    if ok==False:
                         break
                if ok==True:
                    break

            #Generare nume
            numePosibile = ["Matei", "Marcel", "Petrisor", "DorianPopa", "Selaru", "Eminescu", "Costel", "Makaveli", "Popica", "Gabi"]
            numeStudent = random.choice(numePosibile)

            grupa=round(random.random(), 2)

            genuri=["M", "F"]
            gen = random.choice(genuri)

            student = Studenti(studentID, numeStudent, grupa, gen)
            StudentValidator(student).validate()
            self.__repo.add(student)





