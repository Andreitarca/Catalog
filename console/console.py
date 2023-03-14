from colorama import Fore

from controller.controller_note import ManageNote


class Console:
    def __init__(self, service_studenti, service_discipline, service_note:ManageNote):
        self.__service_studenti = service_studenti
        self.__service_discipline = service_discipline
        self.__service_note = service_note
        self.__comenzi = {
            "hello": self.__hello,
            "help": self.__help,

            "print_studenti": self.__print_all_students,
            "adauga_student": self.__adauga_student,
            "modifica_student": self.__modfica_student,
            "sterge_student": self.__sterge_student,
            "sterge_toti_studentii": self.__sterge_toti_studentii,
            "print_student": self.__print_student,
            "cauta_studenti": self.__cauta_studenti,
            "print_nr_studenti": self.__print_nr_studenti,
            "random_studenti": self.__random_studenti,
            "auto_populare_studenti": self.__auto_populare_studenti,

            "print_discipline": self.__print_all_discipline,
            "adauga_disciplina": self.__adauga_disciplina,
            "modifica_disciplina": self.__modifica_disciplina,
            "sterge_disciplina": self.__sterge_disciplina,
            "sterge_toate_disciplinele": self.__sterge_toate_disciplinele,
            "print_disciplina": self.__print_disciplina,
            "cauta_discipline": self.__cauta_discipline,
            "print_nr_discipline": self.__print_nr_discipline,
            "random_discipline": self.__random_discipline,
            "auto_populare_discipline": self.__auto_populare_discipline,

            "print_note": self.__print_all_note,
            "adauga_nota": self.__adauga_nota,
            "modifica_nota": self.__modifica_nota,
            "sterge_nota": self.__sterge_nota,
            "sterge_toate_notele": self.__sterge_toate_notele,
            "print_nr_note": self.__print_nr_note,
            "statistici_note_disc": self.__note_la_disciplina,
            "sef_promotie": self.__sef_promotie,
            "sef_promotie_to_file": self.__sef_promotie_file,
            "medii_disciplina": self.__medie_disciplina,
            "auto_populare_note": self.__auto_populare_note
        }

    def __hello(self):
        print(Fore.LIGHTBLUE_EX + "Salut\nBine ai venit la catalogul pentru gestioanarea studentilor si a disciplinelor" + Fore.RESET)
        print("Incepe prin a rula comenzi pentru a afla mai multe despre optiunile disponibile.\n")
        print("Pentru a afla modul de functionare a comenzilor, introdu:")
        print("help [nume_comanda]")
        print("Functionalitatile disponibile sunt: ")
        l_comenzi = list(self.__comenzi.keys())
        # regandit sa le pun tot cate 3 si aliniate pe mijloc si eventual si grupate idk
        comenzi_stud = [key for key in self.__comenzi.keys() if "studen" in key]
        comenzi_disc = [key for key in self.__comenzi.keys() if "discipli" in key]
        comenzi_note = [key for key in self.__comenzi.keys() if "not" in key]
        '''
        eventual consola pe bucati?
        sau idk cum sa fac.....
        '''
        # mda..mult mai bine grupate
        print("")
        print(Fore.LIGHTYELLOW_EX + "Comenzi pentru gestionarea studentilor: " + Fore.RESET)
        i = 0
        for comanda in comenzi_stud:
            print(comanda, end='\t\t\t')
            i += 1
            if i == 3:
                print("")
                i = 0
        print("")
        print(Fore.LIGHTMAGENTA_EX + "Comenzi pentru gestionarea disciplinelor: " + Fore.RESET)
        i = 0
        for comanda in comenzi_disc:
            print(comanda, end='\t\t\t')
            i += 1
            if i == 3:
                print("")
                i = 0
        print("")
        print(Fore.LIGHTCYAN_EX + "Comenzi pentru gestionarea notelor: " + Fore.RESET)
        i = 0
        for comanda in comenzi_note:
            print(comanda, end='\t\t\t')
            i += 1
            if i == 3:
                print("")
                i = 0
        print("")
        print(Fore.LIGHTBLUE_EX + "Pentru a inchide aplicatia, introdu: exit" + Fore.RESET)

    def __help(self, params):
        pass

    '''
    urmeaza partea de studenti
    '''

    def __print_all_students(self, params):
        if len(params) > 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        if self.__service_studenti.get_nr_studenti_service() == 0:
            print("Lista de studenti este vida!")
        else:
            for key in self.__service_studenti.get_all_studenti_service():
                print(self.__service_studenti.get_all_studenti_service()[key])

    def __print_student(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            params[0] = int(params[0])
        except ValueError:
            print(Fore.RED + "ID student invalid!" + Fore.RESET)
            return
        print(self.__service_studenti.get_student_id_service(params))

    def __print_nr_studenti(self, params):
        nr = self.__service_studenti.get_nr_studenti_service()
        if nr == 0:
            print("Nu exista niciun student introdus!")
        elif nr == 1:
            print(f"Exista un student introdus!")
        else:
            print(f"Exista {nr} studenti introdusi!")

    def __adauga_student(self, params):
        if not (len(params) == 1 or len(params) == 2):
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        if len(params) == 2:
            try:
                params[0] = int(params[0])
            except ValueError:
                print(Fore.RED + "ID student invalid!" + Fore.RESET)
                return
        self.__service_studenti.adauga_student_service(params)
        print(Fore.LIGHTGREEN_EX + f"Studentul a fost adaugat cu succes!" + Fore.RESET)

    def __modfica_student(self, params):
        if len(params) != 2:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            params[0] = int(params[0])
        except ValueError:
            print(Fore.RED + "ID student invalid!" + Fore.RESET)
            return
        self.__service_studenti.modifica_nume_student_id_service(params)
        print(Fore.LIGHTGREEN_EX + f"Studentului i-a fost modificat numele cu succes!" + Fore.RESET)

    def __sterge_student(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        # aici si de note ulterior
        # self.__service_studenti.sterge_student_id_service(params)
        try:
            id_stud = int(params[0])
        except ValueError:
            print(Fore.RED + "ID student invalid!" + Fore.RESET)
            return
        self.__service_note.sterge_student_si_notele_sale_service(id_stud)
        print(Fore.LIGHTGREEN_EX + "Studentul si notele sale au fost sterse cu succes!" + Fore.RESET)

    def __cauta_studenti(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        keys = self.__service_studenti.cauta_studenti_service(params)
        if len(keys) == 0:
            print("Nu s-a gasit niciun student!")
        else:
            for key in keys:
                print(self.__service_studenti.get_student_id_service([key]))

    def __random_studenti(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            nr_stud = int(params[0])
        except ValueError as ve:
            print(Fore.RED + "Numar de studenti invalid!" + Fore.RESET)
            return
        self.__service_studenti.studenti_random_service(nr_stud)
        print(Fore.LIGHTGREEN_EX + "Studentii generati random au fost adaugati cu succes!" + Fore.RESET)

    def __auto_populare_studenti(self, params):
        self.__service_studenti.auto_populare_studenti_service()
        print(Fore.LIGHTGREEN_EX + "Lista de studenti a fost autopopulata cu succes!" + Fore.RESET)


        #functie de sterge toti studentii si notele lor etc

    '''
    urmeaza partea de discipline
    '''

    def __print_all_discipline(self, params):
        if len(params) > 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        if self.__service_discipline.get_nr_discipline_service() == 0:
            print("Lista de discipline este vida!")
        else:
            for key in self.__service_discipline.get_all_discipline_service():
                print(self.__service_discipline.get_all_discipline_service()[key])

    def __adauga_disciplina(self, params):
        if not (len(params) == 2 or len(params) == 3):
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        if len(params) == 3:
            try:
                params[0] = int(params[0])
            except ValueError:
                print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
                return
        self.__service_discipline.adauga_disciplina_service(params)
        print(Fore.LIGHTGREEN_EX + f"Disciplina a fost adaugata cu succes!" + Fore.RESET)

    def __modifica_disciplina(self, params):
        if len(params) < 2 or len(params) > 3:  # aici alt numar
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            params[0] = int(params[0])
        except ValueError:
            print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
            return
        self.__service_discipline.modifica_disciplina_id_service(params)
        print(Fore.LIGHTGREEN_EX + f"Disciplina a fost modificata cu succes!" + Fore.RESET)

    def __sterge_disciplina(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        # aici si de note ulterior
        # self.__service_discipline.sterge_disciplina_id_service(params)
        try:
            disc_id = int(params[0])
        except ValueError:
            print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
            return
        self.__service_note.sterge_disciplina_si_note_service(disc_id)
        print(Fore.LIGHTGREEN_EX + "Disciplina si notele de la ea au fost stearse cu succes!" + Fore.RESET)

    def __print_disciplina(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            idd = int(params[0])
        except ValueError:
            print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
            return
        print(self.__service_discipline.get_disciplina_id_service(idd))

    def __cauta_discipline(self, params):
        if len(params) < 1 or len(params) > 2:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        keys = self.__service_discipline.cauta_discipline_service(params)
        if len(keys) == 0:
            print("Nu s-a gasit nicio disciplina!")
        else:
            for key in keys:
                print(self.__service_discipline.get_disciplina_id_service(key))

    def __print_nr_discipline(self, params):
        nr = self.__service_discipline.get_nr_discipline_service()
        if nr == 0:
            print("Nu exista nicio disciplina introdusa!")
        elif nr == 1:
            print(f"Exista o disciplina introdusa!")
        else:
            print(f"Exista {nr} discipline introduse!")

    def __random_discipline(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            nr_disc = int(params[0])
        except ValueError as ve:
            print(Fore.RED + "Numar de discipline invalid!" + Fore.RESET)
            return
        self.__service_discipline.discipline_random_service(nr_disc)
        print(Fore.LIGHTGREEN_EX + "Disciplinele generate random au fost adaugate cu succes!" + Fore.RESET)

    def __auto_populare_discipline(self, params):
        self.__service_discipline.auto_populare_discipline_service()
        print(Fore.LIGHTGREEN_EX + "Lista de discipline a fost autopopulata cu succes!" + Fore.RESET)

    '''
    urmeaza partea de note
    '''

    def __print_all_note(self, params):                 # print toate notele unui student la o disciplina
        if len(params) > 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        if self.__service_note.get_nr_note_service() == 0:
            print("Lista de note este vida!")
        else:
            for key in self.__service_note.get_all_note_string_service():
                print(self.__service_note.get_all_note_string_service()[key])

    def __print_nr_note(self, params):
        nr = self.__service_note.get_nr_note_service()
        if nr == 0:
            print("Nu exista nicio nota introdusa!")
        elif nr == 1:
            print(f"Exista o nota introdusa!")
        else:
            print(f"Exista {nr} note introduse!")

    def __adauga_nota(self, params):
        comenzi_id = {
            "studid": "ceva",
            "discid": "atlcv"
        }
        params2 = {
            "notaid": -1,
            "studid": 0.1,
            "discid": 0.1,
            "val": 0.1
        }
        okid = False
        if not (len(params) == 3 or len(params) == 4):
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        j = 0
        if len(params) == 4:
            okid = True
            try:
                params[0] = int(params[0])
                params2["notaid"] = params[0]
            except ValueError:
                print(Fore.RED + "ID nota invalid!" + Fore.RESET)
                return
            j = 1
        for i in range(j, len(params)):
            split = params[i].split(":")
            if len(split) == 2:
                comanda = split[0]  # aici ii baiu
                comanda = comanda.strip()
                if comanda in comenzi_id:
                    idp = split[1]
                    idp = idp.strip()
                    try:
                        idp = int(idp)
                    except ValueError:
                        if comanda == "studid":
                            print(Fore.RED + "ID student invalid!" + Fore.RESET)
                        else:
                            print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
                        return
                    if comanda == "studid":
                        if params2[comanda] != 0.1:
                            print(Fore.RED + "Ati introdus deja ID-ul pentru student!" + Fore.RESET)
                            return
                    else:
                        if params2[comanda] != 0.1:
                            print(Fore.RED + "Ati introdus deja ID-ul pentru disciplina!" + Fore.RESET)
                            return
                    params2[comanda] = idp
                elif comanda == "val":
                    val = split[1]
                    val = val.strip()
                    try:
                        val = float(val)
                    except ValueError:
                        print(Fore.RED + "Valoarea notei este invalida!" + Fore.RESET)
                        return
                    if params2["val"] != 0.1:
                        print(Fore.RED + "Ati introdus deja valoarea notei!" + Fore.RESET)
                        return
                    params2["val"] = val
                else:
                    print(Fore.RED + "Comanda invalida!" + Fore.RESET)
                    return
            else:
                print(Fore.RED + "Comanda invalida!" + Fore.RESET)
                return
        for key in params2.keys():
            if params2[key] == 0.1:
                if key == "studid":
                    print(Fore.RED + "Nu ati introdus ID-ul studentului!" + Fore.RESET)
                elif key == "discid":
                    print(Fore.RED + "Nu ati introdus ID-ul disciplinei!" + Fore.RESET)
                elif key == "val":
                    print(Fore.RED + "Nu ati introdus valoarea notei!" + Fore.RESET)
        params = []
        if okid:
            params.append(params2["notaid"])
        params.append(params2["studid"])
        params.append(params2["discid"])
        params.append(params2["val"])
        self.__service_note.adauga_nota_service(params)
        print(Fore.LIGHTGREEN_EX + f"Nota a fost adaugata cu succes!" + Fore.RESET)

    def __modifica_nota(self, params):
        if len(params) != 2:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            id_nota = int(params[0])
        except ValueError:
            print(Fore.RED + "ID nota invalid!" + Fore.RESET)
            return
        try:
            val_nota = float(params[1])
        except ValueError:
            print(Fore.RED + "Valoare nota invalida!" + Fore.RESET)
            return
        self.__service_note.modifica_valoare_nota_service(id_nota, val_nota)
        print(Fore.LIGHTGREEN_EX + f"Nota a fost modificata cu succes!" + Fore.RESET)

    def __sterge_nota(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            idnota = int(params[0])
        except ValueError:
            print(Fore.RED + "ID nota invalid!" + Fore.RESET)
            return
        self.__service_note.sterge_nota_id_service(idnota)
        print(Fore.LIGHTGREEN_EX + "Nota a  fost stearsa cu succes!" + Fore.RESET)

    def __note_la_disciplina(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        parametru = params[0]
        try:
            idd = int(parametru)
        except ValueError:
            print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
            return
        l_alf, l_note = self.__service_note.get_note_disc(idd)      # aici iarasi cu nume sau cu id si caut in controller
        l_alf = self.__service_note.make_str_nota(l_alf)
        l_note = self.__service_note.make_str_nota(l_note)
        print("\nLista ordonata alfabetic este:")
        for el in l_alf:
            print(el)
        print("\nLista ordonata dupa note este:")
        for el in l_note:
            print(el)

    def __sef_promotie(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        lista_rez = self.__service_note.sefpromotie()
        for el in lista_rez:
            print(el)

    def __sef_promotie_file(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        lista_rez = self.__service_note.sefpromotie_to_file()
        for el in lista_rez:
            print(el)

    def __medie_disciplina(self, params):
        if len(params) != 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        try:
            id_disc = int(params[0])
        except ValueError as ve:
            print(Fore.RED + "ID disciplina invalid!" + Fore.RESET)
            return
        l1, l2 = self.__service_note.medie_generala_disciplina(id_disc)
        print("Medii studenti ordonati descrescator dupa medie:")
        for el in l1:
            print(el)
        print()
        print("Medii studenti ordonati crescator dupa nume:")
        for el in l2:
            print(el)

    def __sterge_toate_notele(self, params):
        if len(params) > 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        self.__service_note.sterge_toate_notele()
        print(Fore.LIGHTGREEN_EX + "Toate notele au fost sterse cu succes!" + Fore.RESET)

    def __sterge_toate_disciplinele(self, params):
        if len(params) > 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        self.__service_note.sterge_toate_disciplinele_si_notele()
        print(Fore.LIGHTGREEN_EX + "Toate disciplinele si toate notele au fost sterse cu succes!" + Fore.RESET)

    def __sterge_toti_studentii(self, params):
        if len(params) > 1:
            print(Fore.RED + "Numar parametri invalid!" + Fore.RESET)
            return
        self.__service_note.sterge_toti_studentii_si_notele()
        print(Fore.LIGHTGREEN_EX + "Toti studentii si toate notele au fost sterse cu succes!" + Fore.RESET)

    def __auto_populare_note(self, params):
        try:
            nr = int(params[0])
        except ValueError as ve:
            print(Fore.RED + "Numar de note invalid!" + Fore.RESET)
            return
        self.__service_studenti.auto_populare_studenti_service()
        self.__service_discipline.auto_populare_discipline_service()
        self.__service_note.auto_populare_note_service(nr)
        print(Fore.LIGHTGREEN_EX + "Lista de note a fost autopopulata cu succes!" + Fore.RESET)

    '''
    urmeaza partea de run
    '''

    def start(self):
        self.__hello()
        while True:
            comanda = input(">>> ")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                print(Fore.LIGHTMAGENTA_EX + "La revedere!" + Fore.RESET)
                return
            if comanda == "hello":
                self.__hello()
                continue

            parti = comanda.split()
            nume_comanda = parti[0]
            if nume_comanda in self.__comenzi:
                lungime_nume = len(nume_comanda) + 1
                parte = comanda[lungime_nume:]
                params = parte.split(",")
                for i in range(len(params)):
                    params[i] = params[i].strip()
                try:
                    self.__comenzi[nume_comanda](params)
                except ValueError as ve:
                    print(Fore.RED + str(ve) + Fore.RESET)
            else:
                print(Fore.RED + "Comanda invalida!" + Fore.RESET)
