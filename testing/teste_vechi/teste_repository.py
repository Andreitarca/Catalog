from domain.discipline import Disciplina
from domain.note import Nota
from domain.studenti import Student
from repository.repository_discipline import ListaDiscipline
from repository.repository_note import ListaNote
from repository.repository_studenti import ListaStudenti


def teste_lista_studenti():
    lista_1 = ListaStudenti()
    assert lista_1.getlista() == {}
    assert lista_1.getlenlista() == 0
    Stud1 = Student(6, "Andrei")
    Stud2 = Student(7, "Dorian")
    Stud3 = Student(8, "Ioana")
    Stud4 = Student(6, "Mircea")
    Stud5 = Student(10, "Cezar")
    lista_1.adauga_student(Stud1)
    lista_1.adauga_student(Stud2)
    lista_1.adauga_student(Stud3)
    assert lista_1.getlenlista() == 3
    try:
        lista_1.adauga_student(Stud4)
        assert False
    except ValueError as ve:
        assert str(ve) == "Student existent!"
    assert lista_1.getlenlista() == 3

    assert lista_1.get_nume_student(Stud1) == "Andrei"
    lista_1.modifica_nume_student(Stud1, "Vasile")
    assert lista_1.get_nume_student(Stud1) == "Vasile"
    try:
        lista_1.modifica_nume_student(Stud5, "Idk")
        assert False
    except ValueError as ve:
        assert str(ve) == "Student inexistent!"
    try:
        lista_1.modifica_nume_student(Stud1, "")
        assert False
    except ValueError as ve:
        assert str(ve) == "Nume student invalid!"
    assert lista_1.getlenlista() == 3

    lista_1.sterge_student(Stud3)
    assert lista_1.getlenlista() == 2
    try:
        lista_1.sterge_student(Stud5)
        assert False
    except ValueError as ve:
        assert str(ve) == "Student inexistent!"


def teste_lista_discipline():
    lista_1 = ListaDiscipline()
    assert lista_1.getlista() == {}
    assert lista_1.getlenlista() == 0
    Disc1 = Disciplina(7, "Logica", "Profa de logica")
    Disc2 = Disciplina(9, "Programare", "Profu de fp")
    Disc3 = Disciplina(10, "Pedagogic", "Psiholog")
    Disc5 = Disciplina(3, "Istorie", "Moldo")
    lista_1.adauga_disciplina(Disc1)
    lista_1.adauga_disciplina(Disc2)
    lista_1.adauga_disciplina(Disc3)
    assert lista_1.getlenlista() == 3
    Disc4 = Disciplina(9, "Algebra", "Profu")
    try:
        lista_1.adauga_disciplina(Disc4)
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina existenta!"
    assert lista_1.getlenlista() == 3

    assert lista_1.get_nume_disciplina(Disc1) == "Logica"
    lista_1.modifica_nume_disciplina(Disc1, "Logica computationala")
    assert lista_1.get_nume_disciplina(Disc1) == "Logica computationala"
    try:
        lista_1.modifica_nume_disciplina(Disc5, "Idk")
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina inexistenta!"
    assert lista_1.getlenlista() == 3

    lista_1.sterge_disciplina(Disc3)
    assert lista_1.getlenlista() == 2
    try:
        lista_1.sterge_disciplina(Disc5)
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina inexistenta!"

    assert lista_1.get_prof_disciplina(Disc1) == "Profa de logica"
    try:
        lista_1.get_prof_disciplina(Disc5)
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina inexistenta!"

    lista_1.modifica_profesor_disciplina(Disc2, "Muresan")

    assert lista_1.get_prof_disciplina(Disc2) == "Muresan"
    try:
        lista_1.modifica_profesor_disciplina(Disc5, "Test")
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina inexistenta!"

    try:
        lista_1.modifica_nume_disciplina(Disc1, "")
        assert False
    except ValueError as ve:
        assert str(ve) == "Nume disciplina invalid!"

    try:
        lista_1.modifica_profesor_disciplina(Disc1, "")
        assert False
    except ValueError as ve:
        assert str(ve) == "Nume profesor invalid!"

    Disc6 = Disciplina(31, "Matematica speciala", "Moldo Iulius")
    Disc7 = Disciplina(13, "Matematica algebra", "Moldo Cesarus")
    Disc8 = Disciplina(17, "maTematica analiza", "Muresan")
    lista_1.adauga_disciplina(Disc6)
    lista_1.adauga_disciplina(Disc7)
    lista_1.adauga_disciplina(Disc8)
    lista_1.adauga_disciplina(Disc5)


def teste_lista_note():
    Disc6 = Disciplina(31, "Matematica speciala", "Moldo Iulius")
    Disc7 = Disciplina(13, "Matematica algebra", "Moldo Cesarus")
    Disc8 = Disciplina(17, "maTematica analiza", "Muresan")
    Stud1 = Student(6, "Andrei")
    Stud2 = Student(7, "Dorian")
    Stud3 = Student(8, "Ioana")
    Stud5 = Student(10, "Cezar")
    list = ListaNote()
    assert list.getlenlista() == 0
    assert list.getlista() == {}
    Nota1 = Nota(11, Stud1, Disc6, 8.7)
    Nota2 = Nota(14, Stud2, Disc7, 9.4)
    Nota3 = Nota(14, Stud5, Disc8, 6.7)
    Nota4 = Nota(12, Stud1, Disc7, 8.4)
    Nota5 = Nota(17, Stud2, Disc6, 7.8)
    list.adauga_nota(Nota1)
    list.adauga_nota(Nota2)
    list.adauga_nota(Nota4)
    list.adauga_nota(Nota5)
    assert list.getlenlista() == 4
    try:
        list.adauga_nota(Nota3)
        assert False
    except ValueError as ve:
        assert str(ve) == "Nota existenta!"
    list.sterge_nota(Nota1)
    assert list.getlenlista() == 3
    try:
        list.sterge_nota(Nota1)
        assert False
    except ValueError as ve:
        assert str(ve) == "Nota inexistenta!"
    assert list.get_valoare_nota(Nota2) == 9.4

    list.modifica_nota(Nota2, 5)
    assert list.get_valoare_nota(Nota2) == 5
    assert list.get_id_student_nota(Nota2) == 7
    assert list.get_id_disciplina_nota(Nota2) == 13

    assert list.getlenlista() == 3
    list.sterge_note_student(Stud2)
    assert list.getlenlista() == 1
    list.adauga_nota(Nota2)
    list.adauga_nota(Nota5)
    assert list.getlenlista() == 3
    list.sterge_note_disciplina(Disc7)
    assert list.getlenlista() == 1


def ruleaza_toate_testele_repository():
    teste_lista_studenti()
    teste_lista_discipline()
    teste_lista_note()
