import unittest
import os
from Domain.studentClass import Studenti
from Domain.problemClass import ProblemaLaborator
from Domain.assignClass import Assignment
from Domain.notareclass import Nota  # Atentie la typo-ul din numele fisierului tau (notareclass vs notareClass)

from Repository.repositoryStudent import RepositoryStudent
from Repository.repositoryProblem import RepositoryProblemaLaborator
from Repository.repositoryAssignment import RepositoryAssignment
from Repository.repositoryNota import RepositoryNota

from Controler.serviceStudent import ServiceStudent
from Controler.serviceProblema import ServiceProblema
from Controler.serviceAssignment import ServiceAssignment
from Controler.serviceNota import ServiceNota


class TestAplicatie(unittest.TestCase):

    def setUp(self):
        """
        Aceasta functie ruleaza INAINTE de fiecare test.
        Cream fisiere temporare goale si initializam service-urile.
        """
        self.file_studenti = "test_studenti_temp.txt"
        self.file_probleme = "test_probleme_temp.txt"
        self.file_assign = "test_assigns_temp.txt"
        self.file_note = "test_note_temp.txt"

        with open(self.file_studenti, "w") as f: f.write("")
        with open(self.file_probleme, "w") as f: f.write("")
        with open(self.file_assign, "w") as f: f.write("")
        with open(self.file_note, "w") as f: f.write("")

        self.repo_student = RepositoryStudent(self.file_studenti)
        self.repo_problema = RepositoryProblemaLaborator(self.file_probleme)

        self.repo_assign = RepositoryAssignment(self.file_assign, self.file_probleme, self.file_studenti)

        self.repo_nota = RepositoryNota(self.file_note, self.repo_assign)

        self.srv_student = ServiceStudent(self.repo_student, self.repo_assign, self.repo_nota)
        self.srv_problema = ServiceProblema(self.repo_problema, self.repo_assign, self.repo_nota)

        self.srv_assign = ServiceAssignment(self.repo_assign, self.repo_student, self.repo_problema)
        self.srv_nota = ServiceNota(self.repo_nota, self.repo_assign)

    def tearDown(self):
        """
        Stergem fisierele create dupa test.
        """
        if os.path.exists(self.file_studenti): os.remove(self.file_studenti)
        if os.path.exists(self.file_probleme): os.remove(self.file_probleme)
        if os.path.exists(self.file_assign): os.remove(self.file_assign)
        if os.path.exists(self.file_note): os.remove(self.file_note)

    def test_adaugare_student(self):
        self.srv_student.adauga(1, "Popescu Ion", "1.1", "M")
        all_st = self.srv_student.get_all()
        self.assertEqual(len(all_st), 1)
        self.assertEqual(all_st[0].get_nume(), "Popescu Ion")

        with self.assertRaises(Exception):
            self.srv_student.adauga(-2, "Eroare", "1.1", "M")

    def test_cautare_student(self):
        self.srv_student.adauga(1, "Cautat", "1.1", "M")
        gasit = self.srv_student.cautareStudent(1)
        self.assertIsNotNone(gasit)
        self.assertEqual(gasit.get_nume(), "Cautat")

        nu_exista = self.srv_student.cautareStudent(999)
        self.assertIsNone(nu_exista)

    def test_adaugare_problema(self):
        self.srv_problema.adaugaProblema(1, 1, "Descriere test", "12/12/2025")
        all_pb = self.srv_problema.get_all()
        self.assertEqual(len(all_pb), 1)
        self.assertEqual(all_pb[0].get_descriere(), "Descriere test")

    def test_assign_flux_normal(self):
        self.srv_student.adauga(10, "Student Assign", "2.1", "F")
        self.srv_problema.adaugaProblema(5, 5, "Problema Grea", "01/01/2026")

        self.srv_assign.assign(10, 5, 5)

        all_a = self.srv_assign.get_all()
        self.assertEqual(len(all_a), 1)
        self.assertEqual(all_a[0].get_student().get_nume(), "Student Assign")

    def test_assign_invalid(self):
        self.srv_problema.adaugaProblema(1, 1, "Ceva", "Date")
        with self.assertRaises(Exception):
            self.srv_assign.assign(999, 1, 1)

    def test_adaugare_nota(self):
        # 1. Adaugam Student
        self.srv_student.adauga(1, "Elev Silitor", "1.1", "M")
        # 2. Adaugam Problema
        self.srv_problema.adaugaProblema(1, 1, "Calcul", "Az")
        # 3. Facem Assignment-ul
        self.srv_assign.assign(1, 1, 1)

        self.repo_assign.read_assignment_from_file()

        # 4. Adaugam Nota
        try:
            self.srv_nota.adauga_nota(1, 1, 1, 10.0)
        except Exception as e:
            self.fail(f"Eroare la adaugarea notei: {str(e)}")

        all_n = self.srv_nota.get_all()
        self.assertEqual(len(all_n), 1)
        self.assertEqual(all_n[0].get_valoare(), 10.0)

    def test_statistica_sub_5(self):
        self.srv_student.adauga(1, "Elev Slab", "1.1", "M")
        self.srv_student.adauga(2, "Elev Bun", "1.1", "F")
        self.srv_problema.adaugaProblema(1, 1, "P1", "D")

        self.srv_assign.assign(1, 1, 1)
        self.srv_assign.assign(2, 1, 1)

        self.repo_assign.read_assignment_from_file()

        self.srv_nota.adauga_nota(1, 1, 1, 4.0)
        self.srv_nota.adauga_nota(2, 1, 1, 9.0)

        rezultat = self.srv_nota.statistica_medii_sub5()

        self.assertEqual(len(rezultat), 1)
        self.assertEqual(rezultat[0][0].get_nume(), "Elev Slab")
        self.assertEqual(rezultat[0][1], 4.0)

    # ---------------- TESTE STERGERE CASCADA (NOU) ----------------
    def test_stergere_cascada(self):
        print("\n--- Test Stergere Cascada ---")
        self.srv_student.adauga(99, "De Sters", "1", "M")
        self.srv_problema.adaugaProblema(99, 99, "De Sters", "Azi")

        self.srv_assign.assign(99, 99, 99)
        self.repo_assign.read_assignment_from_file()  # Refresh pt nota

        self.srv_nota.adauga_nota(99, 99, 99, 5.0)

        self.assertEqual(len(self.srv_student.get_all()), 1)
        self.assertEqual(len(self.srv_assign.get_all()), 1)
        self.assertEqual(len(self.srv_nota.get_all()), 1)

        self.srv_student.delete_student(99)

        self.assertEqual(len(self.srv_student.get_all()), 0, "Studentul nu a fost sters")
        self.assertEqual(len(self.srv_assign.get_all()), 0, "Assignment-ul nu a fost sters in cascada")
        self.assertEqual(len(self.srv_nota.get_all()), 0, "Nota nu a fost stersa in cascada")
        print("Stergerea in cascada functioneaza!")


if __name__ == '__main__':
    unittest.main()