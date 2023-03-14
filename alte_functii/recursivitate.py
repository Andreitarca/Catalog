def cauta(lista, element, pozitie=0):
    """
    functie de cautare al unui element intr-o lista
    :param lista: lista de elemente
    :param element: un element
    :param pozitie: pozitia de la care se incepe, 0 by default
    :return:    True daca se gaseste acel element in lista
                False altfel
    """
    '''
                            ---- complexitate ----
            base case:  elementul se afla pe prima pozitie in lista
                            complexitatea: = O(1)
            worst case: elementul pe care il cautam se afla pe ultima pozitie sau nu se afla deloc in lista
                            complexitatea: = O(n)
            average case: depinde de pozitia elementului in lista sau daca se afla in lista
                            complexitatea: = O(n)
    '''
    if pozitie >= len(lista):
        return False
    elif lista[pozitie] == element:
        return True
    else:
        return cauta(lista, element, pozitie + 1)

def cauta_studenti_cu_nume(lista, nume, lista_noua=None):
    """
    functie de cautare a studentilor cu nume in numele lor
    :param lista: lista de studenti - values din dictionar
    :param nume: secventa de nume care va fi cautat
    :param lista_noua: lista noua in care vor fi returnate listele - optionala
    :return: lista cu id-urile studentilor
    """
    '''
                            ---- complexitate ----
            toate cazurile sunt egale => O(n) - se itereaza de fiecare data prin toata lista
    '''
    if lista_noua is None:
        lista_noua = []
    if not lista:
        return lista_noua
    else:
        if nume.lower() in lista[0].getnume().lower():
            lista_noua.append(lista[0].getid())
        return cauta_studenti_cu_nume(lista[1:], nume, lista_noua)

def sterge_note(lista_note, id_entitate, key, lista_noua=None):
    """
    functie care ia din lista_note initiala doar notele care nu au id-ul entitatii egale cu cel dat
    :param lista_note: lista de note
    :param id_entitate: id_disciplina sau id_student, ale caror note se vor sterge
    :param key: keyul de acces al id-urilor - fie al disciplinei, fie al studentului
    :param lista_noua: lista finala
    :return: lista_noua
    """
    '''
                            ---- complexitate ----
            toate cazurile sunt egale => O(n) - se itereaza de fiecare data prin toata lista
    '''
    if lista_noua is None:
        lista_noua = {}
    if not lista_note:
        return lista_noua
    else:
        if key(lista_note[0]) != id_entitate:
            lista_noua[lista_note[0].getid()] = lista_note[0]
        return sterge_note(lista_note[1:], id_entitate, key, lista_noua)

