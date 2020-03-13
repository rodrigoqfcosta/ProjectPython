'''
Faça um programa que leia o aquivo Alice's Adventures in Wonderland.txt
e conte o número de ocorrencias de cada palavra no texto
'''

import string
arq = open("C:/Users/rodri/OneDrive/Área de Trabalho/Alice's Adventures in Wonderland.txt")
texto = arq.read()
texto = texto.replace('\n', '').lower()
for c in texto:
    if c in string.punctuation:
        texto = texto.replace(c, ' ')
arq.close()

dic = dict()
texto = texto.split()
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1

for k, v in dic.items():
    print(f"A palavra {k}, apareceu {v} vezes.")
