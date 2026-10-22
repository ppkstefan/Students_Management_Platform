class ProblemaLaborator:
    def __init__(self, numar_laborator, numar_problema, descriere, deadline):
        """
        Studenti CLass
        :param numar_laborator:
        :param numar_problema:
        :param descriere:
        :param deadline:
        """
        self.__numar_laborator = numar_laborator
        self.__numar_problema = numar_problema
        self.__descriere = descriere
        self.__deadline = deadline

    def __getitem__(self, key):
        if(key == 'numar_laborator'):
            return self.__numar_laborator
        elif(key == 'numar_problema'):
            return self.__numar_problema
        elif(key == 'descriere'):
            return self.__descriere
        elif(key == 'deadline'):
            return self.__deadline

    def __str__(self):
        """
        Print function for Studenti
        :return:
        """
        return f"Numar Laborator:{self.__numar_laborator}   |   Numar Problema:{self.__numar_problema}   |   Descriere: {self.__descriere}  |   Deadline: {self.__deadline}"
    #instanceMethods
    def get_numar_laborator(self):
        return self.__numar_laborator
    def get_numar_problema(self):
        return self.__numar_problema
    def get_descriere(self):
        return self.__descriere
    def get_deadline(self):
        return self.__deadline
