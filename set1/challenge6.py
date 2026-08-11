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

def base64_to_bytes() -> bytes:

    # Ler ficheiro e remover newlines
    with open("challenge6.txt") as f:
        text = f.read().replace("\n", "")

    return base64.b64decode(text)

def get_keysize() -> int:
    scores = []
    file_bytes = base64_to_bytes()

    for keysize in range(2, 41):
        blocks = [file_bytes[i : i+keysize] for i in range(0, len(file_bytes), keysize)]

        # taking the first four blocks for each keysize
        pairs = min(len(blocks) - 1, 4)

        total = 0
        for i in range(pairs):
            total += hamming_distance(blocks[i], blocks[i+1])

        normalized = total / (pairs * keysize)

        scores.append((normalized, keysize))

    scores.sort()
    return scores[0][1]

print(get_keysize())

def transposing_blocks() -> str:
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

def result() -> str:
    blocks = transposing_blocks()
    scores = []

    for i in range(len(blocks)):
        cipher_bytes = blocks[i]

        best_score = -999999
        best_plaintext = None
        
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
                best_plaintext = plaintext

        scores.append([best_score, best_plaintext])

    return scores

#print(result())

