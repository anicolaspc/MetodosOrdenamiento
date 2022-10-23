from typing import Sized


vec = [8, 5, 3, 9, 1, 4, 7]

tam = len(vec)
print(vec, end="   ")
print()


def orden(vec):
    if len(vec) > 1:
        n1 = int((len(vec) + 1) / 2)
        n2 = int(len(vec) - n1)

        izq = []
        der = []
        for i in range(0, n1):
            izq.append(vec[i])
        for i in range(0, n2):
            der.append(vec[i + n1])

        orden(izq)
        orden(der)
        mezclar(vec, izq, der)
        print(izq, end="   ")
        print("Izquierda    ")
        print(der, end="   ")
        print("Derecha   ")
        print(vec, end="   ")
        print("Completo   ")


def mezclar(vec, izq, der):
    v = 0
    i = 0
    d = 0
    while d < len(der) and i < len(izq):
        if der[d] > izq[i]:
            vec[v] = izq[i]
            i += 1
        else:
            vec[v] = der[d]
            d += 1
        v += 1

    while i < len(izq):
        vec[v] = izq[i]
        i += 1
        v += 1

    while d < len(der):
        vec[v] = der[d]
        d += 1
        v += 1


orden(vec)
