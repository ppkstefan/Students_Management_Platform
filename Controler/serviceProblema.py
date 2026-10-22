from Domain.validators.problem_validator import *
from Domain.problemClass import ProblemaLaborator
import random

class ServiceProblema:
    def __init__(self, repo, repoAssign, repoNota):
        """
        :param repo:
        :param repoAssign:
        :param repoNota:
        """
        self.__repo = repo
        self.__repoAssign = repoAssign
        self.__repoNota = repoNota

    def adaugaProblema(self, NumarLab, NumarProblema, descriere, deadline):
        """
        adauga problema
        :param NumarLab:
        :param NumarProblema:
        :param descriere:
        :param deadline:
        :return:
        """
        problema = ProblemaLaborator(NumarLab, NumarProblema, descriere, deadline)
        ProblemaValidator(problema).validate()
        self.__repo.addProblema(problema)

    def get_all(self):
        """
        :return: repo problema
        """
        return self.__repo.get_all()

    def update_problema(self, NumarLab, NumarProblema, descriere, deadline):
        """
        update problema
        :param NumarLab:
        :param NumarProblema:
        :param descriere:
        :param deadline:
        :return:
        """
        problema = ProblemaLaborator(NumarLab, NumarProblema, descriere, deadline)
        ProblemaValidator(problema).validate()
        self.__repo.update(problema)

    def delete_problema(self, NumarLab, NumarProblema):
        """
        delete problema
        :param NumarLab:
        :param NumarProblema:
        :return:
        """
        assigns=self.__repoAssign.cauta_dupa_problema(NumarLab, NumarProblema)
        for assign in assigns:
            studentID = assign.get_student().get_student_id()
            self.__repoAssign.delete(studentID, NumarLab, NumarProblema)
            self.__repoNota.sterge_nota_pentru_assignment(studentID, NumarLab, NumarProblema)
        self.__repo.delete(NumarLab, NumarProblema)


    def cautareProblema(self, NumarLab, NumarProblema):
        """
        cauta problema
        :param NumarLab:
        :param NumarProblema:
        :return:
        """
        problema = self.__repo.get_all()
        for p in problema:
            if p.get_numar_laborator() == NumarLab and p.get_numar_problema() == NumarProblema:
                return p
        return None

    def random_problema(self,userChoice):
        """
        function for generating random problems
        :param userChoice:
        :return: None
        """
        for i in range(0, userChoice):

            while True:
                nr_lab = random.randint(1, 100)
                nr_problema= random.randint(1, 100)
                problema = self.__repo.get_all()
                ok=True
                for p in problema:
                    if p.get_numar_laborator() == nr_lab and p.get_numar_problema() == nr_problema:
                        ok=False
                    if ok==False:
                         break
                if ok==True:
                    break

            #Generare nume
            descriere = ["wow", "foarte tare", "matematica", "algebra liniara 2+2", "analiza serii Taylor"]
            descriere = random.choice(descriere)

            deadline = ["12/09/2025", "34/56/2090", "01/01/2026", "99/101/2234"]
            deadline = random.choice(deadline)

            problema = ProblemaLaborator(nr_lab,nr_problema, descriere, deadline)
            ProblemaValidator(problema).validate()
            self.__repo.addProblema(problema)