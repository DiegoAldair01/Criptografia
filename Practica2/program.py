def TEA_Encrypt(v, k):
    y, z = v
    sum_ = 0
    delta = 0x9E3779B9
    n = 32

    while n > 0:
        sum_ = (sum_ + delta) & 0xFFFFFFFF
        y = (y + (((z << 4) + k[0]) ^ (z + sum_) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF
        z = (z + (((y << 4) + k[2]) ^ (y + sum_) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF
        n -= 1

    return [y, z]

def TEA_Decrypt(v, k):
    y, z = v
    delta = 0x9E3779B9
    sum_ = (delta << 5) & 0xFFFFFFFF  # delta * 32
    n = 32

    while n > 0:
        z = (z - (((y << 4) + k[2]) ^ (y + sum_) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF
        y = (y - (((z << 4) + k[0]) ^ (z + sum_) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF
        sum_ = (sum_ - delta) & 0xFFFFFFFF
        n -= 1

    return [y, z]

def parse_hex_list(line):
    return [int(x, 16) for x in line.strip().split(',')]

def main():
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]

    mode = lines[0]
    block = parse_hex_list(lines[1])
    key = parse_hex_list(lines[2])

    if mode == 'E':
        result = TEA_Encrypt(block, key)
    elif mode == 'D':
        result = TEA_Decrypt(block, key)
    else:
        print("Modo inválido")
        return

    print(f"0x{result[0]:08X},0x{result[1]:08X}")

if __name__ == "__main__":
    main()
