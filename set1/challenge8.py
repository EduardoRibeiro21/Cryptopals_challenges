"""In this challenge, to detect the ciphertext encrypted with ECB, we need to
determine the ciphertext with the most repeated occurences of 16 bytes blocks.

We don´t need to know what block has been repeated, we just only have the compute
the number of repeated occurences in general, for each ciphertext."""

def count_repeated_blocks(ciphertext: str) -> int:
    cipherbytes = bytes.fromhex(ciphertext)

    blocks = set()
    for i in range(0, len(cipherbytes), 16):
        blocks.add(cipherbytes[i : i+16])

    return len(cipherbytes) - len(blocks)

def solve() -> int:
    with open("challenge8.txt") as f:
        max_score = -1
        best_line = None
        count = 1

        for line in f:
            score = count_repeated_blocks(line)
            if score > max_score:
                max_score = score
                best_line = count

            count += 1

    return best_line

print(solve())