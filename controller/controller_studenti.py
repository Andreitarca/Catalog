from alte_functii.recursivitate import cauta_studenti_cu_nume
from controller.random_entities import RandomStudent
from domain.studenti import Student
from validating.alte_validari import AlteValidari


class ManageStudenti:
    """
    clasa care manageriaza studentii, avand un repository si un validator specifice
    """
    def __init__(self, repository, validator):
        """
        creeaza un manager de studenti si salveaza datele in repository si le valideaza cu ajutorul validatorului
        :param repository: obiect de tipul ListaStudenti
        :param validator: obiect de tipul StudentValidator
        """
        self.__repository = repository
        self.__validator = validator

    def __make_id_stud(self):
        """
        obtine un nou id pentru un viitor student care urmeaza a fi creat
        :return: id pt student
        """
        lista_id = list(self.__repository.getlista().keys())
        lista_id.append(100)
        ids = max(lista_id)
        while self.__exist_id_service(ids):
            ids = ids + 1
        return ids

    def adauga_student_service(self, params):
        """
        se adauga un student la lista actuala de studenti stocata in __repository
        :param params: lista de parametri care contin datele dupa urmatorul model:
                        1. un singur element -> acesta este numele studentului
                        2. doua elemente -> primul va fi id-ul daca nu este deja alocat, iar al doilea nume student
        :return: -
        :raises:    ValueError cu urmatoarele mesaje:
                        "Numar parametri invalid!" daca nu este corect numarul parametrilor
                        "Student existent!" daca exista deja un student cu acelasi id in lista
                        ValueError pentru validare:
                            daca studentID < 0 sau daca studentID nu este intreg -> "Id invalid"
                            daca nume == "" -> "Nume student invalid!"
        """
        if len(params) == 1:
            nume = params[0]
            ids = self.__make_id_stud()
        elif len(params) == 2:
            ids = params[0]
            nume = params[1]
        else:
            raise ValueError("Numar parametri invalid!")
        stud = Student(ids, nume)
        try:
            self.__validator.validare(stud)
        except ValueError as ve:
            raise ValueError(ve)
        try:
            self.__repository.adauga_student(stud)
        except ValueError as ve:
            raise ValueError(ve)

    def __sterge_student_service(self, stud):
        """
        sterge studentul stud din repository
        :param stud: obiect de tip Student
        :return: -
        :raises ValueError cu mesajul "Student inexistent!" daca nu exista studentul stud in repository
        """
        self.__repository.sterge_student(stud)

    def sterge_student_id_service(self, params):
        """
        sterge studentul cu id-ul primit prin lista de parametri din repository
        :param params: lista de parametri cu un singur element: id-ul
        :return: -
        :raises: ValueError cu mesajul "Student inexistent!" daca nu exista studentul stud cu ids in repository
                                       "ID student invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        ids = params[0]
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError:
            raise ValueError("ID student invalid!")
        try:
            stud = self.__repository.get_stud_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        self.__sterge_student_service(stud)

    def __modifica_nume_student_service(self, stud, nume_nou):
        """
        modifica numele obiectului de tip Student aflat in repository cu numele primit prin parametru
        :param stud: obiect de tipul Student
        :param nume_nou: string nevid
        :return: -
        """
        self.__repository.modifica_nume_student(stud, nume_nou)

    def modifica_nume_student_id_service(self, params):
        """
        modifica numele obiectului de tip Student cu id-ul din params aflat in repository cu numele primit prin params
        :param params: lista de doua elemente; primul este id-ul studentului, cel de-al doilea noul nume
        :return: -
        :raises: ValueError cu diferite mesaje:
                        "Student inexistent!" daca nu exista studentul stud in repository
                        "Nume invalid!" daca nume_nou este vid
                        "ID student invalid!" daca id-ul introdus nu este intreg pozitiv
                        "Numar parametri invalid!" daca nu sunt doar doua elemente in params
        """
        erori = ""
        validari = AlteValidari()
        if len(params) == 2:
            ids = params[0]
            nume_nou = params[1]
            try:
                validari.validare_id(ids)
            except ValueError:
                erori += "ID student invalid!\n"
            try:
                validari.validare_nume(nume_nou)
            except ValueError:
                erori += "Nume student invalid!\n"
            if len(erori) > 0:
                erori = erori[:-1]
                raise ValueError(erori)
        else:
            raise ValueError("Numar parametri invalid!")
        try:
            stud = self.__repository.get_stud_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        self.__modifica_nume_student_service(stud, nume_nou)

    def get_all_studenti_service(self):
        """
        sunt returnate toate obiectele de tip Student din repository
        :return: lista[dictionatul] din repository
        :raises: ValueError cu mesajul "Nu exista niciun student introdus!" daca lista este goala
        """
        if self.__repository.getlenlista() == 0:
            raise ValueError("Nu exista niciun student introdus!")
        else:
            return self.__repository.getlista()

    def get_student_id_service(self, params):
        """
        returneaza studentul din repository cu id-ul primit in params
        :param params: lista de elemente: contine doar id-ul intreg pozitiv
        :return: obiect de tip Student
        :raises: ValueError cu diverse mesaje:
                        "ID student invalid!" daca id-ul introdus nu este intreg pozitiv
                        "Numar parametri invalid!" daca nu sunt doar doua elemente in params
                        "Student inexistent!" daca nu exista studentul cu id-ul introdus in repository
        """
        if len(params) != 1:
            raise ValueError("Numar parametri invalid!")
        ids = params[0]
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError as ve:
            raise ValueError("ID student invalid!")
        try:
            stud = self.__repository.get_stud_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        return stud

    def __exist_id_service(self, ids):
        """
        verifica daca exista id-ul ids in dictionarul de obiecte studenti
        :param ids: id de tip intreg pozitiv
        :return:    True daca exista acest ids in dictionarul de studenti
                    False daca nu exista acest ids in dictionarul de studenti
        :raises:    ValueError cu mesajul "ID invalid!" daca nr_id nu poate fi id
        """
        if ids in self.__repository.getlista():
            return True
        return False

    def __get_nume_student_service(self, stud):
        """
        returneaza numele studentului daca acesta se afla in repository
        :param stud: obiect de tipul Student
        :return: numele studentului stud
        :raises: ValueError cu mesajul: "Student inexistent!" daca nu exista studentul stud in repository
        """
        return stud.getnume()

    def get_nume_student_id_service(self, ids):
        """
        returneaza numele studentului cu id-ul ids daca acesta se afla in repository
        :param ids: id-ul studentului
        :return: numele studentului stud
        :raises: ValueError cu mesajul: "Student inexistent!" daca nu exista studentul stud in repository
                                        "ID student invalid!" daca id-ul introdus nu este intreg pozitiv
        """
        validari = AlteValidari()
        try:
            validari.validare_id(ids)
        except ValueError:
            raise ValueError("ID student invalid!")
        try:
            stud = self.__repository.get_stud_from_id(ids)
        except ValueError as ve:
            raise ValueError(ve)
        return self.__get_nume_student_service(stud)

    def get_nr_studenti_service(self):
        """
        se returneaza numarul de studenti aflati in repository
        :param params: lista goala []
        :return: numarul de studenti aflati in repository
        """
        return self.__repository.getlenlista()

    def cauta_studenti_service(self, params):
        """
        functia cauta studenti care au in nume subnumele primit prin params
        :param params: lista de parametri, o parte din nume
        :return: o lista de keys reprezentand id-ul studentilor
        :raises: ValueError cu mesajul: "Numar parametri invalid!" daca nu sunt doar doua elemente in params
                                        "Nume invalid!" daca secventa de nume introdus este vida
        """
        validare = AlteValidari()
        if len(params) != 1:
            raise ValueError("Numar parametri invalid!")
        nume = params[0]
        try:
            validare.validare_nume(nume)
        except ValueError as ve:
            raise ValueError("Nume student invalid!")
        # keys = []
        # nume = nume.lower()
        # for key in self.__repository.getlista():
        #     if nume in self.__repository.getlista()[key].getnume().lower():
        #         keys.append(key)
        # urmeaza o metoda recursiva
        lista_studenti = list(self.__repository.getlista().values())
        keys = cauta_studenti_cu_nume(lista_studenti, nume)
        return keys

    def studenti_random_service(self, nr_stud):
        if nr_stud <= 0:
            raise ValueError("Numar de studenti invalid!")
        lista_stud_random = RandomStudent()
        lista_stud_random.genereaza_studenti(nr_stud)
        lista_nume_studenti_generati = lista_stud_random.getlista_nume_random()
        for i in range(nr_stud):
            self.adauga_student_service([lista_nume_studenti_generati[i]])

    def sterge_toti_studentii(self):
        """
        sterge toti studentii din repository-ul de studenti
        :return: -
        """
        self.__repository.del_all()

    def auto_populare_studenti_service(self):
        """
        functia care autopopuleaza lista de studenti cu studenti creati in prealabil
        :return: -
        """
        self.adauga_student_service(["Sava Lucian"])
        self.adauga_student_service(["Chirita Narcisa"])
        self.adauga_student_service(["Stanescu Florin"])
        self.adauga_student_service(["Dumitru Viorela"])
        self.adauga_student_service(["Nistor Lucian"])
        self.adauga_student_service(["Dumitrescu Dorin"])
        self.adauga_student_service(["Stanciu Codrut"])
        self.adauga_student_service(["Diaconu Sebastian"])
        self.adauga_student_service(["Ciocarlan Alexandra"])
        self.adauga_student_service(["Diaconu Alexandru"])
        self.adauga_student_service(["Chirita Nicoleta"])
        self.adauga_student_service(["Stanciu Nicolae"])
        self.adauga_student_service(["Muresan Dumitru"])
        self.adauga_student_service(["Georgescu Paul"])
        self.adauga_student_service(["Pop Cezar"])
        self.adauga_student_service(["Pop Bogdan Ionel"])
