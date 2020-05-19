import binascii
from c3 import *

if __name__ == '__main__':
    with open('4.txt','r') as f:
        lines = f.readlines()

    output = []
    for l in lines:
        decodedinput = binascii.unhexlify(l.strip())
        output.append(break1bytexor(decodedinput))
    finalscores = {}
    for i in output:
        finalscores[i[0]] = score(i[0])
    print(max(finalscores, key=finalscores.get))
