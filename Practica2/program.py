def TEA_Encrypt(v, k):
    """
    Función que cifra un bloque de 64 bits usando el algoritmo TEA (Tiny Encryption Algorithm).

    Parámetros:
    v : lista de dos enteros de 32 bits (bloque de datos a cifrar)
    k : lista de cuatro enteros de 32 bits (clave de 128 bits)

    Retorna:
    Una lista con dos enteros de 32 bits cifrados.
    """
    y, z = v  # División del bloque en dos partes de 32 bits
    sum_ = 0  # Inicialización de la suma
    delta = 0x9E3779B9  # Constante mágica derivada del número áureo
    n = 32  # Número de rondas (recomendado para TEA)

    while n > 0:
        sum_ = (sum_ + delta) & 0xFFFFFFFF  # Suma acumulada (mod 2^32)
        y = (y + (((z << 4) + k[0]) ^ (z + sum_) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF  # Actualización de y
        z = (z + (((y << 4) + k[2]) ^ (y + sum_) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF  # Actualización de z
        n -= 1

    return [y, z]  # Retorna el bloque cifrado

def TEA_Decrypt(v, k):
    """
    Función que descifra un bloque de 64 bits cifrado con TEA.

    Parámetros:
    v : lista de dos enteros de 32 bits (bloque cifrado)
    k : lista de cuatro enteros de 32 bits (clave de 128 bits)

    Retorna:
    Una lista con dos enteros de 32 bits descifrados.
    """
    y, z = v
    delta = 0x9E3779B9
    sum_ = (delta << 5) & 0xFFFFFFFF  # sum_ = delta * 32 (valor inicial de suma)
    n = 32

    while n > 0:
        z = (z - (((y << 4) + k[2]) ^ (y + sum_) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF  # Reverso de z
        y = (y - (((z << 4) + k[0]) ^ (z + sum_) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF  # Reverso de y
        sum_ = (sum_ - delta) & 0xFFFFFFFF  # Disminuye la suma
        n -= 1

    return [y, z]  # Retorna el bloque descifrado

def parse_hex_list(line):
    """
    Convierte una línea de texto con valores hexadecimales separados por comas
    en una lista de enteros.

    Ejemplo:
    '0x01234567,0x89ABCDEF' -> [19088743, 2309737967]
    """
    return [int(x, 16) for x in line.strip().split(',')]

def main():
    """
    Función principal que lee datos desde la entrada estándar,
    determina el modo de operación (encriptar o desencriptar),
    y ejecuta la función correspondiente.
    """
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]  # Lee todas las líneas no vacías

    mode = lines[0]           # Primer línea: 'E' para cifrar o 'D' para descifrar
    block = parse_hex_list(lines[1])  # Segundo línea: bloque de datos (dos hex)
    key = parse_hex_list(lines[2])    # Tercera línea: clave (cuatro hex)

    # Ejecuta según el modo
    if mode == 'E':
        result = TEA_Encrypt(block, key)
    elif mode == 'D':
        result = TEA_Decrypt(block, key)
    else:
        print("Modo inválido")
        return

    # Imprime el resultado en formato hexadecimal
    print(f"0x{result[0]:08X},0x{result[1]:08X}")

# Punto de entrada
if __name__ == "__main__":
    main()
