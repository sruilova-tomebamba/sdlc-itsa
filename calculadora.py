
# Función para calcular la potencia
def calcular_potencia(base, exponente):
    """
    Calcula la potencia de un número.
    base: el número base.
    exponente: el número exponente.
    """
    return base ** exponente

# FUNCION DE DIVISION

def dividir_numeros(num1, num2):
    try:
        resultado = num1 / num2
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."
    except TypeError:
        return "Error: Los valores deben ser números."

    # Ejemplo de uso
    #numero1 = 10
    #numero2 = 2
    #ividir_numeros(numero1, numero2)
    
# Función para multiplicar
def multiplicar(a, b):
    return a * b
