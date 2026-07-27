# This function does the same as bytes.fromhex
def hex_to_bytes(hex_string: str) -> bytes:
    if len(hex_string) % 2 != 0:
        raise ValueError(f"Hex com comprimento ímpar: {hex_string}")

    result = []

    for i in range(0, len(hex_string), 2):
        pair = hex_string[i:i+2]

        # converting each digit
        high = pair[0]
        low = pair[1]

        # converting hex → decimal
        if '0' <= high <= '9':
            high_val = ord(high) - ord('0')
        else:
            high_val = ord(high) - ord('a') + 10

        if '0' <= low <= '9':
            low_val = ord(low) - ord('0')
        else:
            low_val = ord(low) - ord('a') + 10

        byte = high_val * 16 + low_val
        result.append(byte)

    return bytes(result)

def xor_buffers(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])

# This function does the same as the built-in method .hex()
def bytes_to_hex(b: bytes) -> str:
    res = ""
    for byte in b:
        res += format(byte, "02x")       # converts to hex with 2 digits
    return res

hex_string1 = "1c0111001f010100061a024b53535009181c"
hex_string2 = "686974207468652062756c6c277320657965"

result = xor_buffers(hex_to_bytes(hex_string1), hex_to_bytes(hex_string2))
print(bytes_to_hex(result))