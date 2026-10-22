from Domain.studentClass import Studenti
from Repository.repository_Exception import RepositoryExceptionStudent

class RepositoryStudent:

    def __init__(self, path_to_studenti):
        """
        :param path_to_studenti (str): path to studenti
        """
        self.__students = []
        self.__path_to_studenti = path_to_studenti

    def read_students_from_file(self):
        """
        read students from file
        :return:
        """
        with open(self.__path_to_studenti, 'r') as file:
            lines=file.readlines()
            self.__students = []
            k=0
            for line in lines:
                line=line.strip()
                k+=1
                if k%4==1:
                    id=int(line)
                if k%4==2:
                    name=line
                if k%4==3:
                    grupa=line
                if k%4==0:
                    gender=line
                    student = Studenti(id, name, grupa, gender)
                    self.__students.append(student)
                    k=0

    def store_students_in_file(self):
        """
        store students in file
        :return:
        """
        with open(self.__path_to_studenti, 'w') as file:
            for student in self.__students:
                file.writelines(str(student.get_id()) + "\n")
                file.writelines(str(student.get_nume()) + "\n")
                file.writelines(str(student.get_grup()) + "\n")
                file.writelines(str(student.get_gen()) + "\n")

    def add(self, new_student):
        """
        adds a new student to the repository
        :param new_student:
        """
        self.read_students_from_file()
        for s in self.__students:
            if s.get_id() == new_student.get_id():
                raise RepositoryExceptionStudent(f"Student with id {new_student.get_id()} already exists!")
        self.__students.append(new_student)
        self.store_students_in_file()

    def get_all(self):
        """
        get all students
        :return: repo students
        """
        self.read_students_from_file()
        return self.__students

    def print_all(self):
        for s in self.__students:
            print(s)

    def update(self, updated_student):
        """
        updates a student with updated student
        :param updated_student:
        :return:
        """
        self.read_students_from_file()
        for s in self.__students:
            if s.get_id() == updated_student.get_id():
                s.nume = updated_student.get_nume()
                s.grup = updated_student.get_grup()
                s.gen = updated_student.get_gen()
                self.store_students_in_file()
                return
        raise RepositoryExceptionStudent(f"Student with id {updated_student.get_id()} does not exist!")



    def delete(self, student_id):
        """
        deletes a student from repository
        :param student_id:
        :return:
        """
        self.read_students_from_file()
        for s in self.__students:
            if s.get_id() == student_id:
                self.__students.remove(s)
                self.store_students_in_file()
                return
        raise RepositoryExceptionStudent(f"Student with id {student_id} does not exist!")