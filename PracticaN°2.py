import random

def ejercicioUno():

    """
    Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
    """

    numeroUno = random.randint(1,100)
    numeroDos = random.randint(0,5)

    try:
        resultado = numeroUno / numeroDos

    except ZeroDivisionError:

        print(f"\nError. No se puede dividir {numeroUno} por {numeroDos}.\n")
    
    else:

        print(f"\n{numeroUno} / {numeroDos} = {round(resultado,2)}\n")



def ejercicioDos():

    """
    Escribe un programa que intente sumar un número y una cadena. Si se produce un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
    """

    numero = random.randint(1,100)

    cadena = ["Hola mundo","Texto de prueba 123","ABC-123-XYZ","cadena_texto_ejemplo","Lorem ipsum dolor sit amet","usuario_2026","a8Kx92LmPq","Texto con espacios y símbolos: !@#$%","Esta es una cadena más larga para realizar pruebas"]

    try:

        resultado = numero + random.choice(cadena)
        print(resultado)

    except TypeError:

        print("\nError. No se puede sumar un número con una cadena de texto.\n")


def ejercicioTres():

    """
    Escribe un programa que intente acceder a una clave que no existe en un diccionario. Si se produce una excepción KeyError, captura la excepción y muestra
    """

    persona = {
        "nombre": "Juan",
        "edad": 25,
        "ciudad": "Buenos Aires"
    }

    try:

        print(f"La edad de {persona['nombre']} es {persona['años']}")

    except KeyError:

        print("\nError. Se intenta acceder a una clave que no existe en el diccionario.\n")


def ejercicioCuatro():

    """
    Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin embargo, también intenta crear el archivo si no existe.
    """

    nombre = "archivo.txt"

    try:      
        with open(nombre,"r") as archivo:

            for linea in archivo:

                print(linea)

    except FileNotFoundError:

        print("\nError. Se está intentado abrir un archivo inexistente.")
        print(f"\nSe creará un archivo llamado '{nombre}' para solucionar el problema.\n")

        with open(nombre, "w") as _:
            pass


def ejercicioCinco():

    """
    Escribe un programa que intente dividir dos números. Si el segundo número es cero, captura la excepción ZeroDivisionError. Si el primer número es un número no válido, captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
    """

    listElementos = ["2145","Hola mundo","1597","Lorem ipsum dolor sit amet","4952"]

    numeroDos = random.randint(0,2)

    try:

        numeroUno = int(random.choice(listElementos))

        resultado = numeroUno / numeroDos
        print(f"\n{numeroUno} / {numeroDos} = {resultado}\n")

    except ZeroDivisionError:

        print(f"\nError. No se puede dividir {numeroUno} por {numeroDos}.\n")

    except ValueError:

        print(f"\nError. El cociente debe ser un número.\n")


#Inicio del programa

numero = input("\nIngrese un numero entre 1 y 5: ")

if numero.isdigit():

    match int(numero):

        case 1:
            ejercicioUno()
        case 2:
            ejercicioDos()
        case 3:
            ejercicioTres()
        case 4:
            ejercicioCuatro()
        case 5:
            ejercicioCinco()
        case _:
            print("\nError.\n")

else:
    print("\nError.\n")