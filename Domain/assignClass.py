class Assignment:
    def __init__(self, student, problema):
        """
        CLass Assignment
        :param student from Student Class:
        :param problema from Problem Class:
        """
        self.__student = student
        self.__problema = problema

    def get_student(self):
        """
        :return: student from Student Class:
        """
        return self.__student

    def get_problema(self):
        """
        :return: problem from Problem Class:
        """
        return self.__problema

    def __str__(self):
        """
        print function of Assignment Class:
        """
        return f" {self.__student.get_nume()} (ID={self.__student.get_id()}) - Problema {self.__problema.get_numar_problema()} / Lab {self.__problema.get_numar_laborator()}"

