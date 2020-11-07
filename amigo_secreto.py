#Amigo secreto da turma do chaves
import random

nomes = ["Chaves", "Chiquinha", "Kiko", "Professor Girafales", "Seu Madruga", "Inhonho", "Dona Florinda", "Seu Barriga"] 
sorteados = []
ordem = {}
for pessoa in nomes:
    amigo_secreto = random.choice(nomes)
    while((pessoa == amigo_secreto) or (amigo_secreto in sorteados)):
        amigo_secreto = random.choice(nomes)
    sorteados.append(amigo_secreto)
    ordem[pessoa] = amigo_secreto
print(ordem)