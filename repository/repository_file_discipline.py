from domain.discipline import Disciplina
from repository.repository_discipline import ListaDiscipline


class ListaDisciplineFile(ListaDiscipline):
    def __init__(self, filename):
        ListaDiscipline.__init__(self)
        self.__filename = filename

    def __read_all_from_file(self):
        """
        functia de citire din fisier
        :return: -
        :raises IOError daca un exista fisierul
        """
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                self._lista.clear()
                for line in lines:
                    line = line.strip()
                    if line != "":
                        parts = line.split(";")
                        id_disc = int(parts[0])
                        nume_disc = parts[1]
                        nume_disc = nume_disc.strip()
                        prof_disc = parts[2]
                        prof_disc = prof_disc.strip()
                        disciplina = Disciplina(id_disc, nume_disc, prof_disc)
                        self._lista[id_disc] = disciplina
        except IOError:
            raise IOError("The file doesn't exist!")

    def __write_all_to_file(self):
        """
        funcita de scriere in fisier
        :return: -
        """
        with open(self.__filename, "w") as f:
            for id_disc in self._lista.keys():
                disciplina = self._lista[id_disc]
                f.write(f"{str(disciplina.getid())}; {str(disciplina.getnume())}; {str(disciplina.getprof())}\n")

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
        self.__read_all_from_file()
        ListaDiscipline.adauga_disciplina(self, disciplina)
        self.__write_all_to_file()

    def getlista(self):
        """
        este returnata lista de discipline
        :return: dictionar care contine obiectele discipline
        """
        self.__read_all_from_file()
        return ListaDiscipline.getlista(self)

    def getlenlista(self):
        """
        este returnata lista de discipline
        :return: dictionar care contine obiectele discipline
        """
        self.__read_all_from_file()
        return ListaDiscipline.getlenlista(self)

    def get_disc_from_id(self, idp):
        """
        este returnata disciplina cu id-ul primit prin parametrul idp
        :param idp: id de tip intreg pozitiv
        :return: disciplina cu id-ul idp daca exista
        :raises:        ValueError cu mesajul "Disciplina inexistenta!" daca nu exista disciplina cu acest id in lista
                                              "ID invalid!" daca idp nu poate fi id
        """
        self.__read_all_from_file()
        return ListaDiscipline.get_disc_from_id(self, idp)

    def sterge_disciplina(self, disciplina):
        """
        sterge obiectul de tip disciplia din dictionarul de obiecte discipline
        :param disciplina: obiect de tip disciplina
        :return: -
        :raises:    ValueError cu mesajul "Disciplina inexistenta!" daca nu exista aceasta disciplina in dictionar
        """
        self.__read_all_from_file()
        ListaDiscipline.sterge_disciplina(self, disciplina)
        self.__write_all_to_file()

    def get_nume_disciplina(self, disciplina):
        """
        returneaza numele obiectului de tip disciplina aflat in dictionar
        :param disciplina: disciplina data
        :type disciplina: object
        :return: string - numele disciplinei
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista aceasta disciplina in dictionar
        """
        self.__read_all_from_file()
        return ListaDiscipline.get_nume_disciplina(self, disciplina)

    def get_prof_disciplina(self, disciplina):
        """
        returneaza numele profesorului obiectului de tip disciplina aflat in dictionar
        :param disciplina: obiect de tip disciplina
        :return: string - numele profesorului care preda disciplina
        :raises: ValueError cu mesajul "Disciplina inexistenta!" daca nu exista aceasta disciplina in dictionar
        """
        self.__read_all_from_file()
        return ListaDiscipline.get_prof_disciplina(self, disciplina)

    def modifica_nume_disciplina(self, disciplina, nume_nou):
        """
        modifica numele obiectului de tip Disciplina aflata in dictionar
        :param disciplina: obiect de tip Disciplina
        :param nume_nou: string nevid, urmatorul posibil nume
        :return: -
        :raises: ValueError cu mesajul "Disciplina inexistent!" daca nu exista aceasta disciplina in dictionar
                                       "Nume disciplina invalid!" daca nume_nou este vid
        """
        self.__read_all_from_file()
        ListaDiscipline.modifica_nume_disciplina(self, disciplina, nume_nou)
        self.__write_all_to_file()

    def modifica_profesor_disciplina(self, disciplina, prof_nou):
        """
        modifica numele profesorului obiectului de tip Disciplina aflata in dictionar
        :param disciplina: obiect de tip Disciplina
        :param prof_nou: string nevid, urmatorul posibil nume al profesorului
        :return: -
        :raises: ValueError cu mesajul "Disciplina inexistent!" daca nu exista aceasta disciplina in dictionar
                                       "Nume profesor invalid!" daca nume_nou este vid
        """
        self.__read_all_from_file()
        ListaDiscipline.modifica_profesor_disciplina(self, disciplina, prof_nou)
        self.__write_all_to_file()

    def del_all(self):
        """
        sterge toate disciplinele
        :return: -
        """
        ListaDiscipline.del_all(self)
        self.__write_all_to_file()
