class Studenti:
    def __init__(self, studentID, nume, grup, gen):
        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup
        self.__gen = gen

    def __getitem__(self, key):
        if(key == 'studentID'):
            return self.__studentID
        elif(key == 'nume'):
            return self.__nume
        elif(key == 'grup'):
            return self.__grup
        elif(key == 'gen'):
            return self.__gen
    def __str__(self):
        return f"Student_ID:{self.__studentID}   |   Nume:{self.__nume}   |   Grup: {self.__grup}   |   Gen: {self.__gen}"
    # instanceMethods
    def get_id(self):
        return self.__studentID
    def get_nume(self):
        return self.__nume
    def get_grup(self):
        return self.__grup
    def get_gen(self):
        return self.__gen
