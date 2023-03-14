from validating.alte_validari import AlteValidari


class StudentValidator:
    def validare(self, student):
        """
        valideaza daca studentul introdus are toate atributele valide
        :param student: Student
        :return: -
        :raises: ValueError daca datele din student sunt invalide:
                            daca studentID < 0 sau daca studentID nu este intreg -> "Id invalid\n"
                            daca nume == "" -> "Nume invalid!\n"
        """
        erori = ""
        validari = AlteValidari()
        try:
            validari.validare_id(student.getid())
        except ValueError as ve:
            erori += "ID student invalid!\n"
        if len(student.getnume()) == 0:
            erori += "Nume student invalid!\n"
        if len(erori) > 0:
            erori = erori[:-1]
            raise ValueError(erori)

class DisciplinaValidator:
    def validare(self, disciplina):
        """
        valideaza daca disciplina introdusa are toate atributele valide
        :param disciplina:
        :return: -
        :raises: ValueError daca datele din disciplina sunt invalide:
                        daca disciplinaID < 0 sau daca studentID nu este intreg -> "Id invalid\n"
                        daca nume == "" -> "Nume invalid!\n"
                        daca prof == "" -> "Nume profesor invalid!\n"
        """
        erori = ""
        validari = AlteValidari()
        try:
            validari.validare_id(disciplina.getid())
        except ValueError as ve:
            erori += "ID disciplina invalid!\n"
        if len(disciplina.getnume()) == 0:
            erori += "Nume disciplina invalid!\n"
        if len(disciplina.getprof()) == 0:
            erori += "Nume profesor invalid!\n"
        if len(erori) > 0:
            erori = erori[:-1]
            raise ValueError(erori)


class NoteValidator:
    def validare(self, nota):
        """
        valideaza daca nota introdusa are toate atributele valide
        :param nota: Student
        :return: -
        :raises: ValueError daca datele din nota sunt invalide:
                            daca notaID < 0 sau daca notaID nu este intreg -> "ID invalid\n"
                            daca studentul este invalid -> "Student invalid!\n"
                            daca disciplina este invalida -> Disciplina invalida!\n"
                            daca valoarea este invalida (nu e cuprinsa intre 1 si 10) -> "Nota invalida!\n"
        """
        erori = ""
        validari = AlteValidari()
        try:
            validari.validare_id(nota.getid())
        except ValueError:
            erori += "ID nota invalid!\n"
        try:
            validari.validare_id(nota.getid_student())
        except ValueError:
            erori += "ID student invalid!\n"
        try:
            validari.validare_id(nota.getid_disciplina())
        except ValueError:
            erori += "ID disciplina invalid!\n"
        try:
            validari.validare_valoare_nota(nota.getnota())
        except ValueError as ve:
            erori += str(ve)
            erori += '\n'
        if len(erori) > 0:
            erori = erori[:-1]
            raise ValueError(erori)
