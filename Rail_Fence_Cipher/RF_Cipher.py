# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:18:58 2019

@author: PRIYANK DHRUV
"""
 
def encryptRailFence(text, nor): 
	rail = [['\n' for i in range(len(text))] for j in range(nor)] 
	
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)): 
		if (row == 0) or (row == nor - 1): 
			dir_down = not dir_down 
		
		rail[row][col] = text[i] 
		col += 1
		
		if dir_down: 
			row += 1
		else: 
			row -= 1
	
	result = [] 
	for i in range(nor): 
		for j in range(len(text)): 
			if rail[i][j] != '\n': 
				result.append(rail[i][j]) 
	return("".join(result)) 
	
    
def decryptRailFence(cipher, nor): 
	rail = [['\n' for i in range(len(cipher))] for j in range(nor)] 
	
	dir_down = None
	row, col = 0, 0
	
	for i in range(len(cipher)): 
		if row == 0: 
			dir_down = True
		if row == nor - 1: 
			dir_down = False
		
		rail[row][col] = '*'
		col += 1
		
		if dir_down: 
			row += 1
		else: 
			row -= 1
			
	index = 0
	for i in range(nor): 
		for j in range(len(cipher)): 
			if ((rail[i][j] == '*') and (index < len(cipher))): 
				rail[i][j] = cipher[index] 
				index += 1
		 
	result = [] 
	row, col = 0, 0
	for i in range(len(cipher)): 
		if row == 0: 
			dir_down = True
		if row == nor-1: 
			dir_down = False
			
		if (rail[row][col] != '*'): 
			result.append(rail[row][col]) 
			col += 1
			 
		if dir_down: 
			row += 1
		else: 
			row -= 1
	return("".join(result)) 


Plaintxt = input("Enter any Random text : \n")
N_Rows = input("\nEnter No. of Rows : \n")

Ciphertxt = encryptRailFence(Plaintxt, 2)
print("\nCiphertext : ", Ciphertxt) 	

Rtnd_Plaintxt = decryptRailFence(Ciphertxt, 2)
print("\nReturned Plaintext : ", Rtnd_Plaintxt) 