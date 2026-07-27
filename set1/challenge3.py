# Occurrence of each letter of the alphabet in the English language
occurance_english = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}

# As you can see, "etaoinshrdlu" are the 12 letters with most occurence.
# The whitespaces are also very important to consider.

def hex_to_bytes(hex_string: str) -> bytes:
    return bytes.fromhex(hex_string)

def xor_with_key(byte_list, key):
    result = []
    for b in byte_list:
        result.append(b ^ key)
    return result

def bytes_to_text(byte_list: bytes) -> str:
    text = ""
    for b in byte_list:
        text += chr(b)      # each byte turns to a char
    return text

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

def result(hex_string: str) -> list:
    # 1) hex → bytes (manual)
    cipher_bytes = hex_to_bytes(hex_string)

    best_score = -999999
    best_plaintext = None
    
    # 2) testing all possible keys
    for key in range(256):
        # XOR
        candidate_bytes = xor_with_key(cipher_bytes, key)

        # bytes → text
        plaintext = bytes_to_text(candidate_bytes)

        # scoring
        score = score_plaintext(plaintext)

        if score > best_score:
            best_score = score
            best_plaintext = plaintext

    return [best_score, best_plaintext]

hex_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
print(result(hex_string))
