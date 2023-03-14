from domain.note import Nota
from repository.repository_note import ListaNote
from sortari.sortare_principala import sortare


def teste_sortari():
    repo = ListaNote()
    nota1 = Nota(11, 4, 3, 7.6)
    nota2 = Nota(12, 5, 3, 5.69)
    nota4 = Nota(13, 5, 3, 9.3)
    nota6 = Nota(16, 5, 3, 9.3)
    nota7 = Nota(17, 5, 4, 9.3)
    repo.adauga_nota(nota1)
    repo.adauga_nota(nota2)
    repo.adauga_nota(nota4)
    repo.adauga_nota(nota6)
    repo.adauga_nota(nota7)
    lista = repo.getlista()
    lista = list(lista.values())
    lista_noua = sortare(lista, key=lambda x: (x.getnota(), x.getid()), nume_sortare="Shake_Sort", reverse=True)
    assert lista_noua == [nota7, nota6, nota4, nota1, nota2]
    lista_noua = sortare(lista, key=lambda x: (x.getnota(), x.getid()), nume_sortare="Shake_Sort")
    assert lista_noua == [nota2, nota1, nota4, nota6, nota7]
    lista_noua = sortare(lista, key=lambda x: (x.getnota(), x.getid()), nume_sortare="Selection_Sort", reverse=True)
    assert lista_noua == [nota7, nota6, nota4, nota1, nota2]
    lista_noua = sortare(lista, key=lambda x: (x.getnota(), x.getid()), nume_sortare="Selection_Sort")
    assert lista_noua == [nota2, nota1, nota4, nota6, nota7]
