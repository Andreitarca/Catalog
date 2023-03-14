class SefPromotieDTO:
    """
    clasa ne creeeaza un obiect cu studentul si media sa
    """
    def __init__(self, id_stud, nume_stud, media):
        self.__idsef = id_stud
        self.__nume = nume_stud
        self.__media = media

    def getid(self):
        return self.__idsef

    def getnume(self):
        return self.__nume

    def getmedia(self):
        return self.__media

    def __str__(self):
        return f"Student cu ID-ul [{self.__idsef}] si numele '{self.__nume}' cu media {round(self.__media, 2)}"
