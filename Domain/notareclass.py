class Nota:
    def __init__(self, assignment, valoare):
        self.__assignment = assignment
        self.__valoare = valoare

    def get_assignment(self):
        return self.__assignment

    def get_valoare(self):
        return self.__valoare

    def __str__(self):
            s = self.__assignment.get_student().get_nume()
            p = self.__assignment.get_problema()
            return f"{s} | Lab {p.get_numar_laborator()} Prob {p.get_numar_problema()} | Nota: {self.__valoare}"
