import base64

# working!
def hamming_distance(text1: bytes, text2: bytes) -> int:
    result = 0

    for x, y in zip(text1, text2):
        temp = bin(x^y)

        for bit in temp:
            if bit == "1":
                result += 1

    return result

# To convert the file in bytes
def base64_to_bytes() -> bytes:

    # Reading the file and removing newlines
    with open("challenge6.txt") as f:
        text = f.read().replace("\n", "")

    return base64.b64decode(text)

'''To obtain the keysize, we need all combinations of hamming_distances between
4 consecutive blocks'''
def get_keysize() -> int:
    scores = []
    file_bytes = base64_to_bytes()

    for keysize in range(2, 41):
        b1 = file_bytes[0 : keysize]
        b2 = file_bytes[keysize : 2 * keysize]
        b3 = file_bytes[2 * keysize : 3 * keysize]
        b4 = file_bytes[3 * keysize : 4 * keysize]

        distances = [hamming_distance(b1, b2),
                     hamming_distance(b1, b3),
                     hamming_distance(b1, b4),
                     hamming_distance(b2, b3),
                     hamming_distance(b2, b4),
                     hamming_distance(b3, b4)]

        normalized = (sum(distances) / len(distances)) / keysize
        scores.append((normalized, keysize))

    scores.sort()
    return scores[0][1]

def transposing_blocks() -> list:
    keysize = get_keysize()
    file_bytes = base64_to_bytes()
    columns = []

    blocks = [file_bytes[i : i+keysize] for i in range(0, len(file_bytes), keysize)]

    for i in range(keysize):
        col = []
        for block in blocks:
            if i < len(block):
                col.append(block[i])
        columns.append(bytes(col))

    return columns

# Score method used in another challenges
def score_plaintext(plaintext: str) -> int:
    score = 0

    for ch in plaintext:
        c = ord(ch)

        if c < 32 and c not in (9, 10, 13):  # tab, \n, \r
            score -= 5
            continue
        if c > 126:
            score -= 5
            continue

        if ch == " ":
            score += 3

        if ch.lower() in "etaoinshrdlu":
            score += 2

        if ch.isalpha():
            score += 1
        if ch in ".,:;!?'":
            score += 1

    return score

def decrypt_key() -> bytes:
    blocks = transposing_blocks()
    key_bytes = []

    for i in range(len(blocks)):
        cipher_bytes = blocks[i]

        best_score = -999999
        best_key = None
        
        # 2) testing all possible keys
        for key in range(256):
            # XOR
            candidate_bytes = bytes(b ^ key for b in cipher_bytes)

            # bytes → text
            plaintext = candidate_bytes.decode("latin-1")

            # scoring
            score = score_plaintext(plaintext)

            if score > best_score:
                best_score = score
                best_key = key

        key_bytes.append(best_key)

    return bytes(key_bytes)

# With the key found, this becomes simple, right?
def result():
    key = decrypt_key()
    file_bytes = base64_to_bytes()

    plaintext_bytes = []

    for i, c in enumerate(file_bytes):
        plaintext_bytes.append(c ^ key[i % len(key)])

    result = bytes(plaintext_bytes)
    return result.decode("latin-1")

print(result())

