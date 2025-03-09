import sys

# Función KSA (Key Scheduling Algorithm) - Inicializa y mezcla S con la clave
def ksa(key):
    """Key Scheduling Algorithm (KSA) - Inicializa el estado S"""
    S = list(range(256))  # Crear lista con valores de 0 a 255
    j = 0
    
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256  # Mezcla S con la clave
        S[i], S[j] = S[j], S[i]  # Intercambio de valores en S
    
    return S

# Función PRGA (Pseudo-Random Generation Algorithm) - Genera el keystream
def prga(S, length):
    """Pseudo-Random Generation Algorithm (PRGA) - Genera la secuencia de cifrado"""
    i = j = 0  # Inicialización de los índices
    keystream = []  # Lista para almacenar el keystream
    
    for _ in range(length):
        i = (i + 1) % 256  # Avanzar i
        j = (j + S[i]) % 256  # Avanzar j
        S[i], S[j] = S[j], S[i]  # Intercambiar valores en S
        K = S[(S[i] + S[j]) % 256]  # Generar el siguiente byte del keystream
        keystream.append(K)
    
    return keystream

# Función principal para cifrar usando RC4
def rc4_encrypt(plaintext, key):
    """Cifra un mensaje usando RC4 y devuelve la salida en formato hexadecimal"""
    key = [ord(c) for c in key.strip()]  # Convertir la clave a valores ASCII
    plaintext = plaintext.strip()  # Eliminar espacios extra en el mensaje
    
    S = ksa(key)  # Inicializar S con la clave
    keystream = prga(S, len(plaintext))  # Generar el keystream con la misma longitud del mensaje
    
    # Aplicar XOR entre el mensaje y el keystream
    ciphertext = [ord(p) ^ k for p, k in zip(plaintext, keystream)]
    
    # Convertir el resultado a formato hexadecimal
    return ''.join(f"{byte:02X}" for byte in ciphertext)

# Leer entrada estándar (stdin)
lines = sys.stdin.read().split("\n")  # Leer todas las líneas y separarlas por saltos de línea
key = lines[0].strip()  # La primera línea es la clave
message = ''.join(lines[1:]).strip()  # El resto es el mensaje a cifrar

# Ejecutar la función de cifrado y mostrar el resultado
print(rc4_encrypt(message, key))
