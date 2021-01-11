import binascii

def repeatingkeyxor(input, key):
    '''XOR key over input byte-by-byte\n
    input, key - bytes
    '''
    output = b""
    for i in range(0,len(input)):
        output += bytes([input[i] ^ key[i%len(key)]])
    return output


if __name__ == '__main__':
    i = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    k = b'ICE'
    ''' Expected Output
    0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
    a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
    '''
    output = repeatingkeyxor(i,k)
    print(binascii.hexlify(output))