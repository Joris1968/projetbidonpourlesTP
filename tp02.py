#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import * 

liste = []


def genere_liste_alea(liste):
	for i in range(20):
		x = randint(1,50)
		liste.append(x)



def fusion(T1,T2) :
	if T1==[] :
		return T2
	if T2==[] :
		return T1
	if T1[0] < T2[0] :
		return [T1[0]]+fusion(T1[1 :],T2)
	else :
		return [T2[0]]+fusion(T1,T2[1 :])		

		


def tri_fusion(T):
	if len(T) <= 1 : 
		return T
	T1=[T[x] for x in range(len(T)//2)]    # tri par comprehension
	T2=[T[x] for x in range(len(T)//2,len(T))]
	return fusion(tri_fusion(T1),tri_fusion(T2))		


genere_liste_alea(liste)
print(liste)
# print(int(3))	
liste2 = tri_fusion(liste) 
print('toto')
print(liste2)


