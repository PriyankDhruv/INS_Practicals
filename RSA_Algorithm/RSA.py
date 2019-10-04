# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:53:09 2019

@author: PRIYANK DHRUV
"""

from decimal import Decimal 

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b, a%b) 

print('\n')    
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter any random value = ')) 
n = p*q 
t = (p-1)*(q-1) 

for e in range(2, t): 
	if gcd(e,t)== 1: 
		break

for i in range(1,10): 
	x = 1 + i*t 
	if x % e == 0: 
		d = int(x/e) 
		break

ctt = Decimal(0) 
ctt = pow(no, e) 
ct = ctt % n 

dtt = Decimal(0) 
dtt = pow(ct, d) 
dt = dtt % n 

print('\n')
print('n = ' + str(n))
print('e = ' + str(e))
print('t = ' + str(t)) 
print('d = ' + str(d)) 
print('Cipher-text = '+ str(ct))
print('Decrypted-text = '+ str(dt)) 
