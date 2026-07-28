# working!
def hamming_distance(text1: bytes, text2: bytes) -> int:
    result = 0

    for x, y in zip(text1, text2):
        temp = bin(x^y)

        for bit in temp:
            if bit == "1":
                result += 1

    return result

