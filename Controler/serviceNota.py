from Domain.notareclass import Nota
from Domain.validators.problem_validator import *
from Controler.utils import *


class ServiceNota:
    def __init__(self, repoNota, repoAssign):
        """
        :param repoNota: repo nota
        :param repoAssign: repo assign
        """
        self.__repoNota = repoNota
        self.__repoAssign = repoAssign

    def adauga_nota(self, student_id, lab, problema, valoare):
        """
        adauga nota
        :param student_id(int): id student
        :param lab (int): nr lab
        :param problema (int):nr pb
        :param valoare (float): valoare nota
        :return:
        """
        assignments = self.__repoAssign.get_all()
        target = None

        for a in assignments:
            if (a.get_student().get_id() == student_id and
                a.get_problema().get_numar_laborator() == lab and
                a.get_problema().get_numar_problema() == problema):
                target = a
                break

        if target is None:
            raise Exception("Assignment-ul nu exista! Nu poti pune nota.")

        nota = Nota(target, valoare)
        self.__repoNota.add(nota)

    def get_all(self):
        """
        :return: repo note
        """
        return self.__repoNota.get_all()

    def cauta_dupa_student(self, student_id):
        """
        cauta nota dupa student
        :param student_id (int): id student
        :return:
        """
        return self.__repoNota.cauta_dupa_student(student_id)

    def statistica_problema(self, lab, problema, criteriu):
        """
        statistica problema
        :param lab (int): nr lab
        :param problema (int): nr pb
        :param criteriu (str): criteriu pentru sortare
        :return:
        """
        rezultat = []
        for n in self.__repoNota.get_all():
            a = n.get_assignment()
            if (a.get_problema().get_numar_laborator() == lab and
                    a.get_problema().get_numar_problema() == problema):
                rezultat.append((a.get_student(), n.get_valoare()))

        if criteriu.lower() == "nume":
            rezultat = generic_sort(
                rezultat,
                key=lambda x: (x[0].get_nume(), x[1]),
                algorithm='bubble'
            )
        elif criteriu.lower() == "nota":
            rezultat = generic_sort(
                rezultat,
                key=lambda x: x[1],
                algorithm='shell'
            )
        return rezultat

    def statistica_medii_sub5(self):
        """
        statistica medii sub5
        :return: rezultatul sortarii
        """
        note_student = {}
        for n in self.__repoNota.get_all():
            a = n.get_assignment()
            sid = a.get_student().get_id()
            if sid not in note_student:
                note_student[sid] = []
            note_student[sid].append(n.get_valoare())

        rezultat = []
        for n in note_student:
            medie = sum(note_student[n]) / len(note_student[n])
            if medie < 5:
                student = None
                for nota in self.__repoNota.get_all():
                    if nota.get_assignment().get_student().get_id() == n:
                        student = nota.get_assignment().get_student()
                        break
                rezultat.append((student, medie))

        return generic_sort(
            rezultat,
            key=lambda x: x[0].get_nume(),
            algorithm='shell'
        )

    def statistica_medii_peste5(self):
        """
        statistica medii peste5
        :return: rezultatul statistici
        """
        note_student = {}
        for n in self.__repoNota.get_all():
            a = n.get_assignment()
            sid = a.get_student().get_id()
            if sid not in note_student:
                note_student[sid] = []
            note_student[sid].append(n.get_valoare())

        rezultat = []
        for n in note_student:
            medie = sum(note_student[n]) / len(note_student[n])
            if medie >= 5:
                student = None
                for nota in self.__repoNota.get_all():
                    if nota.get_assignment().get_student().get_id() == n:
                        student = nota.get_assignment().get_student()
                        break
                rezultat.append((student, medie))

        # Sortare Shell dupa nume
        return generic_sort(
            rezultat,
            key=lambda x: x[0].get_nume(),
            algorithm='shell'
        )