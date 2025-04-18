def kid_krypto(mode, a, b, A, B, message):
    # Paso 1: Calcular M, e, d, n
    M = a * b - 1
    e = A * M + a
    d = B * M + b
    n = (e * d - 1) // M

    if mode == 'E':  # Encriptar
        x = int(message)
        y = (x * e) % n
        return y
    elif mode == 'D':  # Desencriptar
        y = int(message)
        x = (y * d) % n
        return x
    else:
        raise ValueError("Modo no válido. Usa 'E' para encriptar o 'D' para desencriptar.")

# Leer los datos de entrada
if __name__ == "__main__":
    mode = input().strip()  # 'E' o 'D'
    a = int(input())
    b = int(input())
    A = int(input())
    B = int(input())
    message = int(input())

    result = kid_krypto(mode, a, b, A, B, message)
    print(result)
