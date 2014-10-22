from math import e


def e_with_precision(n):
    return '%.*f' % (n, e)
if __name__ == '__main__':
    while True:
        precision = int(raw_input('Number of decimal places: '))
        print(e_with_precision(precision))
