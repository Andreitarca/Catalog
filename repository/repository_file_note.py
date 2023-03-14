from domain.note import Nota
from repository.repository_note import ListaNote


class ListaNoteFile(ListaNote):
    def __init__(self, filename):
        ListaNote.__init__(self)
        self.__filename = filename

    def __read_all_from_file(self):
        """
        functia de citire din fisier - se apeleaza de fiecare data
        :return: -
        :raise: IOError daca nu exista fisierul
        """
        try:
            with open(self.__filename) as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line != "":
                        parts = line.split(";")
                        id_nota = int(parts[0])
                        id_student = int(parts[1])
                        id_disciplina = int(parts[2])
                        valoare_nota = float(parts[3])
                        nota = Nota(id_nota, id_student, id_disciplina, valoare_nota)
                        self._lista[id_nota] = nota
        except IOError:
            raise IOError("The file doesn't exist!")

    def __write_all_to_file(self):
        """
        functia de scriere in fisier
        :return:
        """
        with open(self.__filename, "w") as f:
            for id_nota in self._lista:
                nota = self._lista[id_nota]
                f.write(f"{nota.getid()}; {nota.getid_student()}; {nota.getid_disciplina()}; {nota.getnota()}")
                f.write("\n")

    def getlista(self):
        """
        este returnata lungimea listei de obiecte Nota
        :return: lungimea listei de obiecte Nota
        """
        self.__read_all_from_file()
        return ListaNote.getlista(self)

    def getlenlista(self):
        """
        este returnata lista de Note
        :return: dictionar care contine obiectele Note
        """
        self.__read_all_from_file()
        return ListaNote.getlenlista(self)

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
        self.__read_all_from_file()
        ListaNote.adauga_nota(self, nota)
        self.__write_all_to_file()

    def sterge_nota(self, nota):
        """
        sterge obiectul de tip nota din dictionarul de obiecte note
        :param nota: obiect de tip nota
        :return: -
        :raises:    ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        self.__read_all_from_file()
        ListaNote.sterge_nota(self, nota)
        self.__write_all_to_file()

    def sterge_note_student(self, id_stud):
        """
        sterge toate obiectele de tip nota ale id_studentului id_stud din dictionarul de obiecte note
        :param id_stud: obiect de tip id_student
        :return: -
        :raises: -
        """
        self.__read_all_from_file()
        ListaNote.sterge_note_student(self, id_stud)
        self.__write_all_to_file()

    def sterge_note_disciplina(self, id_disc):
        """
        sterge toate obiectele de tip nota la disciplina disc din dictionarul de obiecte note
        :param disc: obiect de tip Disciplina
        :return: -
        :raises: -
        """
        self.__read_all_from_file()
        ListaNote.sterge_note_disciplina(self, id_disc)
        self.__write_all_to_file()

    def get_note_disciplina(self, id_disc):
        """
        returneaza toate obiectele de tip nota la disciplina disc din dictionarul de obiecte note
        :param disc: obiect de tip Disciplina
        :return: lista de obiecte
        :raises: -
        """
        self.__read_all_from_file()
        return ListaNote.get_note_disciplina(self, id_disc)

    def modifica_nota(self, nota, val_noua):
        """
        modifica valoarea obiectului de tip Nota aflata in dictionar
        :param nota: obiect de tip Nota
        :param val_noua: float cuprins intre 1 si 10
        :return: -
        :raises: ValueError cu mesajul "Nota inexistent!" daca nu exista aceasta disciplina in dictionar
                                       "Nota invalida!" daca val_noua nu este un float cuprins intre 1 si 10
        """
        self.__read_all_from_file()
        ListaNote.modifica_nota(self, nota, val_noua)
        self.__write_all_to_file()

    def get_valoare_nota(self, nota):
        """
        returneaza valoarea notei obiectului de tip nota aflat in dictionar
        :param nota: obiect de tip nota
        :return: float - valoarea notei
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        self.__read_all_from_file()
        return ListaNote.get_valoare_nota(self, nota)

    def get_nota_from_id(self, idn):
        """
        returneaza obiectul de tip nota aflat in dictionar cu id-ul idn
        :param idn: id-ul notei
        :return: obiect de tipul Nota
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista acest id de nota in dictionar
        """
        self.__read_all_from_file()
        return ListaNote.get_nota_from_id(self, idn)

    def get_id_student_nota(self, nota):
        """
        returneaza id-ul studentul obiectului de tip nota aflat in dictionar
        :param nota: obiect de tip nota
        :return: int id-ul studentului
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        self.__read_all_from_file()
        return ListaNote.get_id_student_nota(self, nota)

    def get_id_disciplina_nota(self, nota):
        """
        returneaza id-ul disciplinei obiectului de tip nota aflat in dictionar
        :param nota: obiect de tip nota
        :return: int id-ul disciplinei
        :raises: ValueError cu mesajul "Nota inexistenta!" daca nu exista aceasta nota in dictionar
        """
        self.__read_all_from_file()
        return ListaNote.get_id_disciplina_nota(self, nota)

    def del_all(self):
        """
        sterge toate notele
        :return: -
        """
        ListaNote.del_all(self)
        self.__write_all_to_file()

    def write_to_file_raport(self, list):
        """
        scrie lista primita in file-ul primit
        :param list: lista
        :return: -
        """
        with open("files_repository/sef_promotie.txt", "w") as f:
            i = 0
            for el in list:
                i += 1
                f.write(str(i) + ". ")
                f.write(str(el))
                f.write("\n")
