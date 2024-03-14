import random


def generate_key(key_space):
    """
    This function is used for mono-alphabetic substitution cipher.
    :param key_space: This function will use this key space to generate the key. It is represented by a list.
    :return: A dictionary represented key, showing the map relation between characters.
    """
    key = {}
    s = set()
    for c in key_space:
        s.add(c)

    for i in range(len(key_space)):
        picked_character = random.choice(tuple(s))
        key[key_space[i]] = picked_character
        s.remove(picked_character)

    return key


if __name__ == '__main__':
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', ' ']
    key = generate_key(l)
    print(key)