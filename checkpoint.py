# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def DividirDosNumeros(dividendo, divisor):
    '''
    Esta función devuelve dos valores, la parte entera de la división y su resto
    Recibe dos argumentos:
        dividendo: El número que va a ser dividido
        divisor: El número que va a dividir
    Ej:
        DividirDosNumeros(10,3) debe retornar 3, 1
    '''
    #Tu código aca:
    parte_entera = None
    resto = None

    resto = dividendo % divisor
    parte_entera = dividendo // divisor
    
    return parte_entera, resto
 

def ProximoPrimo(actual_primo):
    '''
    Esta función devuelve el número primo siguiente al enviado como parámetro.
    En caso de que el parámetro no sea de tipo entero y/o no sea un número primo, debe retornar nulo.
    Recibe un argumento:
        actual_primo: Será el número primo a partir del cual debo buscar el siguiente
    Ej:
        ProximoPrimo(7) debe retornar 11
        ProximoPrimo(8) debe retornar nulo
    '''
    #Tu código aca:
    def primo(n):
        primo  = True
        for i in range(2,n):
            if (n % i == 0):
                primo = False
                break
        return primo

    if type(actual_primo)!= int:
        return None
    elif primo(actual_primo) == False:
        return None
    else:
        siguiente_primo = actual_primo +1
        while(primo(siguiente_primo)==False):
            siguiente_primo = siguiente_primo +1       
    return siguiente_primo

def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    class Animal:
        def __init__(self,especie,color):
            self.color = color
            self.especie = especie
            self.edad = 0
        
        def CumplirAnios(self):
            self.edad += 1    
            return self.edad
    return Animal(especie, color)


