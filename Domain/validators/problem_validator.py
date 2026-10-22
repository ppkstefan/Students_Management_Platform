class ValidationException(Exception):
    def __init__(self, message):
        self.__message = message
    def get_message(self):
        return self.__message

class ProblemaValidator:
    def __init__(self, problem):
        self.problem = problem

    def validate(self):
        if not isinstance(self.problem.get_numar_laborator(), int) or self.problem.get_numar_laborator() <= 0:
            raise ValidationException("Numar laborator invalid!")
        if not isinstance(self.problem.get_numar_problema(), int) or self.problem.get_numar_problema() <= 0:
            raise ValidationException("Numar problema invalid!")
        if not self.problem.get_descriere().strip():
            raise ValidationException("Descriere goala!")
        if not self.problem.get_deadline().strip():
            raise ValidationException("Deadline gol!")
