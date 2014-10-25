from operator import xor


def readfile(filename = None):
    if filename is not  None:
        with open(filename) as f:
            content = [text.split(",") for text in f.readlines()]
            return content
        return False

def decode(lists = None,dekey = (ord('s'),ord('b'),ord('w'))):
    if lists is not None:
        res = list()
        for i in range(len(lists)):
            if i%3 == 0:
                res.append(xor(int(lists[i]), dekey[0]))
            elif i%3 == 1:
                res.append(xor(int(lists[i]), dekey[1]))
            elif i%3 == 2:
                res.append(xor(int(lists[i]), dekey[2]))
            else:
                return False
        content = [chr(int(res[i])) for i in range(len(res))]
        return content
    return False


if __name__ == "__main__":
    content = readfile('./decodetext')
    res = decode(content[0])
    s = str()
    for i in range(len(res)):
        s += res[i]
    print s

            
        
