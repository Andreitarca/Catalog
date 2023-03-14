import string
import random


class RandomStudent:
    def __init__(self):
        self.__list = []

    def genereaza_studenti(self, nrstud):
        for i in range(nrstud):
            nr_char = random.randint(4, 20)
            nume = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + " ", k=nr_char))
            self.__list.append(nume)

    def getlista_nume_random(self):
        return self.__list


class RandomDisciplina:
    def __init__(self):
        self.__list = []

    def genereaza_discipline(self, nrdisc):
        for i in range(nrdisc):
            nr_char = random.randint(4, 20)
            nume = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + " ", k=nr_char))
            nr_char = random.randint(4, 20)
            prof = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + " ", k=nr_char))
            disciplina = []
            disciplina.append(nume)
            disciplina.append(prof)
            self.__list.append(disciplina)

    def getlista_nume_prof_random(self):
        return self.__list
