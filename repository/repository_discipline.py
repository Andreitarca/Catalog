from validating.alte_validari import AlteValidari
from validating.validari_domeniu import DisciplinaValidator


class ListaDiscipline:
    """
    clasa Lista_Discipline ne creeaza si manageriaza lista cu disciplinele de tip Disciplina
    """
    def __init__(self):
        """
        un obiect de tipul ListaDiscipline este format dintr-un dictionar
        """
        self._lista = {}

    def adauga_disciplina(self, disciplina):
        """
        se adauga o disciplina la dictionarul curent de discipline
        :param disciplina: obiect de tipul Disciplina
        :return: -
        :raises:    ValueError cu mesajul "Disciplina existenta!" daca exista deja o disciplina cu acelasi id in lista
                    ValueError daca datele din disciplina sunt invalide:
                        daca disciplinaID < 0 sau daca disciplinaID nu este intreg -> "Id invalid"
                        daca nume == "" -> "Nume invalid!"
                        daca prof == "" -> "Nume profesor invalid!"
        """
        validare = DisciplinaValidator()
        try:
            validare.validare(disciplina)
        except ValueError as ve:
            raise ValueError(ve)
        if disciplina.getid() in self._lista:
            raise ValueError("Disciplina existenta!")
        self._lista[disciplina.getid()] = disciplina

    def getlista(self):
        """
        este returnata lista de discipline
        :return: dictionar care contine obiectele discipline
        """
        return self._lista

    def getlenlista(self):
        """
        este returnata lista de discipline
        :return: dictionar care contine obiectele discipline
        """
        return len(self._lista)

    def get_disc_from_id(self, idp):
        """
        este returnata disciplina cu id-ul primit prin parametrul idp
        :param idp: id de tip intreg pozitiv
        :return: disciplina cu id-ul idp daca exista
        :raises:        ValueError cu mesajul "Disciplina inexistenta!" daca nu exista disciplina cu acest id in lista
                                              "ID invalid!" daca idp nu poate fi id
        """
        validare = AlteValidari()
        try:
            validare.validare_id(idp)
        except ValueError as ve:
            raise ValueError("ID disciplina invalid!")
        if idp in self._lista:
            return self._lista[idp]
        raise ValueError("Disciplina inexistenta!")

    def sterge_disciplina(self, disciplina):
        """
        sterge obiectul de tip disciplia din dictionarul de obiecte discipline
        :param disciplina: obiect de tip disciplina
        :return: -
        :raises:    ValueError cu mesajul "Disciplina inexistenta!" daca nu exista aceasta disciplina in dictionar
        """
        try:
            del self._lista[disciplina.getid()]
        except KeyError:
            raise ValueError("Disciplina inexistenta!")

    def get_nume_disciplina(self, disciplina):
        """
        returneaza numele obiectului de tip disciplina aflat in dictionar
        :param disciplina: obiect de tip disciplina
        :return: string - numele disciplinei
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista aceasta disciplina in dictionar
        """
        if disciplina.getid() in self._lista:
            return disciplina.getnume()
        else:
            raise ValueError("Disciplina inexistenta!")

    def get_prof_disciplina(self, disciplina):
        """
        returneaza numele profesorului obiectului de tip disciplina aflat in dictionar
        :param disciplina: obiect de tip disciplina
        :return: string - numele profesorului care preda disciplina
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista aceasta disciplina in dictionar
        """
        if disciplina.getid() in self._lista:
            return disciplina.getprof()
        else:
            raise ValueError("Disciplina inexistenta!")

    def modifica_nume_disciplina(self, disciplina, nume_nou):
        """
        modifica numele obiectului de tip Disciplina aflata in dictionar
        :param disciplina: obiect de tip Disciplina
        :param nume_nou: string nevid, urmatorul posibil nume
        :return: -
        :raises: ValueError cu mesajul "Disciplina inexistent!" daca nu exista aceasta disciplina in dictionar
                                       "Nume disciplina invalid!" daca nume_nou este vid
        """
        alte_validari = AlteValidari()
        try:
            alte_validari.validare_nume(nume_nou)
        except ValueError as ve:
            raise ValueError("Nume disciplina invalid!")
        if disciplina.getid() in self._lista:
            self._lista.pop(disciplina.getid())
            disciplina.setnume(nume_nou)
            self._lista[disciplina.getid()] = disciplina
        else:
            raise ValueError("Disciplina inexistenta!")

    def modifica_profesor_disciplina(self, disciplina, prof_nou):
        """
        modifica numele profesorului obiectului de tip Disciplina aflata in dictionar
        :param disciplina: obiect de tip Disciplina
        :param prof_nou: string nevid, urmatorul posibil nume al profesorului
        :return: -
        :raises: ValueError cu mesajul "Disciplina inexistent!" daca nu exista aceasta disciplina in dictionar
                                       "Nume profesor invalid!" daca nume_nou este vid
        """
        alte_validari = AlteValidari()
        try:
            alte_validari.validare_nume(prof_nou)
        except ValueError as ve:
            raise ValueError("Nume profesor invalid!")
        if disciplina.getid() in self._lista:
            self._lista.pop(disciplina.getid())
            disciplina.setprof(prof_nou)
            self._lista[disciplina.getid()] = disciplina
        else:
            raise ValueError("Disciplina inexistenta!")

    def del_all(self):
        """
        sterge toate disciplinele
        :return: -
        """
        self._lista = {}
