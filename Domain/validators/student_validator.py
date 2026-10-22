def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class ValidationException(Exception):
    def __init__(self, message):
        self.__message = message
    def get_message(self):
        return self.__message

class StudentValidator:
    def __init__(self, student):
        self.student = student

    def validate(self):
        if not isinstance(self.student.get_nume(), str):
            raise ValidationException("Nume invalid! Trebuie sa contina doar litere.")
        if not isinstance(self.student.get_id(), int) or self.student.get_id() <= 0:
            raise ValidationException("ID invalid!")
        if not is_float(self.student.get_grup()):
            raise ValidationException("Grupa invalida! Trebuie sa fie numar.")
        if not self.student.get_gen().isalpha():
            raise ValidationException("Gen invalid! Trebuie sa contina doar litere.")


