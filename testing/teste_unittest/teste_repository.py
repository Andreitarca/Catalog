import unittest

from domain.discipline import Disciplina
from domain.note import Nota
from domain.studenti import Student
from repository.repository_file_discipline import ListaDisciplineFile
from repository.repository_file_note import ListaNoteFile
from repository.repository_file_studenti import ListaStudentiFile


class TestRepositoryFileStudenti(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_studenti = ListaStudentiFile("Backend/testing/test_files/teste_repository_studenti.txt")
        self.__repo_studenti_gres = ListaStudentiFile("idk aici ceva")
        self.__repo_studenti.del_all()
        self.__student1 = Student(4, "Andrei")
        self.__student2 = Student(5, "Marian")
        self.__student3 = Student(4, "Gigel")
        self.__student4 = Student(-3, "Hagi")
        self.__student5 = Student(3, "")
        self.__student6 = Student(-2, "")
        self.__student7 = Student(7, "Ionel")

    def tearDown(self) -> None:
        self.__repo_studenti.del_all()

    def test_fisier_gresit(self):
        with self.assertRaises(IOError) as io:
            self.__repo_studenti_gres.adauga_student(self.__student1)
        self.assertEqual(str(io.exception), "The file doesn't exist!")

    def test_adauga_student(self):
        self.assertEqual(self.__repo_studenti.getlenlista(), 0)
        self.__repo_studenti.adauga_student(self.__student1)
        self.__repo_studenti.adauga_student(self.__student2)
        self.assertEqual(self.__repo_studenti.getlenlista(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__repo_studenti.adauga_student(self.__student3)
        self.assertEqual(str(ve.exception), "Student existent!")
        self.assertEqual(self.__repo_studenti.getlenlista(), 2)

    def test_get_lista(self):
        self.__repo_studenti.adauga_student(self.__student1)
        self.assertEqual(self.__repo_studenti.getlista(), {self.__student1.getid(): self.__student1})

    def test_get_stud_from_id(self):
        self.__repo_studenti.adauga_student(self.__student1)
        self.__repo_studenti.adauga_student(self.__student2)
        self.assertEqual(self.__repo_studenti.get_stud_from_id(4), self.__student1)
        with self.assertRaises(ValueError) as ve:
            self.__repo_studenti.get_stud_from_id(6)
        self.assertEqual(str(ve.exception), "Student inexistent!")

    def test_sterge_student(self):
        self.assertEqual(self.__repo_studenti.getlenlista(), 0)
        self.__repo_studenti.adauga_student(self.__student1)
        self.__repo_studenti.adauga_student(self.__student2)
        self.assertEqual(self.__repo_studenti.getlenlista(), 2)
        self.__repo_studenti.sterge_student(self.__student1)
        self.assertEqual(self.__repo_studenti.getlenlista(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__repo_studenti.sterge_student(self.__student7)
        self.assertEqual(str(ve.exception), "Student inexistent!")
        self.assertEqual(self.__repo_studenti.getlenlista(), 1)

    def test_get_nume_student(self):
        self.__repo_studenti.adauga_student(self.__student1)
        self.__repo_studenti.adauga_student(self.__student2)
        self.assertEqual(self.__repo_studenti.get_nume_student(self.__student1), "Andrei")
        with self.assertRaises(ValueError) as ve:
            self.__repo_studenti.get_nume_student(self.__student7)
        self.assertEqual(str(ve.exception), "Student inexistent!")

    def test_modifica_nume_student(self):
        self.__repo_studenti.adauga_student(self.__student1)
        self.__repo_studenti.adauga_student(self.__student2)
        self.assertEqual(self.__repo_studenti.get_nume_student(self.__student1), "Andrei")
        self.__repo_studenti.modifica_nume_student(self.__student1, "Ioan")
        self.assertEqual(self.__repo_studenti.get_nume_student(self.__student1), "Ioan")
        with self.assertRaises(ValueError) as ve:
            self.__repo_studenti.modifica_nume_student(self.__student7, "Luca")
        self.assertEqual(str(ve.exception), "Student inexistent!")


class TestRepositoryFileDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo_discipline = ListaDisciplineFile("Backend/testing/test_files/teste_repository_studenti.txt")
        self.__repo_discipline_gres = ListaDisciplineFile("idk aici ceva")
        self.__repo_discipline.del_all()
        self.__disciplina1 = Disciplina(3, "Analiza", "Iulia")
        self.__disciplina2 = Disciplina(4, "Info", "Giulia")
        self.__disciplina3 = Disciplina(3, "", "")
        self.__disciplina4 = Disciplina(-3, "", "Maria")
        self.__disciplina5 = Disciplina(4, "Informatica", "Karina")

    def tearDown(self) -> None:
        self.__repo_discipline.del_all()

    def test_fisier_gresit(self):
        with self.assertRaises(IOError) as io:
            self.__repo_discipline_gres.adauga_disciplina(self.__disciplina1)
        self.assertEqual(str(io.exception), "The file doesn't exist!")

    def test_adauga_disciplina(self):
        self.assertEqual(self.__repo_discipline.getlenlista(), 0)
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.getlenlista(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.adauga_disciplina(self.__disciplina4)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!\nNume disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.adauga_disciplina(self.__disciplina3)
        self.assertEqual(str(ve.exception), "Nume disciplina invalid!\nNume profesor invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.adauga_disciplina(self.__disciplina5)
        self.assertEqual(str(ve.exception), "Disciplina existenta!")
        self.assertEqual(self.__repo_discipline.getlenlista(), 2)

    def test_getlista(self):
        self.assertEqual(self.__repo_discipline.getlista(), {})
        pass

    def test_get_disc_from_id(self):
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.get_disc_from_id(3), self.__disciplina1)
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.get_disc_from_id(-4)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.get_disc_from_id(6)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")

    def test_sterge_disciplina(self):
        self.assertEqual(self.__repo_discipline.getlenlista(), 0)
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.getlenlista(), 2)
        self.__repo_discipline.sterge_disciplina(self.__disciplina1)
        self.assertEqual(self.__repo_discipline.getlenlista(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.sterge_disciplina(self.__disciplina1)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        self.assertEqual(self.__repo_discipline.getlenlista(), 1)

    def test_get_nume_disciplina(self):
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.get_nume_disciplina(self.__disciplina1), "Analiza")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.get_nume_disciplina(self.__disciplina4)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")

    def test_get_prof_disciplina(self):
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.get_prof_disciplina(self.__disciplina1), "Iulia")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.get_prof_disciplina(self.__disciplina4)
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")

    def test_modifica_nume_disciplina(self):
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.get_nume_disciplina(self.__disciplina1), "Analiza")
        self.__repo_discipline.modifica_nume_disciplina(self.__disciplina1, "Analiza matematica")
        self.assertEqual(self.__repo_discipline.get_nume_disciplina(self.__disciplina1), "Analiza matematica")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.modifica_nume_disciplina(self.__disciplina4, "Chimie")
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.modifica_nume_disciplina(self.__disciplina2, "")
        self.assertEqual(str(ve.exception), "Nume disciplina invalid!")

    def test_modifica_prof_disciplina(self):
        self.__repo_discipline.adauga_disciplina(self.__disciplina1)
        self.__repo_discipline.adauga_disciplina(self.__disciplina2)
        self.assertEqual(self.__repo_discipline.get_prof_disciplina(self.__disciplina1), "Iulia")
        self.__repo_discipline.modifica_profesor_disciplina(self.__disciplina1, "Iulia Teodora")
        self.assertEqual(self.__repo_discipline.get_prof_disciplina(self.__disciplina1), "Iulia Teodora")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.modifica_profesor_disciplina(self.__disciplina4, "Teodor")
        self.assertEqual(str(ve.exception), "Disciplina inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__repo_discipline.modifica_profesor_disciplina(self.__disciplina2, "")
        self.assertEqual(str(ve.exception), "Nume profesor invalid!")


class TestRepositoryFileNote(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ListaNoteFile("Backend/testing/test_files/teste_repository_note.txt")
        self.__repo_gresit = ListaNoteFile("ceva acolo")
        self.__repo.del_all()
        student1 = Student(4, "Andrei")
        self.__student2 = Student(5, "Marian")
        self.__disciplina1 = Disciplina(3, "Analiza", "Iulia")
        disciplina2 = Disciplina(4, "Info", "Giulia")
        self.__nota1 = Nota(11, 4, 3, 7.6)
        self.__nota2 = Nota(12, 5, 3, 5.69)
        self.__nota3 = Nota(13, 4, 4, -56)
        self.__nota4 = Nota(12, 5, 3, 9.3)
        self.__nota5 = Nota(-3, 4, 4, 6.7)
        self.__nota6 = Nota(16, 5, 3, 9.3)
        self.__nota7 = Nota(17, 5, 4, 9.3)

    def tearDown(self) -> None:
        self.__repo.del_all()

    def test_fisier_gresit(self):
        with self.assertRaises(IOError) as io:
            self.__repo_gresit.adauga_nota(self.__nota1)
        self.assertEqual(str(io.exception), "The file doesn't exist!")

    def test_adauga_nota(self):
        self.assertEqual(self.__repo.getlenlista(), 0)
        self.assertEqual(self.__repo.getlista(), {})
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.assertEqual(self.__repo.getlenlista(), 2)
        with self.assertRaises(ValueError) as ve:
            self.__repo.adauga_nota(self.__nota4)
        self.assertEqual(str(ve.exception), "Nota existenta!")
        with self.assertRaises(ValueError) as ve:
            self.__repo.adauga_nota(self.__nota3)
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__repo.adauga_nota(self.__nota5)
        self.assertEqual(str(ve.exception), "ID nota invalid!")
        self.assertEqual(self.__repo.getlenlista(), 2)

    def test_sterge_nota(self):
        self.assertEqual(self.__repo.getlenlista(), 0)
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.__repo.sterge_nota(self.__nota1)
        self.assertEqual(self.__repo.getlenlista(), 1)
        with self.assertRaises(ValueError) as ve:
            self.__repo.sterge_nota(self.__nota1)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")

    def test_sterge_note_student(self):
        self.assertEqual(self.__repo.getlenlista(), 0)
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.__repo.adauga_nota(self.__nota6)
        self.__repo.sterge_note_student(5)
        self.assertEqual(self.__repo.getlenlista(), 1)

    def test_sterge_note_disciplina(self):
        self.assertEqual(self.__repo.getlenlista(), 0)
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.__repo.adauga_nota(self.__nota6)
        self.__repo.adauga_nota(self.__nota7)
        self.__repo.sterge_note_disciplina(3)
        self.assertEqual(self.__repo.getlenlista(), 1)

    def test_get_note_disciplina(self):
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.__repo.adauga_nota(self.__nota6)
        self.__repo.adauga_nota(self.__nota7)
        self.assertEqual(self.__repo.get_note_disciplina(3), [self.__nota1, self.__nota2, self.__nota6])

    def test_modifica_nota(self):
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.assertEqual(self.__repo.get_valoare_nota(self.__nota1), 7.6)
        self.__repo.modifica_nota(self.__nota1, 7.8)
        self.assertEqual(self.__repo.get_valoare_nota(self.__nota1), 7.8)
        with self.assertRaises(ValueError) as ve:
            self.__repo.modifica_nota(self.__nota2, -6)
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")
        self.assertEqual(self.__repo.get_valoare_nota(self.__nota1), 7.8)
        with self.assertRaises(ValueError) as ve:
            self.__repo.modifica_nota(self.__nota6, 5)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__repo.get_valoare_nota(self.__nota6)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")

    def test_get_nota_from_id(self):
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.assertEqual(self.__repo.get_nota_from_id(11), self.__nota1)
        with self.assertRaises(ValueError) as ve:
            self.__repo.get_nota_from_id(9)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")
        with self.assertRaises(ValueError) as ve:
            self.__repo.get_nota_from_id(-9)
        self.assertEqual(str(ve.exception), "ID nota invalid!")

    def test_get_id_student_nota(self):
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.assertEqual(self.__repo.get_id_student_nota(self.__nota1), 4)
        with self.assertRaises(ValueError) as ve:
            self.__repo.get_id_student_nota(self.__nota6)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")

    def test_get_id_disciplina_nota(self):
        self.__repo.adauga_nota(self.__nota1)
        self.__repo.adauga_nota(self.__nota2)
        self.assertEqual(self.__repo.get_id_disciplina_nota(self.__nota1), 3)
        with self.assertRaises(ValueError) as ve:
            self.__repo.get_id_disciplina_nota(self.__nota6)
        self.assertEqual(str(ve.exception), "Nota inexistenta!")


def suita_repository_file():
    test_suita_repository_file = unittest.TestSuite()
    test_suita_repository_file.addTest(unittest.makeSuite(TestRepositoryFileStudenti))
    test_suita_repository_file.addTest(unittest.makeSuite(TestRepositoryFileDiscipline))
    test_suita_repository_file.addTest(unittest.makeSuite(TestRepositoryFileNote))
    return test_suita_repository_file
