from controller.controller_discipline import ManageDiscipline
from controller.controller_note import ManageNote
from controller.controller_studenti import ManageStudenti
from domain.discipline import Disciplina
from domain.studenti import Student
from repository.repository_discipline import ListaDiscipline
from repository.repository_note import ListaNote
from repository.repository_studenti import ListaStudenti
from validating.validari_domeniu import StudentValidator, DisciplinaValidator, NoteValidator


def teste_controller_studenti():
    rep_stud = ListaStudenti()
    validator_stud = StudentValidator()
    manage_stud = ManageStudenti(rep_stud, validator_stud)
    assert manage_stud.get_nr_studenti_service() == 0
    manage_stud.adauga_student_service([4, "Andrei"])
    assert manage_stud.get_nr_studenti_service() == 1
    manage_stud.adauga_student_service(["George"])
    assert manage_stud.get_nr_studenti_service() == 2
    try:
        manage_stud.adauga_student_service([4, "Ilie"])
        assert False
    except ValueError as ve:
        assert str(ve) == "Student existent!"
    try:
        manage_stud.adauga_student_service([-4, ""])
        assert False
    except ValueError as ve:
        assert str(ve) == "ID student invalid!\nNume student invalid!"

    manage_stud.sterge_student_id_service([4])
    assert manage_stud.get_nr_studenti_service() == 1
    try:
        manage_stud.sterge_student_id_service([4])
        assert False
    except ValueError as ve:
        assert str(ve) == "Student inexistent!"

    manage_stud.adauga_student_service([5, "Andrei"])
    manage_stud.modifica_nume_student_id_service([5, "Laurentiu"])
    assert manage_stud.get_nume_student_id_service(5) == "Laurentiu"
    try:
        manage_stud.modifica_nume_student_id_service([2, "Test"])
        assert False
    except ValueError as ve:
        assert str(ve) == "Student inexistent!"
    try:
        manage_stud.modifica_nume_student_id_service([5, ""])
        assert False
    except ValueError as ve:
        assert str(ve) == "Nume student invalid!"
    try:
        manage_stud.modifica_nume_student_id_service([-4, "nume"])
    except ValueError as ve:
        assert str(ve) == "ID student invalid!"


def teste_controller_discipline():
    rep_disc = ListaDiscipline()
    validator_disc = DisciplinaValidator()
    manage_disc = ManageDiscipline(rep_disc, validator_disc)
    assert manage_disc.get_nr_discipline_service() == 0
    manage_disc.adauga_disciplina_service([5, "Analiza matematica", "Muresan"])
    assert manage_disc.get_nr_discipline_service() == 1
    manage_disc.adauga_disciplina_service([18, "Algebra matematica", "Ionut"])
    assert manage_disc.get_nr_discipline_service() == 2
    try:
        manage_disc.adauga_disciplina_service([5, "Info", "Gelu"])
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina existenta!"
    try:
        manage_disc.adauga_disciplina_service([-4, "", ""])
        assert False
    except ValueError as ve:
        assert str(ve) == "ID disciplina invalid!\nNume disciplina invalid!\nNume profesor invalid!"

    manage_disc.sterge_disciplina_id_service([5])
    assert manage_disc.get_nr_discipline_service() == 1
    try:
        manage_disc.sterge_disciplina_id_service([2])
        assert False
    except ValueError as ve:
        assert str(ve) == "Disciplina inexistenta!"

    manage_disc.adauga_disciplina_service([13, "OOP", "Prof OP"])
    manage_disc.adauga_disciplina_service([15, "Metode avansate", "Best prof"])
    assert manage_disc.get_nume_disciplina_id_service(13) == "OOP"
    assert manage_disc.get_profesor_disciplina_id_service(15) == "Best prof"
    manage_disc.modifica_disciplina_id_service([15, "nume: MAPRPMI", "prof: Gabi"])
    assert manage_disc.get_nume_disciplina_id_service(15) == "MAPRPMI"
    assert manage_disc.get_profesor_disciplina_id_service(15) == "Gabi"
    try:
        manage_disc.modifica_disciplina_id_service(["nume: test"])
        assert False
    except ValueError as ve:
        assert str(ve) == "Numar parametri invalid!"
    try:
        manage_disc.modifica_disciplina_id_service([-3, "nume: test", "prof: Profesor"])
        assert False
    except ValueError as ve:
        assert str(ve) == "ID disciplina invalid!"
    try:
        manage_disc.modifica_disciplina_id_service([15, "num: MAPRPMI", "prof: Gabi"])
    except ValueError as ve:
        assert str(ve) == "Comanda invalida!"
    manage_disc.modifica_disciplina_id_service([15, "prof: Mircea"])
    assert manage_disc.get_profesor_disciplina_id_service(15) == "Mircea"

    manage_disc.adauga_disciplina_service([10, "Analiza matematica", "Eugen"])
    manage_disc.adauga_disciplina_service([16, "Geometrie MateMatica", "Cornel"])
    assert manage_disc.cauta_discipline_service(["nume: MATE"]) == [18, 10, 16]
    try:
        manage_disc.cauta_discipline_service(["nume test"])
    except ValueError as ve:
        assert str(ve) == "Comanda invalida!"
    assert manage_disc.cauta_discipline_service(["prof: o"]) == [18, 13, 16]
    assert manage_disc.cauta_discipline_service(["prof: Maria"]) == []
    assert manage_disc.cauta_discipline_service(["nume: Mate", "prof:   o"]) == [18, 16]


def teste_controller_note():
    repo_stud = ListaStudenti()
    repo_disc = ListaDiscipline()
    validator_note = NoteValidator()
    repo_note = ListaNote()
    manage_note = ManageNote(repo_note, validator_note, repo_stud, repo_disc)

    assert manage_note.get_nr_note_service() == 0
    Stud1 = Student(6, "Andrei")
    Stud2 = Student(7, "Dorian")
    Disc6 = Disciplina(31, "Matematica speciala", "Moldo Iulius")
    Disc8 = Disciplina(17, "maTematica analiza", "Muresan")
    repo_stud.adauga_student(Stud2)
    repo_stud.adauga_student(Stud1)
    repo_disc.adauga_disciplina(Disc6)
    repo_disc.adauga_disciplina(Disc8)
    manage_note.adauga_nota_service([12, 6, 31, 9.7])
    assert manage_note.get_nr_note_service() == 1
    try:
        manage_note.adauga_nota_service([31, 4, 31, 9.7])
        assert False
    except ValueError as ve:
        assert str(ve) == "Student inexistent!"
    manage_note.adauga_nota_service([34, 6, 17, 8.4])
    manage_note.adauga_nota_service([36, 7, 17, 7.67])
    manage_note.adauga_nota_service([38, 7, 31, 5.6])
    assert manage_note.get_nr_note_service() == 4
    manage_note.sterge_nota_id_service(34)
    assert manage_note.get_nr_note_service() == 3
    try:
        manage_note.sterge_nota_id_service(7)
        assert False
    except ValueError as ve:
        assert str(ve) == "Nota inexistenta!"
    manage_note.adauga_nota_service([34, 6, 17, 8.4])
    assert manage_note.get_nr_note_service() == 4
    manage_note.sterge_student_si_notele_sale_service(6)
    assert manage_note.get_nr_note_service() == 2
    repo_stud.adauga_student(Stud1)
    manage_note.adauga_nota_service([34, 6, 17, 8.4])
    manage_note.adauga_nota_service([12,  6, 31, 9.7])
    assert manage_note.get_nr_note_service() == 4
    manage_note.sterge_disciplina_si_note_service(17)
    assert manage_note.get_nr_note_service() == 2

    repo_disc.adauga_disciplina(Disc8)
    manage_note.adauga_nota_service([34, 6, 17, 8.4])
    manage_note.adauga_nota_service([36, 7, 17, 7.67])
    assert manage_note.get_valoare_nota_id_service(34) == 8.4
    manage_note.modifica_valoare_nota_service(34, 8.94)
    assert manage_note.get_valoare_nota_id_service(34) == 8.94
    try:
        manage_note.modifica_valoare_nota_service(-1, 100)
        assert False
    except ValueError as ve:
        assert str(ve) == "ID nota invalid!\nValoare nota invalida!"
    try:
        manage_note.modifica_valoare_nota_service(50, 9.5)
        assert False
    except ValueError as ve:
        assert str(ve) == "Nota inexistenta!"


def ruleaza_toate_testele_controller():
    teste_controller_studenti()
    teste_controller_discipline()
    teste_controller_note()
