import random


def mono(key, plaintext, prob):
    """
    This function is used to encrypt the plaintext by using the value key
    :param key: A dictionary representing the key
    :param plaintext: A string representing the plaintext
    :param prob: A number between 0 and 1 representing the probability of inserting a random character into the cipher
    :return: A string representing the ciphertext
    """
    cipher = ''
    message_pointer = 0

    while message_pointer < len(plaintext):
        coin_value = random.random()
        if coin_value >= prob:  # In this case, it should encrypt the corresponding character
            c = key[plaintext[message_pointer]]
            cipher += c
            message_pointer += 1
        else:
            r = random.choice(list(key.values()))
            cipher += r

    return cipher
