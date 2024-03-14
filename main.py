import random
from genk import generate_key
from readP import read_plaintext
from mono import mono


def main():
    plaintext_l = read_plaintext('./s24_dictionary1.txt')
    plaintext = random.choice(plaintext_l)
    print(plaintext)
    message_space = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    key = generate_key(message_space)
    print(key)
    ciphertext = mono(key, plaintext, 0.05)
    print(ciphertext)
    print(len(ciphertext))


if __name__ == '__main__':
    main()
