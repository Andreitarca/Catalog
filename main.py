"""Problema 1 cu catalogul de studenti"""
from console.console import Console
from controller.controller_discipline import ManageDiscipline
from controller.controller_note import ManageNote
from controller.controller_studenti import ManageStudenti
from repository.repository_discipline import ListaDiscipline
from repository.repository_file_discipline import ListaDisciplineFile
from repository.repository_file_note import ListaNoteFile
from repository.repository_file_studenti import ListaStudentiFile
from repository.repository_note import ListaNote
from repository.repository_studenti import ListaStudenti
from testing.teste_generale import ruleaza_toate_testele
from validating.validari_domeniu import StudentValidator, DisciplinaValidator, NoteValidator


def main():
    ruleaza_toate_testele()

    #repository_studenti = ListaStudenti()
    repository_file_studenti = ListaStudentiFile("files_repository/repo_studenti.txt")
    validare_studenti = StudentValidator()
    serviciu_studenti = ManageStudenti(repository_file_studenti, validare_studenti)

    #repository_discipline = ListaDiscipline()
    repository_file_discipline = ListaDisciplineFile("files_repository/repo_discipline.txt")
    validare_discipline = DisciplinaValidator()
    serviciu_discipline = ManageDiscipline(repository_file_discipline, validare_discipline)

    #repository_note = ListaNote()
    repository_file_note = ListaNoteFile("files_repository/repo_note.txt")
    validare_note = NoteValidator()
    serviciu_note = ManageNote(repository_file_note, validare_note, repository_file_studenti, repository_file_discipline)

    consola = Console(serviciu_studenti, serviciu_discipline, serviciu_note)
    consola.start()


main()
