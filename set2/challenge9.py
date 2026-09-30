def padding(plaintext: bytes, block_size: int) -> bytes:
    appending_number = block_size - (len(plaintext) % block_size)

    for _ in range(appending_number):
        plaintext += bytes([appending_number])

    return plaintext

plaintext = b"YELLOW SUBMARINE"

print(padding(plaintext, 20))