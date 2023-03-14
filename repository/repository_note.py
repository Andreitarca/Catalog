from alte_functii.recursivitate import cauta, sterge_note
from validating.alte_validari import AlteValidari
from validating.validari_domeniu import NoteValidator


class ListaNote:
    """
    clasa ListaNote ne adauga si manageriaza notele unui student la o disciplina
    """

    def __init__(self):
        """
        un obiect de tipul ListaNote este format dintr-un dictionar
        """
        self._lista = {}

    def getlista(self):
        """
        este returnata lungimea listei de obiecte Nota
        :return: lungimea listei de obiecte Nota
        """
        return self._lista

    def getlenlista(self):
        """
        este returnata lista de Note
        :return: dictionar care contine obiectele Note
        """
        return len(self._lista)

    def adauga_nota(self, nota):
        """
        se adauga o nota la dictionarul curent de note
        :param nota: obiect de tipul Nota
        :return: -
        :raises:    ValueError cu mesajul "Nota existenta!" daca exista deja o nota cu acelasi id in lista
                    ValueError daca datele din nota sunt invalide:
                            daca notaID < 0 sau daca notaID nu este intreg -> "ID invalid\n"
                            daca studentul este invalid -> "Student invalid!\n"
                            daca disciplina este invalida -> Disciplina invalida!\n"
                            daca valoarea este invalida (nu e cuprinsa intre 1 si 10) -> "Nota invalida!\n"
        """
        validare = NoteValidator()
        try:
            validare.validare(nota)
        except ValueError as ve:
            raise ValueError(ve)
        lista_chei = list(self._lista.keys())
        se_afla = cauta(lista_chei, nota.getid())
        if se_afla:
            raise ValueError("Nota existenta!")
        self._lista[nota.getid()] = nota

    def sterge_nota(self, nota):
        """
        sterge obiectul de tip nota din dictionarul de obiecte note
        :param nota: obiect de tip nota
        :return: -
        :raises:    ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        try:
            del self._lista[nota.getid()]
        except KeyError:
            raise ValueError("Nota inexistenta!")

    def sterge_note_student(self, id_stud):
        """
        sterge toate obiectele de tip nota ale id_studentului id_stud din dictionarul de obiecte note
        :param id_stud: obiect de tip id_student
        :return: -
        :raises: -
        """
        # dictionar = {}
        # for key in self._lista:
        #     if self._lista[key].getid_student() != id_stud:
        #         dictionar[key] = self._lista[key]
        dictionar = sterge_note(list(self._lista.values()), id_stud, key=lambda x: x.getid_student())
        self._lista = dictionar

    def sterge_note_disciplina(self, id_disc):
        """
        sterge toate obiectele de tip nota la disciplina disc din dictionarul de obiecte note
        :param disc: obiect de tip Disciplina
        :return: -
        :raises: -
        """
        # dictionar = {}
        # for key in self._lista:
        #     if self._lista[key].getid_disciplina() != id_disc:
        #         dictionar[key] = self._lista[key]
        dictionar = sterge_note(list(self._lista.values()), id_disc, key=lambda x: x.getid_disciplina())
        self._lista = dictionar

    def get_note_disciplina(self, iddisc):
        """
        returneaza toate obiectele de tip nota la disciplina disc din dictionarul de obiecte note
        :param disc: obiect de tip Disciplina
        :return: lista de obiecte
        :raises: -
        """
        list = []
        for key in self._lista:
            if self._lista[key].getid_disciplina() == iddisc:
                list.append(self._lista[key])
        return list

    def modifica_nota(self, nota, val_noua):
        """
        modifica valoarea obiectului de tip Nota aflata in dictionar
        :param nota: obiect de tip Nota
        :param val_noua: float cuprins intre 1 si 10
        :return: -
        :raises: ValueError cu mesajul "Nota inexistent!" daca nu exista aceasta disciplina in dictionar
                                       "Nota invalida!" daca val_noua nu este un float cuprins intre 1 si 10
        """
        alte_validari = AlteValidari()
        try:
            alte_validari.validare_valoare_nota(val_noua)
        except ValueError as ve:
            raise ValueError(ve)
        if nota.getid() in self._lista:
            self._lista.pop(nota.getid())
            nota.setnota(val_noua)
            self._lista[nota.getid()] = nota
        else:
            raise ValueError("Nota inexistenta!")

    def get_valoare_nota(self, nota):
        """
        returneaza valoarea notei obiectului de tip nota aflat in dictionar
        :param nota: obiect de tip nota
        :return: float - valoarea notei
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        if nota.getid() in self._lista:
            return nota.getnota()
        else:
            raise ValueError("Nota inexistenta!")

    def get_nota_from_id(self, idn):
        """
        returneaza obiectul de tip nota aflat in dictionar cu id-ul idn
        :param idn: id-ul notei
        :return: obiect de tipul Nota
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista acest id de nota in dictionar
        """
        validare = AlteValidari()
        try:
            validare.validare_id(idn)
        except ValueError:
            raise ValueError("ID nota invalid!")
        if idn in self._lista:
            return self._lista[idn]
        raise ValueError("Nota inexistenta!")

    def get_id_student_nota(self, nota):
        """
        returneaza id-ul studentul obiectului de tip nota aflat in dictionar
        :param nota: obiect de tip nota
        :return: int id-ul studentului
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        if nota.getid() in self._lista:
            return nota.getid_student()
        else:
            raise ValueError("Nota inexistenta!")

    def get_id_disciplina_nota(self, nota):
        """
        returneaza id-ul disciplinei obiectului de tip nota aflat in dictionar
        :param nota: obiect de tip nota
        :return: int id-ul disciplinei
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        if nota.getid() in self._lista:
            return nota.getid_disciplina()
        else:
            raise ValueError("Nota inexistenta!")

    def del_all(self):
        """
        sterge toate notele
        :return: -
        """
        self._lista = {}

