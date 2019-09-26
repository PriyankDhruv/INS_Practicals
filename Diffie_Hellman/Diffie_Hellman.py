# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:26:28 2019

@author: PRIYANK DHRUV
"""

def Public_Key_Alice(PrimeNo, Pt_root, PR_Key):
    A = pow(Pt_root, PR_Key, PrimeNo)
    return A
    
def Public_Key_Bob(PrimeNo, Pt_root, PR_Key):    
    B = pow(Pt_root, PR_Key, PrimeNo)
    return B

def SSK_AB(PrimeNo, PR_Key, PU_Key):
    Kab = pow(PU_Key, PR_Key, PrimeNo)
    return Kab

def SSK_BA(PrimeNo, PR_Key, PU_Key):    
    Kba = pow(PU_Key, PR_Key, PrimeNo)
    return Kba

q = int(input("Enter any Prime Number : \n"))
alpha = int(input("Enter any Primitive Root : \n"))

PR_a = int(input("Enter Private Key of Alice : \n"))
PR_b = int(input("Enter Private Key of Bob : \n"))

PU_a = Public_Key_Alice(q, alpha, PR_a)
print("\nPublic Key of Alice : " + str(PU_a))

PU_b = Public_Key_Bob(q, alpha, PR_b)
print("\nPublic Key of Bob15 : " + str(PU_b))

Kab = SSK_AB(q, PR_a, PU_b)
print("\nShared Secret Key of Alice : " + str(Kab))

Kba = SSK_BA(q, PR_b, PU_a)
print("\nShared Secret Key of Bob : " + str(Kba))

if Kab == Kba:
    print("\nKey Exchange is Performed Successfully")
else:
    print("\nError in Performing Key Exchange..!!")    