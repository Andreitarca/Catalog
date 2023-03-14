from domain.studenti import Student
from repository.repository_studenti import ListaStudenti


class ListaStudentiFile(ListaStudenti):
    def __init__(self, filename):
        ListaStudenti.__init__(self)
        self.__filename = filename

    def __read_all_from_file(self):
        """
        functia de citire din fisier - se apeleaza de fiecare data
        :return: -
        :raise: IOError daca nu exista fisierul
        """
        try:
            with open(self.__filename, "r") as f:
                lines = f.readlines()
                self._lista.clear()  # tre sa stergi de dinainte
                for line in lines:
                    line = line.strip()
                    if line != "":
                        parts = line.split(";")
                        id_student = int(parts[0])
                        nume_student = parts[1]
                        nume_student = nume_student.strip()
                        student = Student(id_student, nume_student)
                        self._lista[id_student] = student
        except IOError:
            raise IOError("The file doesn't exist!")

    def __write_all_to_file(self):
        """
        functia de scriere in fisier
        :return:
        """
        with open(self.__filename, "w") as f:
            for id_stud in self._lista.keys():
                student = self._lista[id_stud]
                f.write(f"{str(student.getid())}; {str(student.getnume())}\n")

    def adauga_student(self, student):
        """
        se adauga un student la dictionarul curent de studenti
        :param student: obiect de tipul Student
        :return: -
        :raises:    ValueError cu mesajul "Student existent!" daca exista deja un student cu acelasi id in lista
                    ValueError daca datele din student sunt invalide:
                            daca studentID < 0 sau daca disciplinaID nu este intreg -> "Id invalid"
                            daca nume == "" -> "Nume invalid!"
        """
        self.__read_all_from_file()
        ListaStudenti.adauga_student(self, student)
        self.__write_all_to_file()

    def getlista(self):
        """
        este returnata lista de studenti
        :return: lista care contine obiectele studenti
        """
        self.__read_all_from_file()
        return ListaStudenti.getlista(self)

    def getlenlista(self):
        """
        este returnata lungimea listei de obiecte Student
        :return: lungimea listei de obiecte Student
        """
        self.__read_all_from_file()
        return ListaStudenti.getlenlista(self)

    def get_stud_from_id(self, idp):
        """
        este returnat studentul cu id-ul primit prin parametrul idp
        :param idp: id de tip intreg pozitiv
        :return: studentul cu id-ul idp daca exista
        :raises:        ValueError cu mesajul "Student inexistent!" daca nu exista student cu acest id in lista
                                              "ID invalid!" daca idp nu poate fi id
        """
        self.__read_all_from_file()
        return ListaStudenti.get_stud_from_id(self, idp)

    def sterge_student(self, student):
        """
        sterge obiectul de tip student din dictionarul de obiecte studenti
        :param student: obiect de tip student
        :return: -
        :raises:    ValueError cu mesajul "Student inexistent!" daca nu exista acest student in dictionar
        """
        self.__read_all_from_file()
        ListaStudenti.sterge_student(self, student)
        self.__write_all_to_file()

    def get_nume_student(self, student):
        """
        returneaza numele obiectului de tip student aflat in dictionar
        :param student: obiect de tip Student
        :return: string - numele studentului
        :raises: ValueError cu mesajul "Student inexistent!" daca nu exista acest student in dictionar
        """
        self.__read_all_from_file()
        return ListaStudenti.get_nume_student(self, student)

    def modifica_nume_student(self, student, nume_nou):
        """
        modifica numele obiectului de tip Student aflat in dictionar
        :param student: obiect de tip Student
        :param nume_nou: string nevid, urmatorul nume
        :return: -
        :raises: ValueError cu mesajul "Student inexistent!" daca nu exista acest student in dictionar
                                       "Nume invalid!" daca nume_nou este vid
        """
        self.__read_all_from_file()
        ListaStudenti.modifica_nume_student(self, student, nume_nou)
        self.__write_all_to_file()

    def del_all(self):
        """
        sterge toti studentii din repository-ul de studenti
        :return: -
        """
        ListaStudenti.del_all(self)
        self.__write_all_to_file()
