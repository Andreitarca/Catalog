import unittest
from domain.discipline import Disciplina
from domain.note import Nota
from domain.sefpromotie import SefPromotieDTO
from domain.studenti import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.__student1 = Student(4, "Andrei")
        self.__student2 = Student(5, "Marian")
        self.__student3 = Student(4, "Gigel")

    def test_getid(self):
        self.assertEqual(self.__student1.getid(), 4, "The ID of the student should be 4")

    def test_genume(self):
        self.assertEqual(self.__student1.getnume(), "Andrei", "The name of the student should be 'Andrei'")

    def test_setnume(self):
        self.assertEqual(self.__student1.getnume(), "Andrei", "The name of the student should be 'Andrei'")
        self.__student1.setnume("Ioan")
        self.assertEqual(self.__student1.getnume(), "Ioan", "The name of the student should be 'Ioan'")

    def test_equally(self):
        self.assertEqual(self.__student1, self.__student3, "Should be the same")
        self.assertNotEqual(self.__student1, self.__student2, "Shoud be different")

    def test_print(self):
        self.assertEqual(self.__student1.__str__(), "Student cu ID-ul [4] si cu numele 'Andrei'")

    def test_nr_inst(self):
        self.assertGreater(self.__student1.get_no_inst(), 1)


class TestDisciplina(unittest.TestCase):
    def setUp(self) -> None:
        self.__disciplina1 = Disciplina(5, "Analiza", "Monica")
        self.__disciplina2 = Disciplina(6, "Logica", "Gilius")
        self.__disciplina3 = Disciplina(5, "Algebra", "Eugen")

    def test_getid(self):
        self.assertEqual(self.__disciplina1.getid(), 5)
        self.assertEqual(self.__disciplina2.getid(), 6)

    def test_getnume(self):
        self.assertEqual(self.__disciplina1.getnume(), "Analiza")
        self.assertEqual(self.__disciplina2.getnume(), "Logica")

    def test_getprof(self):
        self.assertEqual(self.__disciplina1.getprof(), "Monica")
        self.assertEqual(self.__disciplina2.getprof(), "Gilius")

    def test_setnume(self):
        self.assertEqual(self.__disciplina1.getnume(), "Analiza")
        self.__disciplina1.setnume("Analiza matematica")
        self.assertEqual(self.__disciplina1.getnume(), "Analiza matematica")

    def test_setprof(self):
        self.assertEqual(self.__disciplina1.getprof(), "Monica")
        self.__disciplina1.setprof("Izg Monica")
        self.assertEqual(self.__disciplina1.getprof(), "Izg Monica")

    def test_equally(self):
        self.assertEqual(self.__disciplina1, self.__disciplina3)
        self.assertNotEqual(self.__disciplina1, self.__disciplina2)

    def test_print(self):
        self.assertEqual(self.__disciplina1.__str__(),
                         "Disciplina cu ID-ul [5], numele 'Analiza' cu profesorul 'Monica'")

    def test_nr_inst(self):
        self.assertGreater(self.__disciplina1.get_no_inst(), 1)


class TestNota(unittest.TestCase):
    def setUp(self) -> None:
        #Student(4, "Andrei")
        #Student(5, "Marian")
        #Disciplina(5, "Analiza", "Monica")
        #Disciplina(6, "Logica", "Gilius")
        self.__nota1 = Nota(11, 4, 5, 7.8)
        self.__nota2 = Nota(12, 5, 5, 6.8)
        self.__nota3 = Nota(11, 4, 6, 9.4)

    def test_getid(self):
        self.assertEqual(self.__nota1.getid(), 11)

    def test_getnota(self):
        self.assertEqual(self.__nota2.getnota(), 6.8)

    def test_getstudent(self):
        self.assertEqual(self.__nota1.getid_student(), 4)

    def test_getdisciplina(self):
        self.assertEqual(self.__nota2.getid_disciplina(), 5)

    def test_setnota(self):
        self.assertEqual(self.__nota3.getnota(), 9.4)
        self.__nota3.setnota(9.6)
        self.assertEqual(self.__nota3.getnota(), 9.6)

    def test_equally(self):
        self.assertEqual(self.__nota1, self.__nota3)
        self.assertNotEqual(self.__nota1, self.__nota2)

    def test_greater(self):
        self.assertGreater(self.__nota1, self.__nota2)

    def test_less(self):
        self.assertLess(self.__nota1, self.__nota3)

    def test_print(self):
        self.assertEqual(self.__nota1.__str__(), "Nota cu ID-ul [11] si valoarea 7.8 atribuita "
                                                 "studentului cu ID-ul [4] la disciplina cu ID-ul [5]")

    def test_nr_inst(self):
        self.assertGreater(self.__nota1.get_no_inst(), 1)


class TestSefPromotie(unittest.TestCase):
    def setUp(self) -> None:
        self.__sef_promotie1 = SefPromotieDTO(4, "Andrei", 8.7)
        self.__sef_promotie2 = SefPromotieDTO(6, "Ioan", 9.53)

    def test_getid(self):
        self.assertEqual(self.__sef_promotie1.getid(), 4)

    def test_getnume(self):
        self.assertEqual(self.__sef_promotie2.getnume(), "Ioan")

    def test_getmedia(self):
        self.assertEqual(self.__sef_promotie1.getmedia(), 8.7)

    def test_print(self):
        self.assertEqual(self.__sef_promotie2.__str__(), "Student cu ID-ul [6] si numele 'Ioan' cu media 9.53")


def suita_domeniu():
    test_suita_domeniu = unittest.TestSuite()
    test_suita_domeniu.addTest(unittest.makeSuite(TestStudent))
    test_suita_domeniu.addTest(unittest.makeSuite(TestDisciplina))
    test_suita_domeniu.addTest(unittest.makeSuite(TestNota))
    test_suita_domeniu.addTest(unittest.makeSuite(TestSefPromotie))
    return test_suita_domeniu
