import binascii
import base64

def hex2b64(input):
    bytestring = binascii.unhexlify(input)
    return base64.b64encode(bytestring)

if __name__ == '__main__':
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(input)
    # Expected output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
    print(hex2b64(input))
