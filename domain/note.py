class Nota:
    """
    clasa Nota ne creeaza note dupa un model predefinit, cu functiile aferente
    o nota are 4 atribute:  id-ul, care este un numar intreg pozitiv unic identificabil
                            studentul, care este un obiect de tip Studenti
                            disciplina, care este un obiect de tip Disciplina
                            valoarea, care este un float cuprins intre 1 si 10
    """
    __no_inst = 10

    def __init__(self, id_nota, id_student, id_disciplina, nota):
        """
        ne cream o nota cu cele 4 atribute
        :param id_nota: care este un numar intreg pozitiv unic identificabil
        :param id_student: obiect de tip id_student
        :param disciplina: obiect de tip disciplina
        :param nota: valoarea notei
        """
        self.__idnota = id_nota
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina
        self.__nota = nota
        Nota.__no_inst += 1

    def getid(self):
        """
        returneaza id-ul obiectului nota la care se apeleaza metoda
        :return: id-ul obiectului nota la care se apeleaza metoda
        """
        return self.__idnota

    def getnota(self):
        """
        returneaza valoarea notei obiectului nota
        :return: valoarea notei obiectului nota
        """
        return self.__nota

    def getid_student(self):
        """
        returneaza id-ul obiectului student pt nota la care se apeleaza metoda
        :return: id-ul obiectului student pt nota la care se apeleaza metoda
        """
        return self.__id_student

    def getid_disciplina(self):
        """
        returneaza id-ul obiectului disciplina pt nota la care se apeleaza metoda
        :return: id-ul obiectului disciplina pt nota la care se apeleaza metoda
        """
        return self.__id_disciplina

    def setnota(self, nota_noua):
        """
        modifica valoarea obiectului nota la valoarea primita prin parametrul nota_noua
        :param nota_noua: valoare pt nota
        :return: -
        """
        self.__nota = nota_noua

    def __eq__(self, Nota2):
        if self.__idnota == Nota2.getid():
            return True
        else:
            return False

    def __lt__(self, Nota2):            # pt comparare tre ambele sa fie False
        return self.__nota < Nota2.getnota()

    def __gt__(self, Nota2):
        return self.__nota > Nota2.getnota()

    def __str__(self):
        return f"Nota cu ID-ul [{self.__idnota}] si valoarea {self.__nota} atribuita " \
               f"studentului cu ID-ul [{self.__id_student}] " \
               f"la disciplina cu ID-ul [{self.__id_disciplina}]"

    @staticmethod
    def get_no_inst():
        """
        returneaza numarul de instante create pana in momentul apelarii, dar se incepe de la 10(6 cu tot cu teste)
        :return: numarul de instante create pana in momentul apelarii
        """
        return Nota.__no_inst
