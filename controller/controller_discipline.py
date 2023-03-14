from controller.random_entities import RandomDisciplina
from domain.discipline import Disciplina
from validating.alte_validari import AlteValidari


class ManageDiscipline:
    """
    clasa care manageriaza disciplinele, avand un repository si un validator specifice
    """
    def __init__(self, repository, validator):
        """
        creeaza un manager de studenti si salveaza datele in repository si le valideaza cu ajutorul validatorului
        :param repository: obiect de tipul ListaDiscipline
        :param validator: obiect de tipul DisciplinaValidator
        """
        self.__repository = repository
        self.__validator = validator

    def __make_id_disc(self):
        """
        obtine un nou id pentru un viitor disciplina care urmeaza a fi creat
        :return: id pt disciplina
        """
        lista_id = list(self.__repository.getlista().keys())
        lista_id.append(50)
        ids = max(lista_id)
        while self.__exist_id_service(ids):
            ids = ids + 1
        return ids

    def adauga_disciplina_service(self, params):
        """
        se adauga o disciplina la lista actuala de discipline stocata in __repository
        :param params: lista de parametri care contin datele dupa urmatorul model:
                        1. doi parametri -> primul va fi numele disciplinei, iar al doilea numele profesorului
                        2. trei parametri -> primul va fi id-ul daca nu este deja alocat, iar celelalte 2 ca mai sus
        :return: -
        :raises:  ValueError cu urmatoarele mesaje:
                    "Numar parametri invalid!" daca nu este corect numarul parametrilor
                    "Disciplina existenta!" daca exista deja un disciplina cu acelasi id in lista
                    ValueError pentru validare:
                        daca disciplinaID < 0 sau daca disciplinaID nu este intreg -> "Id invalid"
                        daca nume == "" -> "Nume disciplina invalid!"
                        daca prof == "" -> "Nume profesor invalid!"
        """
        if len(params) == 2:
            nume = params[0]
            prof = params[1]
            idd = self.__make_id_disc()
        elif len(params) == 3:
            idd = params[0]
            nume = params[1]
            prof = params[2]
        else:
            raise ValueError("Numar parametri invalid!")
        disc = Disciplina(idd, nume, prof)
        try:
            self.__validator.validare(disc)
        except ValueError as ve:
            raise ValueError(ve)
        try:
            self.__repository.adauga_disciplina(disc)
        except ValueError as ve:
            raise ValueError(ve)

    def __exist_id_service(self, idp):
        """
        verifica daca exista id-ul ids in dictionarul de obiecte disciplina
        :param idp: id de tip intreg pozitiv
        :return:    True daca exista acest ids in dictionarul de discipline
                    False daca nu exista acest ids in dictionarul de discipline
        :raises:    ValueError cu mesajul "ID invalid!" daca nr_id nu poate fi id
        """
        if idp in self.__repository.getlista():
            return True
        return False

    def __sterge_disciplina_service(self, disc):
        """
        sterge disciplina disc din repository
        :param disc: obiect de tip Disciplina
        :return: -
        :raises ValueError cu mesajul "Disciplina inexistenta!" daca nu exista disciplina disc in repository
        """
        self.__repository.sterge_disciplina(disc)

    def sterge_disciplina_id_service(self, params):
        """
        sterge disciplina cu id-ul primit prin lista de parametri din repository
        :param params: lista de parametri cu un singur element: id-ul
        :return: -
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista disciplina disc cu ids in repository
                                       "ID Disciplina invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        idd = params[0]
        validari = AlteValidari()
        try:
            validari.validare_id(idd)
        except ValueError as ve:
            raise ValueError("ID disciplina invalid!")
        try:
            disc = self.__repository.get_disc_from_id(idd)
        except ValueError as ve:
            raise ValueError(ve)
        self.__sterge_disciplina_service(disc)

    def __modifica_nume_disiplina_service(self, disc, nume_nou):
        """
        modifica numele obiectului de tip disciplina aflat in repository cu numele primit prin parametru
        :param disc: obiect de tipul disciplina
        :param nume_nou disc: string nevid
        :return: -
        :raises: ValueError cu diferite mesaje:
                        "Disciplina inexistenta!" daca nu exista disciplina stud in repository
                        "Nume disciplina invalid!" daca nume_nou este vid
        """
        self.__repository.modifica_nume_disciplina(disc, nume_nou)

    def __modifica_prof_disciplina_service(self, disc, prof_nou):
        """
        modifica numele profesorului obiectului de tip disciplina aflat in repository cu numele primit prin parametru
        :param disc: obiect de tipul disciplina
        :param prof_nou disc: string nevid
        :return: -
        :raises: ValueError cu diferite mesaje:
                        "Disciplina inexistenta!" daca nu exista disciplina stud in repository
                        "Nume profesor invalid!" daca prof_nou este vid
        """
        self.__repository.modifica_profesor_disciplina(disc, prof_nou)

    def modifica_disciplina_id_service(self, params):
        """
        modifica numele obiectului de tip Disciplina cu id-ul din params aflat in repository cu numele primit prin params
        :param params: lista de doua sau trei elemente; primul este id-ul disciplinei, cel de-al doilea  si al treile noul nume
        :return: -
        :raises: ValueError cu diferite mesaje:
                        "Disciplina inexistenta!" daca nu exista disciplina disc in repository
                        "Nume disciplina invalid!" daca nume_nou este vid
                        "Nume profesor invalid!" daca prof_nou este vid
                        "ID disciplina invalid!" daca id-ul introdus nu este intreg pozitiv
                        "Numar parametri invalid!" daca nu sunt doar doua sau trei elemente in params
        """
        erori = ""
        comenzi = {
            "nume": self.__modifica_nume_disiplina_service,
            "prof": self.__modifica_prof_disciplina_service
        }
        validari = AlteValidari()           # am vaga impresie ca mi-l crapa daca pune altceva aici
        if len(params) == 2 or len(params) == 3:
            idd = params[0]
            try:
                validari.validare_id(idd)
            except ValueError as ve:
                erori += "ID disciplina invalid!\n"
            for i in range(1, len(params)):
                split = params[i].split(":")
                if len(split) == 2:
                    comanda = split[0]
                    comanda = comanda.strip()
                    if comanda in comenzi:
                        nume = split[1]
                        nume = nume.strip()
                        try:
                            validari.validare_nume(nume)
                        except ValueError as ve:
                            if comanda == "nume":
                                erori += "Nume disciplina invalid!\n"
                            else:
                                erori += "Nume profesor invalid!\n"
                        if len(erori) > 0:
                            raise ValueError(erori[:-1])
                        try:
                            disc = self.__repository.get_disc_from_id(idd)
                        except ValueError as ve:
                            raise ValueError(ve)
                        comenzi[comanda](disc, nume)
                    else:
                        raise ValueError("Comanda invalida!")
                else:
                    raise ValueError("Comanda invalida!")
        else:
            raise ValueError("Numar parametri invalid!")

    def get_all_discipline_service(self):
        """
        sunt returnate toate obiectele de tip Disciplina din repository
        :return: lista[dictionatul] din repository
        :raises: ValueError cu mesajul "Nu exista nicio disciplina introdusa!" daca lista este goala
        """
        if self.__repository.getlenlista() == 0:
            raise ValueError("Nu exista nicio disciplina introdusa!")
        else:
            return self.__repository.getlista()

    def get_disciplina_id_service(self, idd):
        """
        returneaza disciplina din repository cu id-ul primit in params
        :param params: lista de elemente: contine doar id-ul intreg pozitiv
        :return: obiect de tip Disciplina
        :raises: ValueError cu diverse mesaje:
                        "ID disciplina invalid!" daca id-ul introdus nu este intreg pozitiv
                        "Numar parametri invalid!" daca nu sunt doar doua elemente in params
                        "Disciplina inexistent!" daca nu exista disciplina cu id-ul introdus in repository
        """
        validari = AlteValidari()
        try:
            validari.validare_id(idd)
        except ValueError as ve:
            raise ValueError("ID disciplina invalid!")
        try:
            disc = self.__repository.get_disc_from_id(idd)
        except ValueError as ve:
            raise ValueError(ve)
        return disc

    def get_nume_disciplina_id_service(self, idd):
        """
        returneaza numele disciplinei cu id-ul idd daca acesta se afla in repository
        :param idd: id-ul disciplinei
        :return: numele disciplinei disc
        :raises: ValueError cu mesajul: "Disciplina inexistenta!" daca nu exista disciplina disc in repository
                                        "ID disciplina invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        validari = AlteValidari()
        try:
            validari.validare_id(idd)
        except ValueError:
            raise ValueError("ID disciplina invalid!")
        try:
            disc = self.__repository.get_disc_from_id(idd)
        except ValueError as ve:
            raise ValueError(ve)
        return self.__repository.get_nume_disciplina(disc)

    def get_profesor_disciplina_id_service(self, idd):
        """
        returneaza numele profesorului disciplinei cu id-ul idd daca acesta se afla in repository
        :param idd: id-ul disciplinei
        :return: numele profesorului disciplinei disc
        :raises: ValueError cu mesajul: "Disciplina inexistenta!" daca nu exista disciplina disc in repository
                                        "ID disciplina invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        validari = AlteValidari()
        try:
            validari.validare_id(idd)
        except ValueError:
            raise ValueError("ID disciplina invalid!")
        try:
            disc = self.__repository.get_disc_from_id(idd)
        except ValueError as ve:
            raise ValueError(ve)
        return self.__repository.get_prof_disciplina(disc)

    def get_nr_discipline_service(self):
        """
        se returneaza numarul de discipine aflate in repository
        :param params: lista goala []
        :return: numarul de discipline aflate in repository
        """
        return self.__repository.getlenlista()

    def __cauta_nume_disciplina_service(self, nume):
        """
        cauta si returneaza cheile obiectelor de tip disciplina din dictionar daca
        numele acestora contine nume primit prin parametru
        nu se tine cont de majuscule
        :param nume: string nevid
        :return: lista de key (id-uri) ale obiectelor de tip disciplina care contin in numele lor stringul introdus
        :raises: ValueError cu mesajul "Nume invalid!" daca nume_nou este vid
        """
        keys = []
        nume = nume.lower()
        for key in self.__repository.getlista():
            if nume in self.__repository.getlista()[key].getnume().lower():
                keys.append(key)
        return keys

    def __cauta_prof_disciplina_service(self, prof):
        """

        :param prof:
        :return:
        """
        keys = []
        nume = prof.lower()
        for key in self.__repository.getlista():
            if nume in self.__repository.getlista()[key].getprof().lower():
                keys.append(key)
        return keys

    def cauta_discipline_service(self, params):
        """
        functia cauta discipline care au in nume sau prof_nume subnumele primit prin params
        :param params: lista de parametri, o parte din numele disciplinei sau profesorului
        :return: o lista de keys reprezentand id-ul disciplinelor
        :raises: ValueError cu diferite mesaje:
                        "Nume disciplina invalid!" daca nume_nou este vid
                        "Nume profesor invalid!" daca prof_nou este vid
                        "Numar parametri invalid!" daca nu sunt doar doua sau trei elemente in params
        """
        # ahm aici pot avea mai multi parametri si dupa numele profului si dupa numele disciplinei
        validare = AlteValidari()
        keys = []
        final_keys = []
        comenzi = {
            "nume": self.__cauta_nume_disciplina_service,
            "prof": self.__cauta_prof_disciplina_service
        }
        if len(params) == 1 or len(params) == 2:
            for i in range(len(params)):
                split = params[i].split(":")
                if len(split) == 2:
                    comanda = split[0]
                    comanda = comanda.strip()
                    if comanda in comenzi:
                        nume = split[1]
                        nume = nume.strip()
                        try:
                            validare.validare_nume(nume)
                        except ValueError as ve:
                            if comanda == "nume":
                                raise ValueError("Nume de cautat disciplina invalid!")
                            else:
                                raise ValueError("Nume de cautat profesor invalid!")
                        keys.append(comenzi[comanda](nume))
                    else:
                        raise ValueError("Comanda invalida!")
                else:
                    raise ValueError("Comanda invalida!")
        else:
            raise ValueError("Numar parametri invalid!")
        if len(keys) == 1:
            final_keys = keys[0]
        else:
            keys1 = keys[0]
            keys2 = keys[1]
            for el in keys1:
                if el in keys2:
                    final_keys.append(el)
        return final_keys

    def sterge_toate_disciplinele(self):
        """
        sterge toate entintatile disciplina din repository
        :return: -
        """
        self.__repository.del_all()

    def discipline_random_service(self, nr_disc):
        if nr_disc <= 0:
            raise ValueError("Numar de discipline invalid!")
        lista_disc_random = RandomDisciplina()
        lista_disc_random.genereaza_discipline(nr_disc)
        lista_nume_prof_disc_generati = lista_disc_random.getlista_nume_prof_random()
        for i in range(nr_disc):
            self.adauga_disciplina_service(lista_nume_prof_disc_generati[i])

    def auto_populare_discipline_service(self):
        """
        functia care autopopuleaza lista de discipline cu discipline create in prealabil
        :return: -
        """
        self.adauga_disciplina_service(["Analiza Matematica", "Tudor Laurentiu"])
        self.adauga_disciplina_service(["Algebra Matematica", "Ifrim Alberto"])
        self.adauga_disciplina_service(["Geometrie Matematica", "Tudor Bogdan"])
        self.adauga_disciplina_service(["Programare in C", "Gabureanu Laurentiu"])
        self.adauga_disciplina_service(["Programare in Python", "Gherban Dalia"])
        self.adauga_disciplina_service(["Informatica complexa", "Nita Eugen"])
        self.adauga_disciplina_service(["Arhitectura sistemelor", "Tomescu Dalia"])
