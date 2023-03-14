class Disciplina:
    """
    clasa Disciplina ne creeaza discipline dupa un model predefinit, cu functiile aferente
    o disciplina are trei atribute:     id-ul, care este un numar intreg pozitiv unic identificabil
                                        numele, care este un string care nu poate fi vid
                                        profesor, care este numele profesorului care preda, care este un string non-vid
    """
    __no_inst = 0

    def __init__(self, idDisciplina, nume, profesor):
        """
        ne cream o disciplina cu cele trei atribute
        :param nume: string non vid
        :param profesor: string non vid
        :param idDisciplina: numar intreg pozitiv unic identificabil
        """
        self.__vdisciplina = {}
        self.__vdisciplina["id"] = idDisciplina
        self.__vdisciplina["nume"] = nume
        self.__vdisciplina["prof"] = profesor
        Disciplina.__no_inst += 1

    def getid(self):
        """
        returneaza id-ul obiectului disciplina la care se apeleaza metoda
        :return: id-ul obiectului disciplina la care se apeleaza metoda
        """
        return self.__vdisciplina["id"]

    def getnume(self):
        """
        returneaza numele obiectului disciplina la care se apeleaza metoda
        :return: numele obiectului disciplina la care se apeleaza metoda
        """
        return self.__vdisciplina["nume"]

    def getprof(self):
        """
        returneaza numele profesorului obiectului disciplina la care se apeleaza metoda
        :return: numele profesorului obiectului disciplina la care se apeleaza metoda
        """
        return self.__vdisciplina["prof"]

    def setnume(self, nume_nou):
        """
        modifica numele obiectului disciplina la numele primit prin parametrul nume_nou
        :param nume_nou: string nevid
        :return: -
        """
        self.__vdisciplina["nume"] = nume_nou

    def setprof(self, prof_nou):
        """
        modifica numele profesorului obiectului disciplina la numele primit prin parametrul nume_nou
        :param prof_nou: string nevid
        :return: -
        """
        self.__vdisciplina["prof"] = prof_nou

    def __eq__(self, Disc2):
        """
        suprascrie metoda obiectului disciplina de comparare
        astfel doua discipline sunt "egale" daca au acelasi id
        :param Disc2: obiect de tipul Disciplina
        :return:    True daca cele doua obiecte sunt egale
                    False daca cele doua obiecte nu sunt egale
        """
        if self.__vdisciplina["id"] == Disc2.getid():
            return True
        return False

    def __str__(self):
        """
        suprascrie metoda obiectului disciplina de afisare
        :return: un string pretty printing ale atributelor obicetului disciplina
        """
        return f"Disciplina cu ID-ul [{self.__vdisciplina['id']}], numele '{self.__vdisciplina['nume']}'" \
               f" cu profesorul '{self.__vdisciplina['prof']}'"

    @staticmethod
    def get_no_inst():
        """
        returneaza numarul de instante create pana in momentul apelarii, dar se incepe de la 10(6 cu tot cu teste)
        :return: numarul de instante create pana in momentul apelarii
        """
        return Disciplina.__no_inst
