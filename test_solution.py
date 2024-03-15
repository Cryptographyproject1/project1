import random
from genk import generate_key
from readP import read_plaintext
from mono import mono
from solve import solve
import string


def test(iter: int, p: float):
    plaintexts = read_plaintext("./s24_dictionary1.txt")
    message_space = list(string.ascii_lowercase + " ")
    success = 0
    for i in range(iter):
        plaintext = random.choice(plaintexts)
        key = generate_key(message_space)
        ciphertext = mono(key, plaintext, p)
        solution = solve(plaintexts, ciphertext)
        if plaintexts[solution] == plaintext:
            success += 1
    print(f"Success rate: {success / iter:.2%}")


if __name__ == "__main__":
    test(100, 0.05)
