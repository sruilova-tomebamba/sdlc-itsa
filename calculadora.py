<<<<<<< HEAD
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
=======
def multiplicar(a, b):
    return a * b
>>>>>>> c04764d47bcb7fde65743af8b782a315a5318d34
