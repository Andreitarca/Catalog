from exceptions.exceptions import SortingException


def sortare(lista: list, key=lambda k: k, nume_sortare="Selection_Sort", reverse=False, cmp=lambda x, y: x<y):
    """
    functie de sortare creata asemanator celei din python
    :param cmp: regula de comparare
    :param lista: o lista de elemente
    :param key: key-ul dupa care se vor ordona elementele
    :param nume_sortare: se va alege care algoritm se va utiliza din cele doua
    :param reverse:     False daca va fi ordonata crescator
                        True daca va fi ordonata descrescator
    :return: lista ordonata
    :raise SortingException cu mesajul "Nu exista aceasta sortare implementata inca!"
    """
    if nume_sortare == "Selection_Sort":
        sortare_selection = SelectionSort(lista, key, reverse, cmp)
        lista_noua = sortare_selection.sortare()
        return lista_noua
    elif nume_sortare == "Shake_Sort":
        sortare_shake = ShakeSort(lista, key, reverse, cmp)
        lista_noua = sortare_shake.sortare()
        return lista_noua
    else:
        raise SortingException("Nu exista aceasta sortare implementata inca!")


class SelectionSort:
    """
    algoritm de sortare prin selectie
    """
    def __init__(self, lista, key, reverse, cmp):
        self.__lista = lista
        if type(key) is tuple:
            self.__key = key[0]
            if len(key) > 1:
                self.__key2 = key[1]
            else:
                self.__key2 = None
        else:
            self.__key = key
            self.__key2 = None
        self.__reverse = reverse
        self.__cmp = cmp

    def sortare(self):
        '''
                            ---- complexitate ----
            base case:  lista e deja sortata -> se parcurge totul
                            complexitatea: = O(n^2) - n*(n+1)
            worst case: lista e sortata in ordine inversa -> se va executa totul de n ori
                            complexitatea: = O(n^2) - n*(n+1)*2
            average case: depinde
                            complexitatea: = O(n^2)
        '''
        if self.__reverse:
            for i in range(0, len(self.__lista) - 1):
                index = i
                for j in range(i + 1, len(self.__lista)):
                    if self.__cmp(self.__key(self.__lista[index]), self.__key(self.__lista[j])):
                        index = j
                    elif self.__key2 is not None:
                        if not self.__cmp(self.__key(self.__lista[j]), self.__key(self.__lista[index])):
                            if self.__cmp(self.__key2(self.__lista[index]), self.__key2(self.__lista[j])):
                                index = j
                if i < index:
                    aux = self.__lista[index]
                    self.__lista[index] = self.__lista[i]
                    self.__lista[i] = aux
        else:
            for i in range(0, len(self.__lista) - 1):
                index = i
                for j in range(i + 1, len(self.__lista)):
                    if self.__cmp(self.__key(self.__lista[j]), self.__key(self.__lista[index])):
                        index = j
                    elif self.__key2 is not None:
                        if not self.__cmp(self.__key(self.__lista[index]), self.__key(self.__lista[j])):
                            if self.__cmp(self.__key2(self.__lista[j]), self.__key2(self.__lista[index])):
                                index = j
                if i < index:
                    aux = self.__lista[index]
                    self.__lista[index] = self.__lista[i]
                    self.__lista[i] = aux
        return self.__lista


class ShakeSort:
    """
    algoritm de sortare shake - cocktail
    """
    def __init__(self, lista, key, reverse, cmp):
        self.__lista = lista
        if type(key) is tuple:
            self.__key = key[0]
            if len(key) > 1:
                self.__key2 = key[1]
            else:
                self.__key2 = None
        else:
            self.__key = key
            self.__key2 = None
        self.__reverse = reverse
        self.__cmp = cmp

    def sortare(self):
        '''
                            ---- complexitate ----
            base case:  lista e deja sortata -> se parcurge odata lista
                            complexitatea: = O(n)
            worst case: lista e sortata in ordine inversa -> se va executa totul de n ori
                            complexitatea: = O(n^2)
            average case: depinde
                            complexitatea: = O(n^2)
        '''
        if self.__reverse:
            start = 0
            end = len(self.__lista) - 1
            swapped = True
            while swapped:
                swapped = False
                for i in range(start, end):
                    if self.__cmp(self.__key(self.__lista[i]), self.__key(self.__lista[i+1])):
                        aux = self.__lista[i]
                        self.__lista[i] = self.__lista[i + 1]
                        self.__lista[i + 1] = aux
                        swapped = True
                    elif self.__key2 is not None:
                        if not self.__cmp(self.__key(self.__lista[i+1]), self.__key(self.__lista[i])):
                            if self.__cmp(self.__key2(self.__lista[i]), self.__key2(self.__lista[i+1])):
                                aux = self.__lista[i]
                                self.__lista[i] = self.__lista[i + 1]
                                self.__lista[i + 1] = aux
                                swapped = True

                if not swapped:
                    break

                swapped = True
                end = end - 1
                for i in range(end - 1, start - 1, -1):
                    if self.__cmp(self.__key(self.__lista[i]), self.__key(self.__lista[i+1])):
                        aux = self.__lista[i]
                        self.__lista[i] = self.__lista[i + 1]
                        self.__lista[i + 1] = aux
                        swapped = True
                    elif self.__key2 is not None:
                        if not self.__cmp(self.__key(self.__lista[i+1]), self.__key(self.__lista[i])):
                            if self.__cmp(self.__key2(self.__lista[i]), self.__key2(self.__lista[i+1])):
                                aux = self.__lista[i]
                                self.__lista[i] = self.__lista[i + 1]
                                self.__lista[i + 1] = aux
                                swapped = True

                start = start + 1

        else:
            start = 0
            end = len(self.__lista) - 1
            swapped = True
            while swapped:
                swapped = False
                for i in range(start, end):
                    if self.__cmp(self.__key(self.__lista[i+1]), self.__key(self.__lista[i])):
                        aux = self.__lista[i]
                        self.__lista[i] = self.__lista[i + 1]
                        self.__lista[i + 1] = aux
                        swapped = True
                    elif self.__key2 is not None:
                        if not self.__cmp(self.__key(self.__lista[i+1]), self.__key(self.__lista[i])):
                            if self.__cmp(self.__key2(self.__lista[i+1]), self.__key2(self.__lista[i])):
                                aux = self.__lista[i]
                                self.__lista[i] = self.__lista[i + 1]
                                self.__lista[i + 1] = aux
                                swapped = True
                if not swapped:
                    break

                swapped = True
                end = end - 1
                for i in range(end - 1, start - 1, -1):
                    if self.__cmp(self.__key(self.__lista[i+1]), self.__key(self.__lista[i])):
                        aux = self.__lista[i]
                        self.__lista[i] = self.__lista[i + 1]
                        self.__lista[i + 1] = aux
                        swapped = True
                    elif self.__key2 is not None:
                        if not self.__cmp(self.__key(self.__lista[i+1]), self.__key(self.__lista[i])):
                            if self.__cmp(self.__key2(self.__lista[i+1]), self.__key2(self.__lista[i])):
                                aux = self.__lista[i]
                                self.__lista[i] = self.__lista[i + 1]
                                self.__lista[i + 1] = aux
                                swapped = True

                start = start + 1
        return self.__lista