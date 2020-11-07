import random

letras = ["R", "G", "B"] 
lista_nova = ' '.join(random.choice(letras) for letra in range(16))
print(lista_nova)


#lista_ordenada = []
#lista_str = ' - '.join(letras)

#R = letras.count("R")
#G = letras.count("G")
#B = letras.count("B")

#for R in range(R):     # por índice
#    lista_ordenada.append("R")
#for B in range(B):
#    lista_ordenada.append("B")
#for G in range(G):
#    lista_ordenada.append("G")     

#print(lista_ordenada)
#print(' - '.join(lista_ordenada))
#lista_A_str = ' -- '.join(lista_A))

#usar o random pra criar as linhas