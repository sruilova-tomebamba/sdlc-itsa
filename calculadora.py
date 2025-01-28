# Función para sumar
def suma():
    numero_uno = int(input("Introduce el primer número: "))
    numero_dos = int(input("Introduce el segundo número: "))
    resultado = numero_uno + numero_dos 
    
    return resultado

# Función para calcular la potencia
def calcular_potencia(base, exponente):
    """
    Calcula la potencia de un número.
    base: el número base.
    exponente: el número exponente.
    """
    return base ** exponente

# FUNCION DE DIVISION
def dividir_numeros(numero_uno, numero_dos):
    try:
        resultado = numero_uno / numero_dos
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Los valores deben ser números."
    
# Función para multiplicar
def multiplicar(numero_uno, numero_dos):
    return numero_uno * numero_dos

# Función resta
def resta (numero_uno , numero_dos):
    return numero_uno - numero_dos
