def read_plaintext(filename):
    with open(filename, 'r') as file:
        content = file.read()
        l = content.split('\n')
        res = []
        for pt in l:
            if len(pt) == 600:
                res.append(pt)

        return res


if __name__ == '__main__':
    read_plaintext('./s24_dictionary1.txt')
