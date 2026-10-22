from Repository.repository_Exception import RepositoryExceptionAssign
from Repository.repositoryStudent import RepositoryStudent
from Repository.repositoryProblem import RepositoryProblemaLaborator
from Domain.assignClass import Assignment

class RepositoryAssignment:
    def __init__(self, path_to_assigns, path_to_probleme, path_to_studenti):
        """
        :param path_to_assigns: str path to assignment file
        :param path_to_probleme: str path to problem file
        :param path_to_studenti: str path to student file
        """
        self.__assignments = []
        self.__path_to_assigns = path_to_assigns
        self.__path_to_probleme = path_to_probleme
        self.__path_to_studenti = path_to_studenti


    def find_students_by_id(self, student_id, repoStudenti):
        """
        finds students by id
        :param student_id:
        :param repoStudenti:
        :return:
        """
        for student in repoStudenti.get_all():
            if student.get_id() == student_id:
                return student

    def find_problema_by_nr_lab_nr_pb(self, nr_lab, nr_problema, repoProblema):
        """
        finds problems by nr lab nr
        :param nr_lab:
        :param nr_problema:
        :param repoProblema:
        :return:
        """
        for problema in repoProblema.get_all():
            if problema.get_numar_laborator() == nr_lab and problema.get_numar_problema() == nr_problema:
                return problema

    def read_assignment_from_file(self):
        """
        reads assignment from file
        :return:
        """
        with open(self.__path_to_assigns, 'r') as file:
            lines = file.readlines()
            self.__assignments = []
            for line in lines:
                line = line.strip()
                line = line.split(',')
                repoStudenti=RepositoryStudent(self.__path_to_studenti)
                repoProblema=RepositoryProblemaLaborator(self.__path_to_probleme)
                student=self.find_students_by_id(int(line[0]), repoStudenti)
                problema=self.find_problema_by_nr_lab_nr_pb(int(line[1]), int(line[2]), repoProblema)
                assign=Assignment(student, problema)
                self.__assignments.append(assign)

    def store_assignment_in_file(self):
        """
        stores assignment in file
        :return:
        """
        with open(self.__path_to_assigns, 'w') as file:
            for assignment in self.__assignments:
                file.writelines(str(assignment.get_student().get_id()) + ",")
                file.writelines(str(assignment.get_problema().get_numar_laborator()) + ",")
                file.writelines(str(assignment.get_problema().get_numar_problema()) + "\n")


    def add(self, assignment):
        """
        adds a student to repository
        :param assignment:
        :return:
        """
        self.read_assignment_from_file()
        for a in self.__assignments:
            if (a.get_student().get_id() == assignment.get_student().get_id() and
                a.get_problema().get_numar_laborator() == assignment.get_problema().get_numar_laborator() and
                a.get_problema().get_numar_problema() == assignment.get_problema().get_numar_problema()):
                raise RepositoryExceptionAssign("Acest assignment exista deja!")

        self.__assignments.append(assignment)
        self.store_assignment_in_file()

    def delete(self, student_id, lab, problema):
        """
        deletes a student from repository
        :param student_id:
        :param lab:
        :param problema:
        :return:
        """
        self.read_assignment_from_file()
        for a in self.__assignments:
            if (a.get_student().get_id() == student_id and
                a.get_problema().get_numar_laborator() == lab and
                a.get_problema().get_numar_problema() == problema):
                self.__assignments.remove(a)
                self.store_assignment_in_file()
                return

        raise RepositoryExceptionAssign("Assignment-ul nu exista!")

    def get_all(self):
        """
        :return:assigns
        """
        self.read_assignment_from_file()
        return self.__assignments[:]

    def cauta_dupa_student(self, student_id):
        self.read_assignment_from_file()
        return [a for a in self.__assignments if a.get_student().get_id() == student_id]

    def cauta_dupa_problema(self, lab, problema):
        self.read_assignment_from_file()
        return [a for a in self.__assignments if
                a.get_problema().get_numar_laborator() == lab and
                a.get_problema().get_numar_problema() == problema]
