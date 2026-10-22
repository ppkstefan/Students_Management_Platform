from Domain.notareclass import Nota


# Nu mai ai nevoie de importul RepositoryAssignment aici, il primesti ca obiect

class RepositoryNota:
    def __init__(self, path_to_note, repo_assignment):
        """
        :param path_to_note (str): path to note
        :param repo_assignment: repo assignment
        """
        self.__note = []
        self.__path_to_note = path_to_note
        self.__repo_assignment = repo_assignment  # Primim repo-ul gata facut

    def read_note_from_file(self):
        """
        read note from file
        :return:
        """
        assignments = self.__repo_assignment.get_all()

        try:
            with open(self.__path_to_note, 'r') as file:
                lines = file.readlines()
                self.__note = []
                for line in lines:
                    line = line.strip()
                    if line == "": continue
                    parts = line.split(',')

                    st_id = int(parts[0])
                    lab = int(parts[1])
                    prob = int(parts[2])
                    valoare = float(parts[3])

                    # Cautam assignment-ul care corespunde acestor ID-uri
                    target_assign = None
                    for a in assignments:
                        if (a.get_student().get_id() == st_id and
                                a.get_problema().get_numar_laborator() == lab and
                                a.get_problema().get_numar_problema() == prob):
                            target_assign = a
                            break

                    if target_assign:
                        nota = Nota(target_assign, valoare)
                        self.__note.append(nota)
        except FileNotFoundError:
            self.__note = []

    def store_note_in_file(self):
        """
        store note in file
        :return:
        """
        with open(self.__path_to_note, 'w') as file:
            for nota in self.__note:
                a = nota.get_assignment()
                line = f"{a.get_student().get_id()},{a.get_problema().get_numar_laborator()},{a.get_problema().get_numar_problema()},{nota.get_valoare()}\n"
                file.write(line)

    def add(self, nota):
        """
        :param nota:
        :return:
        """
        self.read_note_from_file()
        for n in self.__note:
            a1 = n.get_assignment()
            a2 = nota.get_assignment()
            if (a1.get_student().get_id() == a2.get_student().get_id() and
                    a1.get_problema().get_numar_laborator() == a2.get_problema().get_numar_laborator() and
                    a1.get_problema().get_numar_problema() == a2.get_problema().get_numar_problema()):
                raise Exception("Nota exista deja pentru acest assignment!")

        self.__note.append(nota)
        self.store_note_in_file()

    def sterge_nota_pentru_assignment(self, student_id, lab, prob):
        """
        Sterge nota asociata unui assignment specific.
        """
        self.read_note_from_file()
        initial_len = len(self.__note)

        self.__note = [n for n in self.__note if not (
                n.get_assignment().get_student().get_id() == student_id and
                n.get_assignment().get_problema().get_numar_laborator() == lab and
                n.get_assignment().get_problema().get_numar_problema() == prob
        )]

        if len(self.__note) != initial_len:
            self.store_note_in_file()

    def get_all(self):
        """
        :return: repo note
        """
        self.read_note_from_file()
        return self.__note[:]

    def cauta_dupa_student(self, student_id):
        self.read_note_from_file()
        return [n for n in self.__note if n.get_assignment().get_student().get_id() == student_id]