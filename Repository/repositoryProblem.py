from Domain.problemClass import ProblemaLaborator
from Repository.repository_Exception import RepositoryExceptionStudent
from Repository.repository_Exception import RepositoryExceptionProblemaLaborator

class RepositoryProblemaLaborator:
    def __init__(self, path_to_probleme):
        """
        :param path_to_probleme (str): path to file probleme
        """
        self.__probleme = []
        self.__path_to_probleme = path_to_probleme

    def read_probleme_from_file(self):
        """
        read probleme from file
        :return:
        """
        with open(self.__path_to_probleme, 'r') as file:
            lines=file.readlines()
            self.__probleme=[]
            for line in lines:
                line=line.strip()
                line=line.split(',')
                nrLab=int(line[0])
                nrProblema=int(line[1])
                descriere=line[2]
                deadline=line[3]
                problema=ProblemaLaborator(nrLab,nrProblema,descriere,deadline)
                self.__probleme.append(problema)

    def store_probleme_to_file(self):
        """
        store the probleme to file
        :return:
        """
        with open(self.__path_to_probleme, 'w') as file:
            for problem in self.__probleme:
                file.writelines(str(problem.get_numar_laborator()) + ",")
                file.writelines(str(problem.get_numar_problema()) + ",")
                file.writelines(str(problem.get_descriere()) + ",")
                file.writelines(str(problem.get_deadline()) + "\n")

    def addProblema(self, new_problem):
        """
        adds a problem to the repository
        :param new_problem:
        :return:
        """
        self.read_probleme_from_file()
        for s in self.__probleme:
            if s.get_numar_laborator() == new_problem.get_numar_laborator() and s.get_numar_problema() == new_problem.get_numar_problema():
                raise RepositoryExceptionProblemaLaborator(
                    f"Problema {new_problem.get_numar_problema()} din lab {new_problem.get_numar_laborator()} exista deja!"
                )
        self.__probleme.append(new_problem)
        self.store_probleme_to_file()

    def get_all(self):
        self.read_probleme_from_file()
        return self.__probleme[:]

    def update(self, updated_problem):
        """
        updates a problem from the repository
        :param updated_problem:
        :return:
        """
        self.read_probleme_from_file()
        for s in self.__probleme:
            if s.get_numar_laborator() == updated_problem.get_numar_laborator() and s.get_numar_problema() == updated_problem.get_numar_problema():
                s.descriere = updated_problem.get_descriere()
                s.deadline = updated_problem.get_deadline()
                self.store_probleme_to_file()
                return
        raise RepositoryExceptionProblemaLaborator(
            f"Problema {updated_problem.get_numar_problema()} din lab {updated_problem.get_numar_laborator()} nu exista!"
        )

    def delete(self, nr_laborator, nr_problema):
        """
        deletes a student from repository
        :param nr_laborator:
        :param nr_problema:
        :return:
        """
        self.read_probleme_from_file()
        for s in self.__probleme:
            if s.get_numar_laborator() == nr_laborator and s.get_numar_problema() == nr_problema:
                self.__probleme.remove(s)
                self.store_probleme_to_file()
                return
        raise RepositoryExceptionProblemaLaborator(
            f"Problema {nr_problema} din lab {nr_laborator} nu exista!"
        )