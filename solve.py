# Given a list of plaintext candidates, and a ciphertext,
# Returns a guess index.
# Assumes encryption scheme from mono.py
def solve(plaintext_candidates: list[str], ciphertext: str) -> int | None:
    len_plaintext = len(plaintext_candidates[0])
    # Check if the plaintext_candidates have equal length
    for i in range(1, len(plaintext_candidates)):
        if len(plaintext_candidates[i]) != len_plaintext:
            print("Inconsistent plaintext candidate length!")
            return None
    len_ciphertext = len(ciphertext)
    # Check if the ciphertext has correct length
    if len_ciphertext < len_plaintext:
        print("Ciphertext is too short!")
        return None
    result1 = frequency_matching(plaintext_candidates, ciphertext)
    return result1


def frequency_matching(plaintexts: list[str], ciphertext: str) -> int | None:
    distributions = []
    for plaintext in plaintexts:
        distributions.append(gen_frequency_dist(plaintext))
    cipher_dist = gen_frequency_dist(ciphertext)
    best_idx = None
    best_value = 27.0
    for i in range(len(plaintexts)):
        val = chi_squared_distance(distributions[i], cipher_dist)
        if val < best_value:
            best_idx = i
            best_value = val
    return best_idx


def gen_frequency_dist(text: [str]) -> []:
    frequencies = [0.0] * 27
    for char in text:
        frequencies[alpha_index(char)] += 1.0
    for i in range(len(frequencies)):
        frequencies[i] /= len(text)
    return sorted(frequencies)


def chi_squared_distance(observed: [], expected: []) -> float:
    sum = 0.0
    for i in range(27):
        if expected[i] == 0.0:
            continue
        sum += (observed[i] - expected[i]) ** 2 / expected[i]
    return sum


# Brute force. Deterministic and gauranteed to be correct.
# Only efficient when noise is very small.
def brute_force(
    plaintexts: list[str],
    ciphertext: str,
) -> int | None:
    n_noise = len(ciphertext) - len(plaintexts[0])
    for i in range(len(plaintexts)):
        # print(f"{plaintexts[i]}")
        if brute_force_test(plaintexts[i], ciphertext, [None] * 27, n_noise, 0, 0):
            return i
    return None


def alpha_index(character: chr) -> int:
    if character == " ":
        return 26
    return ord(character) - ord("a")


def brute_force_test(
    plaintext: str,
    ciphertext: str,
    mono_table,
    noise_left: int,
    plaintext_index: int,
    ciphertext_index: int,
) -> bool:
    # Given a character on a ciphertext, it is either a random char, or a
    # substitution of plaintext
    if ciphertext_index == len(ciphertext):
        return plaintext_index == len(plaintext) and noise_left == 0
    cipher_chr = ciphertext[ciphertext_index]
    # Assume cipher_chr is a random char:
    if noise_left > 0:
        if brute_force_test(
            plaintext,
            ciphertext,
            mono_table,
            noise_left - 1,
            plaintext_index,
            ciphertext_index + 1,
        ):
            return True
    # Otherwise it must be a substitution
    offset = alpha_index(cipher_chr)
    to_match = plaintext[plaintext_index]
    # Check if it is plusible
    # 1. Check it has already been mapped:
    for i in range(len(mono_table)):
        if mono_table[i] == to_match:
            if i != offset:
                return False
            else:
                return brute_force_test(
                    plaintext,
                    ciphertext,
                    mono_table,
                    noise_left,
                    plaintext_index + 1,
                    ciphertext_index + 1,
                )
    # 2. Item has not been matched, try create one if not already occupied
    # If there is anything in it still, it is not good.
    if mono_table[offset] is not None:
        return False
    table_copy = mono_table.copy()
    table_copy[offset] = plaintext[plaintext_index]
    return brute_force_test(
        plaintext,
        ciphertext,
        table_copy,
        noise_left,
        plaintext_index + 1,
        ciphertext_index + 1,
    )
