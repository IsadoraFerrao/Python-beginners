letras = ["R", "B", "R", "R","B","G","G","B","G","R"] 

lista_ordenada = []
#lista_str = ' - '.join(letras)

R = letras.count("R")
G = letras.count("G")
B = letras.count("B")

for R in range(R):     # por índice
    lista_ordenada.append("R")
for B in range(B):
    lista_ordenada.append("B")
for G in range(G):
    lista_ordenada.append("G")     

print(lista_ordenada)
print(' - '.join(lista_ordenada))
#lista_A_str = ' -- '.join(lista_A))

