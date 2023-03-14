import unittest

from controller.controller_discipline import ManageDiscipline
from controller.controller_note import ManageNote
from controller.controller_studenti import ManageStudenti
from domain.discipline import Disciplina
from domain.note import Nota
from domain.sefpromotie import SefPromotieDTO
from domain.studenti import Student
from repository.repository_file_discipline import ListaDisciplineFile
from repository.repository_file_note import ListaNoteFile
from repository.repository_file_studenti import ListaStudentiFile
from sortari.sortare_principala import sortare
from validating.validari_domeniu import StudentValidator, DisciplinaValidator, NoteValidator


class TestControllerStudenti(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_studenti = ListaStudentiFile("Backend/testing/test_files/teste_repository_studenti.txt")
        self.__validari = StudentValidator()
        self.__service = ManageStudenti(self.__repo_studenti, self.__validari)
        self.__service.sterge_toti_studentii()

    def tearDown(self) -> None:
        self.__service.sterge_toti_studentii()

    def test_adauga_student(self):
        self.assertEqual(self.__service.get_nr_studenti_service(), 0)
        self.__service.adauga_student_service([4, "Andrei"])
        self.__service.adauga_student_service([5, "Darius"])
        self.assertEqual(self.__service.get_nr_studenti_service(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_student_service([3, "Pop", "Ion"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_student_service([3, ""])
        self.assertEqual(str(ve.exception), "Nume student invalid!")
        self.__service.adauga_student_service(["Petru"])
        self.__service.adauga_student_service(["Pavel"])
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_student_service([-3, "Gigel"])
        self.assertEqual(str(ve.exception), "ID student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_student_service([-3, ""])
        self.assertEqual(str(ve.exception), "ID student invalid!\nNume student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_student_service([4, "Gigel"])
        self.assertEqual(str(ve.exception), "Student existent!")

    def test_sterge_student(self):
        self.__service.adauga_student_service([4, "Andrei"])
        self.__service.adauga_student_service([5, "Darius"])
        self.assertEqual(self.__service.get_nr_studenti_service(), 2)
        self.__service.sterge_student_id_service([4])
        self.assertEqual(self.__service.get_nr_studenti_service(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_student_id_service([-1])
        self.assertEqual(str(ve.exception), "ID student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_student_id_service([4])
        self.assertEqual(str(ve.exception), "Student inexistent!")
        self.assertEqual(self.__service.get_nr_studenti_service(), 1)

    def test_modifica_student(self):
        self.__service.adauga_student_service([4, "Andrei"])
        self.__service.adauga_student_service([5, "Darius"])
        self.__service.modifica_nume_student_id_service([4, "Ioan"])
        self.assertEqual(self.__service.get_nume_student_id_service(4), "Ioan")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_nume_student_id_service([-3, ""])
        self.assertEqual(str(ve.exception), "ID student invalid!\nNume student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_nume_student_id_service([4, ""])
        self.assertEqual(str(ve.exception), "Nume student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_nume_student_id_service([7, "Luca"])
        self.assertEqual(str(ve.exception), "Student inexistent!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_nume_student_id_service(["Gigel"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")

    def test_get_all_studenti(self):
        with self.assertRaises(ValueError) as ve:
            self.__service.get_all_studenti_service()
        self.assertEqual(str(ve.exception), "Nu exista niciun student introdus!")
        self.__service.adauga_student_service([5, "Darius"])
        self.assertEqual(self.__service.get_all_studenti_service(), {5: Student(5, "Darius")})

    def test_get_student_id(self):
        with self.assertRaises(ValueError) as ve:
            self.__service.get_student_id_service([5, "Matei"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        self.__service.adauga_student_service([7, "Tudor"])
        with self.assertRaises(ValueError) as ve:
            self.__service.get_student_id_service([-5])
        self.assertEqual(str(ve.exception), "ID student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_student_id_service([5])
        self.assertEqual(str(ve.exception), "Student inexistent!")
        self.assertEqual(self.__service.get_student_id_service([7]), Student(7, "Tudor"))

    def test_get_nume_student_id(self):
        self.__service.adauga_student_service([7, "Tudor"])
        self.__service.adauga_student_service([6, "Ciprian"])
        self.assertEqual(self.__service.get_nume_student_id_service(7), "Tudor")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_nume_student_id_service(5)
        self.assertEqual(str(ve.exception), "Student inexistent!")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_nume_student_id_service(-4)
        self.assertEqual(str(ve.exception), "ID student invalid!")

    def test_cauta_studenti(self):
        self.__service.adauga_student_service([6, "Tudor Luca"])
        self.__service.adauga_student_service([7, "Ciprian Luca"])
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_studenti_service(["Luca", "Tudor"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_studenti_service([""])
        self.assertEqual(str(ve.exception), "Nume student invalid!")
        self.assertEqual(self.__service.cauta_studenti_service(["luc"]), [6, 7])

    def test_studenti_random(self):
        with self.assertRaises(ValueError) as ve:
            self.__service.studenti_random_service(-5)
        self.assertEqual(str(ve.exception), "Numar de studenti invalid!")
        self.__service.studenti_random_service(4)
        self.assertEqual(self.__service.get_nr_studenti_service(), 4)

    def test_auto_populare_studenti(self):
        self.__service.auto_populare_studenti_service()
        self.assertGreater(self.__service.get_nr_studenti_service(), 10)


class TestControllerDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_discipline = ListaDisciplineFile("Backend/testing/test_files/teste_repository_discipline.txt")
        self.__validari = DisciplinaValidator()
        self.__service = ManageDiscipline(self.__repo_discipline, self.__validari)
        self.__service.sterge_toate_disciplinele()

    def tearDown(self) -> None:
        self.__service.sterge_toate_disciplinele()

    def test_adauga_disciplina(self):
        self.assertEqual(self.__service.get_nr_discipline_service(), 0)
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.__service.adauga_disciplina_service([4, "Info", "Giulia"])
        self.assertEqual(self.__service.get_nr_discipline_service(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_disciplina_service([3, "Pop", "Ion", "Hi"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_disciplina_service([3, "", "Jonatan"])
        self.assertEqual(str(ve.exception), "Nume disciplina invalid!")
        self.__service.adauga_disciplina_service(["Informatica", "Karina"])
        self.__service.adauga_disciplina_service(["Informatica logica", "Anna"])
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_disciplina_service([-3, "Gigel", "Chimie"])
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_disciplina_service([-3, "", ""])
        self.assertEqual(str(ve.exception), "ID disciplina invalid!\nNume disciplina invalid!\nNume profesor invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_disciplina_service([4, "Logica", "Gigel"])
        self.assertEqual(str(ve.exception), "Disciplina existenta!")

    def test_sterge_disciplina(self):
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.__service.adauga_disciplina_service([4, "Info", "Giulia"])
        self.assertEqual(self.__service.get_nr_discipline_service(), 2)
        self.__service.sterge_disciplina_id_service([3])
        self.assertEqual(self.__service.get_nr_discipline_service(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_disciplina_id_service([-1])
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_disciplina_id_service([3])
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        self.assertEqual(self.__service.get_nr_discipline_service(), 1)

    def test_modifica_disciplina(self):
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.__service.adauga_disciplina_service([4, "Info", "Giulia"])
        self.__service.modifica_disciplina_id_service([3, "nume: Analiza matematica"])
        self.assertEqual(self.__service.get_nume_disciplina_id_service(3), "Analiza matematica")
        self.__service.modifica_disciplina_id_service([3, "prof: Iulia Albu"])
        self.assertEqual(self.__service.get_profesor_disciplina_id_service(3), "Iulia Albu")
        self.__service.modifica_disciplina_id_service([4, "prof: Giulia Letcu", "nume: Informatica"])
        self.assertEqual(self.__service.get_nume_disciplina_id_service(4), "Informatica")
        self.assertEqual(self.__service.get_profesor_disciplina_id_service(4), "Giulia Letcu")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([-3, "nume:"])
        self.assertEqual(str(ve.exception), "ID disciplina invalid!\nNume disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([4, "nume:"])
        self.assertEqual(str(ve.exception), "Nume disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([7, "Luca"])
        self.assertEqual(str(ve.exception), "Comanda invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service(["Gigel"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([-3, "prof:"])
        self.assertEqual(str(ve.exception), "ID disciplina invalid!\nNume profesor invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([4, "prof:"])
        self.assertEqual(str(ve.exception), "Nume profesor invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([7, "Luca"])
        self.assertEqual(str(ve.exception), "Comanda invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service(["Gigel"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([10, "prof:Muresan"])
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_disciplina_id_service([7, "idk:Luca"])
        self.assertEqual(str(ve.exception), "Comanda invalida!")

    def test_get_all_discipline(self):
        with self.assertRaises(ValueError) as ve:
            self.__service.get_all_discipline_service()
        self.assertEqual(str(ve.exception), "Nu exista nicio disciplina introdusa!")
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.assertEqual(self.__service.get_all_discipline_service(), {3: Disciplina(3, "Analiza", "Iulia")})

    def test_get_disciplina_id(self):
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.__service.adauga_disciplina_service([4, "Info", "Giulia"])
        with self.assertRaises(ValueError) as ve:
            self.__service.get_disciplina_id_service(5)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_disciplina_id_service(-5)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        self.assertEqual(self.__service.get_disciplina_id_service(3), Disciplina(3, "Analiza", "Iulia"))

    def test_get_nume_disciplina_id(self):
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.__service.adauga_disciplina_service([4, "Info", "Giulia"])
        with self.assertRaises(ValueError) as ve:
            self.__service.get_nume_disciplina_id_service(-5)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_nume_disciplina_id_service(5)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")

    def test_get_profesor_disciplina_id(self):
        self.__service.adauga_disciplina_service([3, "Analiza", "Iulia"])
        self.__service.adauga_disciplina_service([4, "Info", "Giulia"])
        with self.assertRaises(ValueError) as ve:
            self.__service.get_profesor_disciplina_id_service(-5)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_profesor_disciplina_id_service(5)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")

    def test_cauta_disciplina(self):
        self.__service.adauga_disciplina_service([3, "Analiza matematica", "Pop Iulia"])
        self.__service.adauga_disciplina_service([4, "Informatica", "Marcus Giulia"])
        self.__service.adauga_disciplina_service([5, "Algebra Matematica", "Petrean Iulia"])
        self.__service.adauga_disciplina_service([6, "Info en", "Picovici Giulia"])
        self.assertEqual(self.__service.cauta_discipline_service(["prof: iulia"]), [3, 4, 5, 6])
        self.assertEqual(self.__service.cauta_discipline_service(["nume: MATE"]), [3, 5])
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_discipline_service(["Luca", "Tudor", "idk"])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_discipline_service(["nume:"])
        self.assertEqual(str(ve.exception), "Nume de cautat disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_discipline_service(["prof:"])
        self.assertEqual(str(ve.exception), "Nume de cautat profesor invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_discipline_service(["ceva:idk"])
        self.assertEqual(str(ve.exception), "Comanda invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__service.cauta_discipline_service(["ceva:idk:altcv"])
        self.assertEqual(str(ve.exception), "Comanda invalida!")
        self.assertEqual(self.__service.cauta_discipline_service(["prof: iulia", "nume: mate"]), [3, 5])

    def test_discipline_random(self):
        with self.assertRaises(ValueError) as ve:
            self.__service.discipline_random_service(-5)
        self.assertEqual(str(ve.exception), "Numar de discipline invalid!")
        self.__service.discipline_random_service(4)
        self.assertEqual(self.__service.get_nr_discipline_service(), 4)

    def test_auto_populare_discipline(self):
        self.__service.auto_populare_discipline_service()
        self.assertGreater(self.__service.get_nr_discipline_service(), 5)


class TestControllerNote(unittest.TestCase):
    """
    teste facute in mod black box - nu se iau toate cazurile pentru exemplu
    """

    def setUp(self) -> None:
        repo_studenti = ListaStudentiFile("Backend/testing/test_files/teste_repository_studenti.txt")
        repo_discipline = ListaDisciplineFile("Backend/testing/test_files/teste_repository_discipline.txt")
        repo_note = ListaNoteFile("Backend/testing/test_files/teste_repository_note.txt")
        validari_note = NoteValidator()
        self.__service = ManageNote(repo_note, validari_note, repo_studenti, repo_discipline)
        self.__service.sterge_toti_studentii_si_notele()
        self.__service.sterge_toate_disciplinele_si_notele()
        self.__disciplina1 = Disciplina(3, "Analiza", "Iulia")
        self.__disciplina2 = Disciplina(4, "Info", "Giulia")
        self.__student1 = Student(4, "Andrei")
        self.__student2 = Student(5, "Marian")
        repo_discipline.adauga_disciplina(self.__disciplina1)
        repo_discipline.adauga_disciplina(self.__disciplina2)
        repo_studenti.adauga_student(self.__student1)
        repo_studenti.adauga_student(self.__student2)

    def tearDown(self) -> None:
        self.__service.sterge_toti_studentii_si_notele()
        self.__service.sterge_toate_disciplinele_si_notele()

    def test_adauga_nota(self):
        self.assertEqual(self.__service.get_nr_note_service(), 0)
        with self.assertRaises(ValueError):
            self.__service.get_all_note_service()
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        '''
                self.__nota2 = Nota(12, self.__student2, self.__disciplina1, 5.69)
        self.__nota3 = Nota(13, student1, disciplina2, -56)
        self.__nota4 = Nota(12, self.__student2, self.__disciplina1, 9.3)
        self.__nota5 = Nota(-3, student1, disciplina2, 6.7)
        self.__nota6 = Nota(16, self.__student2, self.__disciplina1, 9.3)
        self.__nota7 = Nota(17, self.__student2, disciplina2, 9.3)'''
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError):
            self.__service.adauga_nota_service([-3, 4, 4, 6.7])

    def test_sterge_nota_id(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        self.__service.sterge_nota_id_service(11)
        self.assertEqual(self.__service.get_nr_note_service(), 1)
        with self.assertRaises(ValueError):
            self.__service.sterge_nota_id_service(10)
        self.assertEqual(self.__service.get_nr_note_service(), 1)

    def test_sterge_student_si_notele_sale(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        self.assertEqual(self.__service.get_nr_note_service(), 4)
        self.__service.sterge_student_si_notele_sale_service(4)
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError):
            self.__service.sterge_student_si_notele_sale_service(11)
        self.assertEqual(self.__service.get_nr_note_service(), 2)

    def test_sterge_disciplina_si_note(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        self.assertEqual(self.__service.get_nr_note_service(), 4)
        self.__service.sterge_disciplina_si_note_service(4)
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError):
            self.__service.sterge_disciplina_si_note_service(11)
        self.assertEqual(self.__service.get_nr_note_service(), 2)

    def test_modifica_valoare_nota(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.assertEqual(self.__service.get_valoare_nota_id_service(11), 7.6)
        self.__service.modifica_valoare_nota_service(11, 8.8)
        self.assertEqual(self.__service.get_valoare_nota_id_service(11), 8.8)
        with self.assertRaises(ValueError):
            self.__service.modifica_valoare_nota_service(16, 8.8)

    def test_get_note_disc(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        l1, l2 = self.__service.get_note_disc(3)
        self.assertEqual(l1, [Nota(11, 4, 3, 7.6), Nota(12, 5, 3, 5.69)])
        self.assertEqual(l2, [Nota(11, 4, 3, 7.6), Nota(12, 5, 3, 5.69)])

    def test_sef_promotie(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        l_sef = self.__service.sefpromotie()
        sef = l_sef[0]
        self.assertEqual(sef.getid(), 4)
        self.assertEqual(sef.getnume(), "Andrei")

    def test_medie_generala_disciplina(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        l1, l2 = self.__service.medie_generala_disciplina(4)

    def test_auto_populare_note(self):
        self.__service.auto_populare_note_service(10)
        self.assertGreater(self.__service.get_nr_note_service(), 5)


class TestControllerNoteWhiteBox(unittest.TestCase):
    """
    teste facute in mod black box - nu se iau toate cazurile pentru exemplu
    """

    def setUp(self) -> None:
        repo_studenti = ListaStudentiFile("Backend/testing/test_files/teste_repository_studenti.txt")
        repo_discipline = ListaDisciplineFile("Backend/testing/test_files/teste_repository_discipline.txt")
        repo_note = ListaNoteFile("Backend/testing/test_files/teste_repository_note.txt")
        validari_note = NoteValidator()
        self.__service = ManageNote(repo_note, validari_note, repo_studenti, repo_discipline)
        self.__service.sterge_toti_studentii_si_notele()
        self.__service.sterge_toate_disciplinele_si_notele()
        self.__disciplina1 = Disciplina(3, "Analiza", "Iulia")
        self.__disciplina2 = Disciplina(4, "Info", "Giulia")
        self.__student1 = Student(4, "Andrei")
        self.__student2 = Student(5, "Marian")
        repo_discipline.adauga_disciplina(self.__disciplina1)
        repo_discipline.adauga_disciplina(self.__disciplina2)
        repo_studenti.adauga_student(self.__student1)
        repo_studenti.adauga_student(self.__student2)

    def tearDown(self) -> None:
        self.__service.sterge_toate_notele()
        self.__service.sterge_toti_studentii_si_notele()
        self.__service.sterge_toate_disciplinele_si_notele()

    def test_adauga_nota(self):
        self.assertEqual(self.__service.get_nr_note_service(), 0)
        with self.assertRaises(ValueError) as ve:
            self.__service.get_all_note_service()
        self.assertEqual(str(ve.exception), "Nu exista nicio nota introdusa!")
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        '''
                self.__nota2 = Nota(12, self.__student2, self.__disciplina1, 5.69)
        self.__nota3 = Nota(13, student1, disciplina2, -56)
        self.__nota4 = Nota(12, self.__student2, self.__disciplina1, 9.3)
        self.__nota5 = Nota(-3, student1, disciplina2, 6.7)
        self.__nota6 = Nota(16, self.__student2, self.__disciplina1, 9.3)
        self.__nota7 = Nota(17, self.__student2, disciplina2, 9.3)'''
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([-3, 4, 4, 6.7])
        self.assertEqual(str(ve.exception), "ID nota invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([3, -4, -4, 6.7])
        self.assertEqual(str(ve.exception), "ID student invalid!\nID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([3, 4, 4, 67])
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([3, 1, 4, 6.7])
        self.assertEqual(str(ve.exception), "Student inexistent!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([3, 4, 1, 6.7])
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([5, 3, 4, 1, 6.7])
        self.assertEqual(str(ve.exception), "Numar parametri invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.adauga_nota_service([12, 4, 4, 6.7])
        self.assertEqual(str(ve.exception), "Nota existenta!")

    def test_sterge_nota_id(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        self.__service.sterge_nota_id_service(11)
        self.assertEqual(self.__service.get_nr_note_service(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_nota_id_service(10)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")
        self.assertEqual(self.__service.get_nr_note_service(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_nota_id_service(-10)
            self.assertEqual(str(ve.exception), "ID nota invalid!")
        self.assertEqual(self.__service.get_nr_note_service(), 1)

    def test_sterge_student_si_notele_sale(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        self.assertEqual(self.__service.get_nr_note_service(), 4)
        self.__service.sterge_student_si_notele_sale_service(4)
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError):
            self.__service.sterge_student_si_notele_sale_service(11)
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_student_si_notele_sale_service(-11)
        self.assertEqual(str(ve.exception), "ID student invalid!")

    def test_sterge_disciplina_si_note(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        self.assertEqual(self.__service.get_nr_note_service(), 4)
        self.__service.sterge_disciplina_si_note_service(4)
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError):
            self.__service.sterge_disciplina_si_note_service(11)
        self.assertEqual(self.__service.get_nr_note_service(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__service.sterge_disciplina_si_note_service(-11)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        self.assertEqual(self.__service.get_nr_note_service(), 2)

    def test_modifica_valoare_nota(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.assertEqual(self.__service.get_valoare_nota_id_service(11), 7.6)
        self.__service.modifica_valoare_nota_service(11, 8.8)
        self.assertEqual(self.__service.get_valoare_nota_id_service(11), 8.8)
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_valoare_nota_service(16, 8.8)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_valoare_nota_service(-16, 8.8)
        self.assertEqual(str(ve.exception), "ID nota invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.modifica_valoare_nota_service(11, 88)
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")

    def test_get_note_disc(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        l1, l2 = self.__service.get_note_disc(3)
        self.assertEqual(l1, [Nota(11, 4, 3, 7.6), Nota(12, 5, 3, 5.69)])
        self.assertEqual(l2, [Nota(11, 4, 3, 7.6), Nota(12, 5, 3, 5.69)])

    def test_get_valoare_nota_id(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        with self.assertRaises(ValueError) as ve:
            self.__service.get_valoare_nota_id_service(-11)
        self.assertEqual(str(ve.exception), "ID nota invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__service.get_valoare_nota_id_service(13)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")

    def test_get_all_note_string(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.assertEqual(self.__service.get_all_note_string_service(),
                         {11: "Nota cu ID-ul [11] si valoarea 7.6 atribuita studentului cu ID-ul [4]: Andrei "
                              "la disciplina cu ID-ul [3]: Analiza"})

    def test_sef_promotie(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        l_sef = self.__service.sefpromotie()
        sef = l_sef[0]
        self.assertEqual(sef.getid(), 4)
        self.assertEqual(sef.getnume(), "Andrei")

    def test_medie_generala_disciplina(self):
        self.__service.adauga_nota_service([11, 4, 3, 7.6])
        self.__service.adauga_nota_service([12, 5, 3, 5.69])
        self.__service.adauga_nota_service([13, 4, 4, 8.34])
        self.__service.adauga_nota_service([14, 5, 4, 3.4])
        l1, l2 = self.__service.medie_generala_disciplina(4)

    def test_auto_populare_note(self):
        self.__service.auto_populare_note_service(10)
        self.assertGreater(self.__service.get_nr_note_service(), 5)


def suita_controller():
    test_suite_contoller = unittest.TestSuite()
    test_suite_contoller.addTest(unittest.makeSuite(TestControllerStudenti))
    test_suite_contoller.addTest(unittest.makeSuite(TestControllerDiscipline))
    test_suite_contoller.addTest(unittest.makeSuite(TestControllerNote))
    test_suite_contoller.addTest(unittest.makeSuite(TestControllerNoteWhiteBox))
    return test_suite_contoller
