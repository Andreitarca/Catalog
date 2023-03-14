from alte_functii.recursivitate import cauta

class ListaStudenti:
    """
    clasa Lista_Studenti ne creeaza si manageriaza lista cu studentii de tip Student
    """
    def __init__(self):
        """
        un obiect de tipul ListaStudenti este format dintr-un dictionar
        """
        self._lista = {}

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
        '''
                                ---- complexitate ----
                base case:  elementul care urmeaza sa fie adaugat se afla pe prima pozitie in lista generata
                                complexitatea: = O(1)
                worst case: elementul pe care care urmeaza sa fie adaugat se afla pe ultima pozitie sau nu se afla deloc in lista generata
                                complexitatea: = O(n)
                average case: depinde de pozitia elementului care urmeaza sa fie adaugat in lista sau daca se afla in lista
                                complexitatea: = O(n)
        '''
        if cauta(list(self._lista.keys()), student.getid()):
            raise ValueError("Student existent!")
        self._lista[student.getid()] = student

    def getlista(self):
        """
        este returnata lista de studenti
        :return: lista care contine obiectele studenti
        """
        return self._lista

    def getlenlista(self):
        """
        este returnata lungimea listei de obiecte Student
        :return: lungimea listei de obiecte Student
        """
        return len(self._lista)

    def get_stud_from_id(self, idp):
        """
        este returnat studentul cu id-ul primit prin parametrul idp
        :param idp: id de tip intreg pozitiv
        :return: studentul cu id-ul idp daca exista
        :raises:        ValueError cu mesajul "Student inexistent!" daca nu exista student cu acest id in lista
                                              "ID invalid!" daca idp nu poate fi id
        """
        if cauta(list(self._lista.keys()), idp):
            return self._lista[idp]
        raise ValueError("Student inexistent!")

    def sterge_student(self, student):
        """
        sterge obiectul de tip student din dictionarul de obiecte studenti
        :param student: obiect de tip student
        :return: -
        :raises:    ValueError cu mesajul "Student inexistent!" daca nu exista acest student in dictionar
        """
        try:
            del self._lista[student.getid()]
        except KeyError:                    #am id deci key error
            raise ValueError("Student inexistent!")

    def get_nume_student(self, student):
        """
        returneaza numele obiectului de tip student aflat in dictionar
        :param student: obiect de tip Student
        :return: string - numele studentului
        :raises: ValueError cu mesajul "Student inexistent!" daca nu exista acest student in dictionar
        """
        if cauta(list(self._lista.keys()), student.getid()):
            return student.getnume()
        else:
            raise ValueError("Student inexistent!")

    def modifica_nume_student(self, student, nume_nou):
        """
        modifica numele obiectului de tip Student aflat in dictionar
        :param student: obiect de tip Student
        :param nume_nou: string nevid, urmatorul nume
        :return: -
        :raises: ValueError cu mesajul "Student inexistent!" daca nu exista acest student in dictionar
                                       "Nume invalid!" daca nume_nou este vid
        """
        if cauta(list(self._lista.keys()), student.getid()):
            self._lista.pop(student.getid())
            student.setnume(nume_nou)
            self._lista[student.getid()] = student
        else:
            raise ValueError("Student inexistent!")

    def del_all(self):
        """
        sterge toti studentii din repository-ul de studenti
        :return: -
        """
        self._lista = {}
