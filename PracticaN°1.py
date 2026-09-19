"""
1) Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
elementos que se encuentran en A o en B, o en ambos.

2) Dados dos conjuntos, A y B, escribe un programa en Python que imprima los
elementos que se encuentran en A y en B

3) Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

4) Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
un subconjunto de otro conjunto, B.

5) Dados un conjunto, A, escribe un programa en Python que imprima el número de
elementos del conjunto
"""

import random


def generarNumeros(cantElementos):

    listaNumeros = []
    cont=0


    while cont < cantElementos:
    
        num = random.randint(1,20)

        if num not in listaNumeros:

            listaNumeros.append(num)
            cont += 1

    return listaNumeros



def manipularConjuntos(conjuntoResultante, textoUno, textoDos):

    listElementos = list(conjuntoResultante)

    if len(listElementos) == 0:

        print(textoUno)

    else:
        print(textoDos, end=" ")

        for numero in listElementos:

            print(f"{numero}", end=" ")

        print("\n\n")

    

def ingresoOpcion():

    print("\n\n1) Dados dos conjuntos, A y B, escribe un programa en Python que imprima los\nelementos que se encuentran en A o en B, o en ambos.\n\n2) Dados dos conjuntos, A y B, escribe un programa en Python que imprima los\nelementos que se encuentran en A y en B\n\n3) Dados dos conjuntos, A y B, escribe un programa en Python que imprima el\nconjunto de los elementos que se encuentran en A o en B, pero no en ambos.\n\n4) Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto\nes un subconjunto de otro conjunto, B.\n\n5) Dados un conjunto, A, escribe un programa en Python que imprima el número de\nelementos del conjunto")

    opcion = input("\n\nSeleccione una opción: ")

    return (True, opcion) if opcion.isdigit() else (False, opcion)


def inicio():

    conjuntoA = set(generarNumeros(6))
    conjuntoB = set(generarNumeros(10))

    opElegida = ingresoOpcion()

    if (not opElegida[0] or int(opElegida[1]) not in (1,2,3,4,5)):

        print("\nERROR. Opción invalida.")

    else: 

        match int(opElegida[1]):
    
            case 1:
                print(f"\n\nEjercicio 1:\n")
                print(f"Conjunto A: {conjuntoA}")
                print(f"Conjunto B: {conjuntoB}")
                
                manipularConjuntos((conjuntoA | conjuntoB), " ", "\nElementos en común entre el conjunto A y el conjunto B: ")
    
            case 2:
                print(f"\n\nEjercicio 2:\n")
                print(f"Conjunto A: {conjuntoA}")
                print(f"Conjunto B: {conjuntoB}")

                manipularConjuntos((conjuntoA & conjuntoB), "\nNo existen elementos coincidentes entre el conjunto A y el conjunto B", "\nElementos en común entre el conjunto A y el conjunto B:")

            case 3:
                print(f"\n\nEjercicio 3:\n")
                print(f"Conjunto A: {conjuntoA}")
                print(f"Conjunto B: {conjuntoB}")

                manipularConjuntos((conjuntoA ^ conjuntoB), "\nEl conjunto A y el conjunto B contienen los mismos elementos", "\nElementos no coincidentes entre el conjunto A y el conjunto B:")

            case 4:
                print(f"\n\nEjercicio 4:\n")
                print(f"Conjunto A: {conjuntoA}")
                print(f"Conjunto B: {conjuntoB}")

                print("\nEl conjunto A es un subconjunto del conjunto B") if (conjuntoA <= conjuntoB) else print("\nEl conjunto A no es un subconjunto del conjunto B")

            case 5:
                print(f"\n\nEjercicio 5:\n")
                print(f"Conjunto A: {conjuntoA}")
                print(f"\nEl conjunto A posee {len(list(conjuntoA))} elementos.\n\n")



inicio()