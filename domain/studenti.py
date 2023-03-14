class Student:
    """
    clasa Student ne creeaza studenti dupa un model predefinit, cu functiile aferente
    un student are doua atribute:   id-ul, care este un numar intreg pozitiv unic identificabil
                                    numele, care este un string care nu poate fi vid
    """
    __no_inst = 0

    def __init__(self, studentID, nume):
        """
        ne cream un student nou cu cele doua atribute
        :param nume: string non vid
        :param studentID: numar intreg pozitiv unic identificabil
        """
        self.__studentID = studentID
        self.__nume = nume
        Student.__no_inst += 1

    def getid(self):
        """
        returneaza id-ul obiectului student la care se apeleaza metoda
        :return: id-ul obiectului student la care se apeleaza metoda
        """
        return self.__studentID

    def getnume(self):
        """
        returneaza numele obiectului student la care se apeleaza metoda
        :return: numele obiectului student la care se apeleaza metoda
        """
        return self.__nume

    def setnume(self, nume_nou):
        """
        modifica numele obiectului student la numele primit prin parametrul nume_nou
        :param nume_nou: string nevid
        :return: -
        """
        self.__nume = nume_nou

    # def to_string(self):
        # return f"Studentul cu ID-ul [{self.__studentID}] si cu numele {self.__nume}"

    def __eq__(self, Stud2):
        """
        suprascrie metoda obiectului student de comparare
        astfel doi studenti sunt "egai" daca au acelasi id
        :param Stud2: obiect de tipul Student
        :return:    True daca cele doua obiecte sunt egale
                    False daca cele doua obiecte nu sunt egale
        """
        if self.__studentID == Stud2.getid():
            return True
        return False
        # si la stergere am egale de ex pt functia if student in lista

    def __str__(self):
        """
        suprascrie metoda obiectului student de afisare
        :return: un string pretty printing ale atributelor obicetului student
        """
        return f"Student cu ID-ul [{self.__studentID}] si cu numele '{self.__nume}'"

    @staticmethod
    def get_no_inst():
        """
        returneaza numarul de instante create pana in momentul apelarii, dar se incepe de la 100(88 cu tot cu teste)
        :return: numarul de instante create pana in momentul apelarii
        """
        return Student.__no_inst
