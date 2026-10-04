import random

def ejercicioUno():

    """ 
    Calcular el mayor de dos números ingresados por teclado usando un operador ternario
    """

    def comprobarNum(numero):

        return isinstance(numero, (int, float)) 
            

    def ingresoNumero():

        return input("Ingrese un número: ")


    def mayor():

        print("")

        numeroUno = ingresoNumero()
        numeroDos = ingresoNumero()

        if comprobarNum(numeroUno) or comprobarNum(numeroDos) or numeroUno in ("", " ") or numeroDos in ("", " "):

            print("\nERROR. Debe ingresar solamente números.")

        else:

            print(f"\n{numeroUno} es mayor que {numeroDos}\n") if numeroUno > numeroDos else print(f"\n{numeroDos} es mayor que {numeroUno}\n")

           
    mayor()



def ejercicioDos():

    """
    Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario
    """

    def ingresoDatos():

        texto = input("\nIngrese una frase: ").split()

        return texto

    def comprobacionTexto(texto):

        flag = False

        for elemento in texto:
        
            if elemento.isdigit():

                flag = True
                break

        return flag


    def busquedaPalabra(*arg):

        texto = ""

        palabra = input("Indique la palabra a buscar: ")

        if comprobacionTexto(arg) or palabra.isdigit() or arg in ("", " ") or palabra in ("", " "):
            
            print("ERROR. Debe ingresar solo palabras.")
                    
        else:

            for elemento in arg:

                texto += (f"{elemento} ")

            print(f"\nFrase ingresada: {texto}")
            print(f"Palabra a buscar: {palabra}")

            print(f"\nLa palabra '{palabra}' es parte de la frase ingresada.\n") if palabra in texto else print(f"\nLa palabra '{palabra}' no es parte de la frase ingresada.\n") 


    busquedaPalabra(*ingresoDatos())



def ejercicioTres():

    """
    Determinar si un número es par o impar
    """

    numero = random.randint(1,1000)

    print(f"\n{numero} es un número par\n" if numero % 2 == 0 else f"\n{numero} es un número impar\n")



def ejercicioCuatro(*arg):

    """
    Calcular el promedio de una lista de números usando args y un operador ternario
    """

    flag = False

    for elemento in arg:

        if isinstance(elemento, str):

            flag = True
            break

    if flag:

        print("\nPara calcular correctamente el promedio, la totalidad de los elementos deben ser números.\n")

    else:

        print("\nNo se puede calcular el promedio porque no existen números para calcularlo.\n") if len(arg) == 0 else (print(f"\nNúmeros: {arg}") ,print(f"El promedio es: {sum(arg)/len(arg)}\n"))



def ejercicioCinco(*arg):

    """
    Imprimir un mensaje de error si no se pasan suficientes argumentos
    """

    cadena = ""
    flag = False
    
    if len(arg) == 3:

        for elemento in arg:

            if isinstance(elemento, str):

                cadena += (f"{elemento} ")
            else:

                flag = True
                break

        print("\nERROR. No se permiten números.\n") if flag else print(f"\nBuenos días, {cadena}\n")

    else:
        print("\nDebe introducir su nombre completo, cada elemento que compone su nombre deberá ser enviado como parametro. Debe estar compuesto al menos con tres palabras.\n")


def inicio():

    num = input("Ingrese un número entre 1 y 5: ")

    if num.isdigit() and int(num) in (1,2,3,4,5):

        match int(num):

            case 1:
                ejercicioUno()
            case 2:
                ejercicioDos()
            case 3:
                ejercicioTres()
            case 4:
                ejercicioCuatro(23,57,80,25)
            case 5:
                ejercicioCinco("Franco","Gabriel","Orellana")
    else:
        print("Opción incorrecta.")

inicio()