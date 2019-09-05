def encryption(text, key):
    ciphertext = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            ciphertext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(char) + key - 97) % 26 + 97)
    return ciphertext
    
def decryption(cipher, key):
    tmp = []
    plaintext = ""
    for char in cipher:
        if(char.isupper()):
            tmp.append(chr((ord(char) - key - 65) % 26 + 65))
            
        else:    
            tmp.append(chr((ord(char) - key - 97) % 26 + 97))
    return plaintext.join(tmp)

plaintext = input("Plaintext : ")
key = int(input("Key : "))

ciphertext = encryption(plaintext, key)
cipher_list = list(ciphertext)
Rtn_plaintext = decryption(cipher_list, key)

print("\nCipherText : " + ciphertext)
print("Returned PlainText : " + Rtn_plaintext)