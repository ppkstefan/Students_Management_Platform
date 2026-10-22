class RepositoryExceptionStudent(Exception):
    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

class RepositoryExceptionProblemaLaborator (Exception):
    def __init__(self, message):
        self.__message = message
    def get_message(self):
        return self.__message


class RepositoryExceptionAssign(Exception):
    def __init__(self, message):
        self.__message = message
    def get_message(self):
        return self.__message
