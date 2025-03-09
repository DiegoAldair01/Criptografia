import sys

def suma_numeros():
    # Leer números desde la entrada estándar (stdin)
    numeros = [int(line.strip()) for line in sys.stdin if line.strip()]
    
    # Calcular la suma
    total = sum(numeros)
    
    # Imprimir el resultado en la salida estándar (stdout)
    print(total)

# Ejecutar la función
suma_numeros()
