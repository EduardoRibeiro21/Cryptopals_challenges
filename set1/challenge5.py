def repeated_key_xor(plaintext: bytes, key: bytes):
    pt = plaintext
    len_key = len(key)
    encoded = []

    for i in range(len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])

    return bytes(encoded)

plaintext = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

print(repeated_key_xor(plaintext, b"ICE").hex())