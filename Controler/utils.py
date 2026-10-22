def cautare_recursiva_lista(lista, id_cautat, index=0):
    """
    Cauta recursiv un element intr-o lista care are metoda get_id()
    Complexity: O(n)
    lista(list): lista de elemente
    id_cautat(int): id cautat
    index(int): index
    """
    if index >= len(lista):
        return None

    if lista[index].get_id() == id_cautat:
        return lista[index]

    return cautare_recursiva_lista(lista, id_cautat, index + 1)


def filter_by_gen_recursiv(lista, gen, index=0, rezultat=None):
    """
    Filtreaza recursiv o lista de studenti dupa gen.
    Complexity: O(n)
    lista(list): lista de studenti dupa gen
    gen(str): gen de studenti dupa gen
    rezultat(list): lista de studenti dupa gen

    """
    if rezultat is None:
        rezultat = []

    if index >= len(lista):
        return rezultat

    student = lista[index]
    if student.get_gen().lower() == gen.lower():
        rezultat.append(student)

    return filter_by_gen_recursiv(lista, gen, index + 1, rezultat)

def generic_sort(rezultat, key, algorithm, reverse=False):
    """
    Algoritm bubble sort / shell sort
    :param rezultat(list): Lista de sortat
    :param key: Functie lambda pentru extragerea valorii de comparatie
    :param reverse(bool): True pentru descrescator, False pentru crescator
    :param algorithm(str): 'bubble' sau 'shell'
    """
    arr = list(rezultat)
    n = len(arr)

    def is_greater(a, b):
        val_a = key(a) if key else a
        val_b = key(b) if key else b
        if reverse:
            return val_a < val_b
        else:
            return val_a > val_b

    if algorithm == 'bubble':
        """
        Best Case   O(n)    Lista deja sortată (datorită flag-ului swapped).
        Average Case    O(n^2)  Performanța tipică; lent pe liste mari.
        Worst Case  O(n^2)  Lista inversată (necesită maximul de schimburi).
        """
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if is_greater(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

    elif algorithm == 'shell':
        """
        Best Case   (n \log n)  Lista deja sortată.
        Average Case approx O(n^{1.5})  Performanța tipică pe date random.
        Worst Case O(n^2)   Secvența n/2 nu amestecă pozițiile pare/impare până la final.
        """
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and is_greater(arr[j - gap], temp):
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    return arr