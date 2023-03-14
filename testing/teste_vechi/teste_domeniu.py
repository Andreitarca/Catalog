from domain.discipline import Disciplina
from domain.note import Nota
from domain.studenti import Student
from validating.validari_domeniu import StudentValidator, DisciplinaValidator, NoteValidator


def teste_studenti():
    student_validator = StudentValidator()
    Stud1 = Student(6, "Andrei")
    assert Stud1.getid() == 6
    assert Stud1.getnume() == "Andrei"
    student_validator.validare(Stud1)
    Stud1.setnume("Ioan")
    assert Stud1.getnume() == "Ioan"
    Stud1e = Student(6, "George")
    assert Stud1e == Stud1

    Stud2gr = Student(-4, "")
    try:
        student_validator.validare(Stud2gr)
        assert False
    except ValueError as ve:
        assert (str(ve) == "ID student invalid!\nNume student invalid!")


def teste_discipline():
    disciplina_validator = DisciplinaValidator()
    Disc1 = Disciplina(4, "Analiza", "Viorel")
    assert Disc1.getid() == 4
    assert Disc1.getnume() == "Analiza"
    assert Disc1.getprof() == "Viorel"
    disciplina_validator.validare(Disc1)
    Disc1.setprof("Adrian")
    Disc1.setnume("Analiza matematica")
    assert Disc1.getnume() == "Analiza matematica"
    assert Disc1.getprof() == "Adrian"
    Disc1e = Disciplina(4, "Algebra", "Matei")
    assert Disc1 == Disc1e

    Disc2gr = Disciplina(-1, "", "")
    try:
        disciplina_validator.validare(Disc2gr)
        assert False
    except ValueError as ve:
        assert (str(ve) == "ID disciplina invalid!\nNume disciplina invalid!\nNume profesor invalid!")


def teste_note():
    note_validator = NoteValidator()
    Stud1 = Student(6, "Andrei")
    Stud2 = Student(9, "Ghita")
    Disc1 = Disciplina(4, "Analiza", "Viorel")
    Disc2 = Disciplina(7, "Algebra", "Gheorghe")
    Nota1 = Nota(5, Stud1, Disc1, 9.56)
    Nota1e = Nota(5, Stud2, Disc2, 8.5)
    Nota2 = Nota(8, Stud2, Disc2, 8.8)
    assert Nota1.getid() == 5
    assert Nota1.getnota() == 9.56
    assert Nota1.getdisciplina() == Disc1
    assert Nota1.getstudent() == Stud1
    note_validator.validare(Nota1)
    Nota1.setnota(9.8)
    assert Nota1.getnota() == 9.8
    assert Nota1 == Nota1e
    assert Nota1 > Nota2
    assert Nota2 < Nota1

    Nota2gr = Nota(-4, Stud1, Disc1, 8)
    try:
        note_validator.validare(Nota2gr)
        assert False
    except ValueError as ve:
        assert str(ve) == "ID nota invalid!"
    Nota3gr = Nota(10, Stud1, Disc1, 11)
    try:
        note_validator.validare(Nota3gr)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoare nota invalida!"


def ruleaza_toate_testele_domeniu():
    teste_studenti()
    teste_discipline()
    teste_note()
