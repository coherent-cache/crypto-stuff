import binascii
from Crypto.Util.strxor import strxor

def xor(input1, input2):
    decodedstring1 = binascii.unhexlify(input1)
    decodedstring2 = binascii.unhexlify(input2)
    output = strxor(decodedstring1, decodedstring2)
    return output

if __name__ == '__main__':
    input1 = '1c0111001f010100061a024b53535009181c'
    input2 = '686974207468652062756c6c277320657965'

    output = xor(input1, input2)
    print(binascii.hexlify(output))