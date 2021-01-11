import binascii
import base64
from heapq import nsmallest
from c3 import *
from c5 import *

def hamming_distance(str1, str2):
    count = 0
    for i,j in zip(str1, str2):
        xor = i ^ j
        while(xor > 0):
            count += xor & 1
            xor >>=1
    return count

if __name__ == '__main__':
    # input1 = b'this is a test'
    # input2 = b'wokka wokka!!!'
    # print(hamming_distance(input1,input2))
    with open('6.txt', 'rb') as f:
        input = f.read()
    decodedinput = base64.b64decode(input)
    #print(decodedinput)
    keysize = range(2,41)
    hamming_list = {}
    for k in keysize:
        block1 = decodedinput[:k]
        block2 = decodedinput[k:2*k]
        #print(block1, block2)
        h = hamming_distance(block1, block2)
        print(h)
        hamming_list[k] = h/k
    #prob_keysize = min(hamming_list, key=hamming_list.get)
    print(hamming_list)
    min3size = nsmallest(3, hamming_list, key=hamming_list.get)
    prob_keysize_list = []
    for val in min3size:
        prob_keysize_list.append(val)
    print(prob_keysize_list)
    for prob_keysize in prob_keysize_list:
        transposed_block = []
        for i in range(prob_keysize):
            transposed_block.append(decodedinput[i::prob_keysize])
        #print(transposed_block)
        crack = ''
        for block in transposed_block:
            #print(block)
            s, k = break1bytexor(block)
            crack += k
        #print(crack)
        final_output = repeatingkeyxor(decodedinput, bytes(crack,'ascii'))
        #print(binascii.hexlify(final_output))

