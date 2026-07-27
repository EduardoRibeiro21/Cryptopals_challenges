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

# As you can see, "etaoinshrdlu" are 12 of the 13 letters with most occurence.
# The whitespaces are also very important to consider.


# score function based on "etaoin shrdlu"
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
    # 1) hex → bytes
    cipher_bytes = bytes.fromhex(hex_string)

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

    return [best_score, best_plaintext]


def solve():
    values = []

    with open("challenge4.txt") as f:
        for line in f:
            hex_string = line.strip().lower()  # removing \n, spaces, and converting to lower-case
            if not hex_string:                 # ignoring blank lines
                continue
            values.append(result(hex_string))

    max_val = -float('inf')
    index = 0

    for i in range(len(values)):
        if values[i][0] > max_val:
            max_val = values[i][0]
            index = i

    return values[index]

print(solve())