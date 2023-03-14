class AlteValidari:

    def validare_id(self, nr_id):
        """
        valideaza daca elementul primit prin parametrul nr_id poate fi un id intreg si pozitiv
        :param nr_id: posibil int
        :return: id-ul daca e int pozitivd
        :raises: ValueError cu mesajul "ID invalid!" daca nr_id nu poate fi id
        """
        if nr_id < 0:
            raise ValueError("ID invalid!")

    def validare_nume(self, nume):
        """
        valideaza daca stringul primit prin parametrul nume poate fi un nume(nu este vid)
        :param nume: string
        :return: -
        :raises: ValueError cu mesajul "String vid!" daca nu poate fi nume
        """
        if len(nume) == 0:
            raise ValueError("String vid!")

    def validare_valoare_nota(self, valoare):
        """
        valideaza daca elementul primit prin parametru este un float cuprins intre 1 si 10
        :param valoare: posibil float pt nota
        :return: -
        :raises: ValueError cu mesajul "Nota invalida" daca valoare nu este un float cuprins intre 1 si 10
        """
        valoare_f = float(valoare)
        if not(1 <= valoare_f <=10):
            raise ValueError("Valoare nota invalida!")