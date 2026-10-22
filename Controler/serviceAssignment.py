from Domain.assignClass import Assignment
from Repository.repository_Exception import RepositoryExceptionAssign

class ServiceAssignment:
    def __init__(self, repoAssign, repoStudent, repoProblema):
        """
        :param repoAssign:
        :param repoStudent:
        :param repoProblema:
        """
        self.__repoAssign = repoAssign
        self.__repoStudent = repoStudent
        self.__repoProblema = repoProblema

    def assign(self, student_id, lab, problema):
        """
        assigneaza un student cu o problema
        :param student_id (int): student id
        :param lab (int): nr lab
        :param problema (int): nr pb
        :return:
        """
        studenti = self.__repoStudent.get_all()
        student = None
        for s in studenti:
            if s.get_id() == student_id:
                student = s
                break
        if student is None:
            raise RepositoryExceptionAssign("Studentul nu exista!")
        # caut problema
        probleme = self.__repoProblema.get_all()
        prob = None
        for p in probleme:
            if p.get_numar_laborator() == lab and p.get_numar_problema() == problema:
                prob = p
                break
        if prob is None:
            raise RepositoryExceptionAssign("Problema nu exista!")

        # creeaza
        assignment = Assignment(student, prob)
        self.__repoAssign.add(assignment)

    def delete(self, student_id, lab, problema):
        """

        :param student_id(int): id student
        :param lab (int): nr lab
        :param problema (int): nr problema
        :return:
        """
        self.__repoAssign.delete(student_id, lab, problema)

    def cauta_dupa_student(self, student_id):
        """
        cauta un student dupa un id
        :param student_id (int): id student
        :return: returneaza assignmenturile studentului
        """
        return self.__repoAssign.cauta_dupa_student(student_id)

    def cauta_dupa_problema(self, lab, problema):
        """
        cauta un problema dupa un id
        :param lab (int): nr lab
        :param problema (int): nr problema
        :return: returneaza assignmentulrile cu problema data
        """
        return self.__repoAssign.cauta_dupa_problema(lab, problema)

    def get_all(self):
        """
        :return: repo assignuri
        """
        return self.__repoAssign.get_all()
