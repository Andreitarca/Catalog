import copy
import random

from domain.note import Nota
from domain.sefpromotie import SefPromotieDTO
from repository.repository_discipline import ListaDiscipline
from repository.repository_note import ListaNote
from repository.repository_studenti import ListaStudenti
from sortari.sortare_principala import sortare
from validating.alte_validari import AlteValidari


class ManageNote:
    """
    clasa care manageriaza notele, avand un repositor si un validator specifice
    """

    def __init__(self, repository:ListaNote, validator, repository_student:ListaStudenti, repository_disciplina:ListaDiscipline):
        """
        creeaza un manager de note si salveaza datele in repository si le valideaza cu ajutorul validatorului
        :param repository: obiect de tipul ListaNote
        :param validator: obiect de tipul NoteValidator
        :param repository_student: obiect de tipul ListaStudent
        :param repository_disciplina: obiect de tipul ListaDisciplina
        """
        self.__repository = repository
        self.__validator = validator
        self.__repository_student = repository_student
        self.__repository_disciplina = repository_disciplina

    def __make_id_nota(self):
        """
        obtine un nou id pentru o viitoare nota care urmeaza sa fie creata
        :return: id pentru nota
        """
        lista_id = list(self.__repository.getlista().keys())
        lista_id.append(100)
        idn = max(lista_id)
        while self.__exist_id_service(idn):
            idn = idn + 1
        return idn

    def adauga_nota_service(self, params):
        """
        se adauga o nota la lista actuala de discipline stocata in __repository
        :param params: disctionar de parametri care contin datele dupa urmatorul model:
                        1. trei parametri -> primul va fi numele disciplinei, iar al doilea numele profesorului
                        2. patru parametri -> primul va fi id-ul daca nu este deja alocat, iar celelalte 2 ca mai sus
        :return: -
        :raises:  ValueError cu urmatoarele mesaje:
                    "Numar parametri invalid!" daca nu este corect numarul parametrilor
                    "Nota existenta!" daca exista deja un disciplina cu acelasi id in lista
                    ValueError pentru validare:
                        daca notaID < 0 sau daca notaID nu este intreg -> "ID invalid"
                        daca nume == "" -> "Nume disciplina invalid!"
                        daca prof == "" -> "Nume profesor invalid!"
        """
        erori = ""
        validari = AlteValidari()
        if len(params) == 4 or len(params) == 3:
            if len(params) == 4:
                idn = params[0]
                try:
                    validari.validare_id(idn)
                except ValueError:
                    erori += "ID nota invalid!\n"
                id_nota = idn
                j = 1
            else:
                id_nota = self.__make_id_nota()
                j = 0
            try:
                validari.validare_id(params[j])
            except ValueError:
                erori += "ID student invalid!\n"
            id_stud = params[j]
            j = j + 1
            try:
                validari.validare_id(params[j])
            except ValueError:
                erori += "ID disciplina invalid!\n"
            id_disc = params[j]
            j = j + 1
            try:
                validari.validare_valoare_nota(params[j])
            except ValueError:
                erori += "Valoare nota invalida!\n"
            val_nota = params[j]
        else:
            raise ValueError("Numar parametri invalid!")
        if len(erori) > 0:
            raise ValueError(erori[:-1])
        try:
            stud = self.__repository_student.get_stud_from_id(id_stud)
        except ValueError as ve:
            raise ValueError(ve)
        try:
            disc = self.__repository_disciplina.get_disc_from_id(id_disc)
        except ValueError as ve:
            raise ValueError(ve)
        nota_prov = Nota(id_nota, id_stud, id_disc, val_nota)
        try:
            self.__validator.validare(nota_prov)
        except ValueError as ve:
            raise ValueError(ve)
        try:
            self.__repository.adauga_nota(nota_prov)
        except ValueError as ve:
            raise ValueError(ve)

    def __sterge_nota_service(self, nota):
        """
        sterge nota nota din repository
        :param nota: obiect de tip Nota
        :return: -
        :raises ValueError cu mesajul "Nota inexistenta!" daca nu exista nota nota in repository
        """
        try:
            self.__repository.sterge_nota(nota)
        except ValueError as ve:
            raise ValueError(ve)

    def __exist_id_service(self, idp):
        """
        verifica daca exista id-ul ids in dictionarul de obiecte note
        :param idp: id de tip intreg pozitiv
        :return:    True daca exista acest ids in dictionarul de note
                    False daca nu exista acest ids in dictionarul de note
        :raises:    ValueError cu mesajul "ID invalid!" daca nr_id nu poate fi id
        """
        validare = AlteValidari()
        try:
            validare.validare_id(idp)
        except ValueError as ve:
            raise ValueError(ve)
        if idp in self.__repository.getlista():
            return True
        return False

    def sterge_nota_id_service(self, idnota):
        """
        sterge nota cu id-ul primit prin lista de parametri din repository
        :param idnota: id-ul notei
        :type idnota: int pozitiv
        :return: -
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista nota nota cu ids in repository
                                       "ID nota invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        ids = idnota
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError:
            raise ValueError("ID nota invalid!")
        try:
            nota = self.__repository.get_nota_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        self.__sterge_nota_service(nota)

    def sterge_student_si_notele_sale_service(self, id_stud):
        """
        sterge studentul si notele studentului cu id-ul primit prin lista de parametri din repository
        :param params: lista de parametri cu un singur element: id-ul
        :return: -
        :raises: ValueError cu mesajul "Student inexistent!" daca nu exista studentul stud cu ids in repository
                                       "ID student invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        ids = id_stud
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError:
            raise ValueError("ID student invalid!")
        try:
            stud = self.__repository_student.get_stud_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        self.__repository.sterge_note_student(id_stud)
        self.__repository_student.sterge_student(stud)

    def sterge_toti_studentii_si_notele(self):
        """
        sterge toti studentii din lista de studenti si implicit si notele lor
        :return: -
        """
        self.__repository.del_all()
        self.__repository_student.del_all()

    def sterge_toate_disciplinele_si_notele(self):
        """
        sterge toate disciplinele din lista de discipline si implicit si notele la ele
        :return: -
        """
        self.__repository.del_all()
        self.__repository_disciplina.del_all()

    def sterge_toate_notele(self):
        """
        sterge toate notele din lista de note
        :return: -
        """
        self.__repository.del_all()

    def sterge_disciplina_si_note_service(self, id_disc):
        """
        sterge disciplina si notele disciplinei cu id-ul primit prin lista de parametri din repository
        :param params: lista de parametri cu un singur element: id-ul
        :return: -
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista disciplina disc cu ids in repository
                                       "ID disciplina invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        ids = id_disc
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError:
            raise ValueError("ID disciplina invalid!")
        try:
            disc = self.__repository_disciplina.get_disc_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        self.__repository.sterge_note_disciplina(id_disc)
        self.__repository_disciplina.sterge_disciplina(disc)

    def __modifica_valoare_nota_service(self, nota, val_noua):
        """
        modifica valoarea obiectului de tip nota aflat in repository cu numele primit prin parametru
        :param nota: obiect de tipul nota
        :param nume_nou nota: float cuprins intre 1 si 10
        :return: -
        :raises: ValueError cu diferite mesaje:
                        "Nota inexistenta!" daca nu exista nota nota in repository
                        "Nota invalida!" daca val_nou nu este valid
        """
        self.__repository.modifica_nota(nota, val_noua)

    def modifica_valoare_nota_service(self, id_nota, val_noua):
        """
        modifica valoarea obiectului de tip nota cu id-ul din params aflat in repository cu valoarea primit prin params
        :param params: lista de doua elemente; primul este id-ul notei, cel de-al doilea noua sa valoare
        :return: -
        :raises: ValueError cu diferite mesaje:
                        "Nota inexistenta!" daca nu exista studentul stud in repository
                        "Nota invalida!" daca val_noua nu este float intre 1 si 10
                        "ID nota invalid!" daca id-ul introdus nu este intreg pozitiv
                        "Numar parametri invalid!" daca nu sunt doar doua elemente in params
        """
        erori = ""
        validari = AlteValidari()
        ids = id_nota
        val_nou = val_noua
        try:
            validari.validare_id(ids)
        except ValueError:
            erori += "ID nota invalid!\n"
        try:
            validari.validare_valoare_nota(val_nou)
        except ValueError:
            erori += "Valoare nota invalida!\n"
        if len(erori) > 0:
            erori = erori[:-1]
            raise ValueError(erori)
        try:
            nota = self.__repository.get_nota_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        self.__modifica_valoare_nota_service(nota, val_nou)

    def get_valoare_nota_id_service(self, idd):
        """
        returneaza valoarea notei cu id-ul idd daca acesta se afla in repository
        :param idd: id-ul notei
        :return: valoarea notei nota
        :raises: ValueError cu mesajul: "Nota inexistenta!" daca nu exista nota disc in repository
                                        "ID nota invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        validari = AlteValidari()
        try:
            validari.validare_id(idd)
        except ValueError:
            raise ValueError("ID nota invalid!")
        try:
            nota = self.__repository.get_nota_from_id(idd)
        except ValueError as ve:
            raise ValueError(ve)
        return self.__repository.get_valoare_nota(nota)

    def get_all_note_service(self):
        """
        sunt returnate toate obiectele de tip Note din repository
        :return: lista[dictionatul] din repository
        :raises: ValueError cu mesajul "Nu exista nicio nota introdus!" daca lista este goala
        """
        if self.__repository.getlenlista() == 0:
            raise ValueError("Nu exista nicio nota introdusa!")
        else:
            return self.__repository.getlista()

    def get_all_note_string_service(self):
        """
        sunt returnate toate obiectele de tip Note din repository
        :return: lista[dictionatul] din repository
        :raises: ValueError cu mesajul "Nu exista nicio nota introdus!" daca lista este goala
        """
        if self.__repository.getlenlista() == 0:
            raise ValueError("Nu exista nicio nota introdusa!")
        else:
            lista_dict = {}
            for key in self.__repository.getlista():
                nota = self.__repository.getlista()[key]
                id_student = nota.getid_student()
                id_disciplina = nota.getid_disciplina()
                valoare_nota = nota.getnota()
                stud = self.__repository_student.get_stud_from_id(id_student)
                disc = self.__repository_disciplina.get_disc_from_id(id_disciplina)
                lista_dict[key] = f"Nota cu ID-ul [{key}] si valoarea {valoare_nota} atribuita " \
                                  f"studentului cu ID-ul [{id_student}]: {stud.getnume()} " \
                                  f"la disciplina cu ID-ul [{id_disciplina}]: {disc.getnume()}"
            return lista_dict

    def get_nr_note_service(self):
        """
        se returneaza numarul de note aflate in repository
        :param params: lista goala []
        :return: numarul de note aflate in repository
        """
        return self.__repository.getlenlista()

    def get_note_disc(self, id_disc):
        """
        se returneaza notele studentilor de la o disciplina cu id-ul dat
        :param id_disc: id disciplina
        :return: list de note la disc.
        """
        ids = id_disc
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError:
            raise ValueError("ID disciplina invalid!")
        try:
            disc = self.__repository_disciplina.get_disc_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        lista_note = self.__repository.get_note_disciplina(id_disc)
        lista_note_1 = copy.deepcopy(lista_note)
        self.__ordonare_alfabetic_studenti(lista_note)
        self.__ordonare_desc_note(lista_note_1)
        return lista_note, lista_note_1

    def __ord_alf_stud(self, nota):
        """
        pt ordonoarea descrescatoare a notelor
        :param nota:
        :return:
        """
        id_stud = nota.getid_student()
        stud = self.__repository_student.get_stud_from_id(id_stud)
        nume_stud = stud.getnume()
        return nume_stud

    def __ord_desc_note(self, nota):
        """
        pt ordonarea descrescatoare a notelor
        :param nota:
        :return:
        """
        valoare = nota.getnota()
        return valoare

    def __ordonare_alfabetic_studenti(self, lista):
        """
        returneaza lista ordonata alfabetic dupa numele studentilor
        :param lista: lista de note
        :return: lista ordonata
        """
        lista = sortare(lista, key=(self.__ord_alf_stud, self.__ord_desc_note), nume_sortare="Selection_Sort")

    def __ordonare_desc_note(self, lista):
        """
        returneaza lista ordonata desc dupa valorile notelor studentilor
        :param lista: lista de note
        :return: list ordonata
        """
        lista = sortare(lista, key=self.__ord_desc_note, nume_sortare="Shake_Sort", reverse=True)

    def sefpromotie(self):
        """
        returneaza lista sefilor de promotie sortate descrescator
        :return: -
        """
        rezultate = []
        situatie_studenti = {}
        lista_toate_notele = self.__repository.getlista()
        for nota_id in self.__repository.getlista():
            nota = self.__repository.get_nota_from_id(nota_id)
            id_stud = self.__repository.get_id_student_nota(nota)
            if id_stud not in situatie_studenti:
                situatie_studenti[id_stud] = []
            situatie_studenti[id_stud].append(nota.getnota())
        for stud_id in situatie_studenti:
            note_stud = situatie_studenti[stud_id]
            medie_stud = sum(note_stud) / len(note_stud)
            medie_stud = round(medie_stud, 4)
            student = self.__repository_student.get_stud_from_id(stud_id)
            nume = student.getnume()
            sefDTO = SefPromotieDTO(stud_id, nume, medie_stud)
            rezultate.append(sefDTO)
        rezultate = sortare(rezultate, key=lambda x: x.getmedia(), nume_sortare="Shake_Sort", reverse=True)
        nr_stud = self.__repository_student.getlenlista()
        nr_stud = nr_stud // 5
        if nr_stud == 0:
            nr_stud = 1
        rezfinal = rezultate[:nr_stud]
        return rezfinal

    def sefpromotie_to_file(self):
        """
        returneaza lista sefilor de promotie sortate descrescator; dar o scrie si in file
        :return: lista de sefi de promotie
        """
        lista_stud = self.sefpromotie()
        self.__repository.write_to_file_raport(lista_stud)
        return lista_stud

    def medie_generala_disciplina(self, id_disciplina):
        """
        calculeaza media studentilor la o anumita disciplina data prin parametrul de id_disciplina
        :param id_disciplina: id-ul disciplinei
        :return: 2 liste cu mediile studentilor, una descrescator dupa valorile notelor si cealalta ordonata alfabetic
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista id-ul disciplinei in repo
        """
        rezultate = []
        if id_disciplina not in self.__repository_disciplina.getlista():
            raise ValueError("Disciplina inexistenta!")
        lista_note_stud = {}
        for nota_id in self.__repository.getlista():
            nota = self.__repository.get_nota_from_id(nota_id)
            if id_disciplina == self.__repository.get_id_disciplina_nota(nota):
                id_stud = nota.getid_student()
                if id_stud not in lista_note_stud:
                    lista_note_stud[id_stud] = []
                lista_note_stud[id_stud].append(nota.getnota())
        for stud_id in lista_note_stud:
            note_stud = lista_note_stud[stud_id]
            medie_stud = sum(note_stud) / len(note_stud)
            medie_stud = round(medie_stud, 4)
            student = self.__repository_student.get_stud_from_id(stud_id)
            nume = student.getnume()
            medieDTO = SefPromotieDTO(stud_id, nume, medie_stud)
            rezultate.append(medieDTO)
        rezultate = sortare(rezultate, key=lambda x: x.getmedia(), nume_sortare="Selection_Sort", reverse=True)
        rezultate1 = copy.deepcopy(rezultate)
        rezultate1 = sortare(rezultate1, key=lambda x: x.getnume(), nume_sortare="Shake_Sort")
        return rezultate, rezultate1

    def make_str_nota(self, lista):
        """
        transforma o lista de note in lista de stringuri de note
        :param lista: lista de note
        :return: lista formata din stringuri
        """
        lista_string = []
        for nota in lista:
            student = self.__repository_student.get_stud_from_id(nota.getid_student())
            disciplina = self.__repository_disciplina.get_disc_from_id(nota.getid_disciplina())
            nota_str = f"Nota cu ID-ul [{nota.getid()}] si valoarea {nota.getnota()} atribuita " \
               f"studentului cu ID-ul [{nota.getid_student()}]: {student.getnume()} " \
               f"la disciplina cu ID-ul [{nota.getid_disciplina()}: {disciplina.getnume()}]"
            lista_string.append(nota_str)
        return lista_string

    def auto_populare_note_service(self, nr):
        """
        functia care autopopuleaza lista de note cu note, studenti si discipline create in prealabil
        :return: -
        """
        if nr <= 0:
            raise ValueError("Introdu un numar valid de note!")
        id_stud = list(self.__repository_student.getlista().keys())
        id_disc = list(self.__repository_disciplina.getlista().keys())
        for i in range(nr):
            id_s = id_stud[i % len(id_stud)]
            id_d = id_disc[i % len(id_disc)]
            val_n = round(random.uniform(1.00, 10.00), 2)
            self.adauga_nota_service([id_s, id_d, val_n])
