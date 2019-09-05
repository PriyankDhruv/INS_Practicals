from string import printable
import random

def encode(plaintext, key):
    return ''.join(key[printable.index(char)] for char in plaintext)
 
def decode(ciphertext, key):
    return ''.join(printable[key.index(char)] for char in ciphertext)
 
plaintext = input("Plaintext : ")
key = ''.join(sorted(printable, key = lambda _:random.random()))

ciphertext = encode(plaintext, key)
Rtn_plaintext = decode(ciphertext, key)

print("Substitution Cipher : " + ciphertext)
print("Returned Plaintext : " + Rtn_plaintext)
