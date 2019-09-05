# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:36:00 2019

@author: PRIYANK DHRUV
"""

def getNumericKey(Plaintxt, key): 
	key = list(key) 
	if len(Plaintxt) == len(key): 
		return(key) 
	else: 
		for i in range(len(Plaintxt) - len(key)): 
			key.append(key[i % len(key)]) 
	return("".join(key)) 
	
 
def cipherText(Plaintxt, NumKey): 
	ciphertext = [] 
	for i in range(len(Plaintxt)): 
		x = (ord(Plaintxt[i]) + ord(NumKey[i])) % 26
		x += ord('A') 
		ciphertext.append(chr(x)) 
	return("".join(ciphertext)) 
	

def plainText(Ciphertxt, NumKey): 
	plaintext = [] 
	for i in range(len(Ciphertxt)): 
		x = (ord(Ciphertxt[i]) - ord(NumKey[i]) + 26) % 26
		x += ord('A') 
		plaintext.append(chr(x)) 
	return("".join(plaintext)) 

Plaintxt = input("\nEnter any Random String : ")
key = input("Enter any Random Keyword : ")
NumKey = getNumericKey(Plaintxt, key)     

x = 1

while(x):
    print("\n***** Vigenere Cipher *****")
    print("\n1.Generate Ciphertext \n2.Generate Plaintext \n3.Exit\n")    
    choice = int(input("Choose any one task : "))

    if choice == 1:	       
        Ciphertxt = cipherText(Plaintxt, NumKey) 
        print("\nCiphertext :", Ciphertxt)

    if choice == 2:
        Ciphertxt = input("\nEnter previous Ciphertext : ")     
        Plaintxt = plainText(Ciphertxt, NumKey) 
        print("\nReturned Plaintext :", Plaintxt)
    
    if choice == 3:
        x = 0
        