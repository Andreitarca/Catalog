import unittest

from domain.discipline import Disciplina
from domain.note import Nota
from domain.studenti import Student
from validating.alte_validari import AlteValidari
from validating.validari_domeniu import StudentValidator, DisciplinaValidator, NoteValidator


class TestAlteValidari(unittest.TestCase):
    def setUp(self) -> None:
        self.__validari = AlteValidari()

    def test_validare_id(self):
        self.__validari.validare_id(5)
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare_id(-3)
        self.assertEqual(str(ve.exception), "ID invalid!")

    def test_validare_nume(self):
        self.__validari.validare_nume("Marius")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare_nume("")
        self.assertEqual(str(ve.exception), "String vid!")

    def test_validare_nota(self):
        self.__validari.validare_valoare_nota(5.6)
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare_valoare_nota(-3)
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare_valoare_nota(14)
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")


class TestValidareStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.__validari = StudentValidator()
        self.__student1 = Student(4, "Andrei")
        self.__student2 = Student(-3, "Hagi")
        self.__student3 = Student(3, "")
        self.__student4 = Student(-2, "")

    def test_validare_student_bun(self):
        self.__validari.validare(self.__student1)

    def test_validare_student(self):
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__student2)
        self.assertEqual(str(ve.exception), "ID student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__student3)
        self.assertEqual(str(ve.exception), "Nume student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__student4)
        self.assertEqual(str(ve.exception), "ID student invalid!\nNume student invalid!")


class TestValidareDisciplina(unittest.TestCase):
    def setUp(self) -> None:
        self.__validari = DisciplinaValidator()
        self.__disciplina1 = Disciplina(6, "Logica", "Gilius")
        self.__disciplina2 = Disciplina(-3, "Mate", "Gabriel")
        self.__disciplina3 = Disciplina(3, "", "Mihai")
        self.__disciplina4 = Disciplina(4, "Mate", "")
        self.__disciplina5 = Disciplina(-2, "", "")

    def test_validare_disciplina_buna(self):
        self.__validari.validare(self.__disciplina1)

    def test_validare_disciplina(self):
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__disciplina2)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__disciplina3)
        self.assertEqual(str(ve.exception), "Nume disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__disciplina4)
        self.assertEqual(str(ve.exception), "Nume profesor invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__disciplina5)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!\nNume disciplina invalid!\nNume profesor invalid!")


class TestValidareNota(unittest.TestCase):
    def setUp(self) -> None:
        self.__validari = NoteValidator()
        #self.__student1 = Student(4, "Andrei")
        #self.__student2 = Student(-3, "Marian")
        #self.__disciplina1 = Disciplina(5, "Analiza", "Monica")
        #self.__disciplina2 = Disciplina(-6, "", "Gilius")
        self.__nota1 = Nota(11, 4, 5, 7.8)
        self.__nota2 = Nota(12, -3, 5, 6.8)
        self.__nota3 = Nota(11, 4, -6, 9.4)
        self.__nota4 = Nota(13, 4, 5, -3.4)
        self.__nota5 = Nota(-1, -3, 5, 13)

    def test_validare_nota_buna(self):
        self.__validari.validare(self.__nota1)

    def test_validare_nota(self):
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__nota2)
        self.assertEqual(str(ve.exception), "ID student invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__nota3)
        self.assertEqual(str(ve.exception), "ID disciplina invalid!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__nota4)
        self.assertEqual(str(ve.exception), "Valoare nota invalida!")
        with self.assertRaises(ValueError) as ve:
            self.__validari.validare(self.__nota5)
        self.assertEqual(str(ve.exception), "ID nota invalid!\nID student invalid!\nValoare nota invalida!")


def suita_validari():
    test_suite_validari = unittest.TestSuite()
    test_suite_validari.addTest(unittest.makeSuite(TestAlteValidari))
    test_suite_validari.addTest(unittest.makeSuite(TestValidareStudent))
    test_suite_validari.addTest(unittest.makeSuite(TestValidareDisciplina))
    test_suite_validari.addTest(unittest.makeSuite(TestValidareNota))
    return test_suite_validari
