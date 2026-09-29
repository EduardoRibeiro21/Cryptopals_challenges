from Crypto.Cipher import AES
import base64

# To convert the file in bytes
def base64_to_bytes() -> bytes:

    # Reading the file and removing newlines
    with open("challenge7.txt") as f:
        text = f.read().replace("\n", "")

    return base64.b64decode(text)

"""For this challenge, we need to use the pycryptodome library, because it contains
pre-builts to simply decrypt files encripted in AES.
We don´t need to reinvent the wheel :)"""

def result():
    ciphertext = base64_to_bytes()
    key = b"YELLOW SUBMARINE"

    aes = AES.new(key, AES.MODE_ECB)
    plaintext = aes.decrypt(ciphertext)

    return plaintext.decode("latin-1")

print(result())