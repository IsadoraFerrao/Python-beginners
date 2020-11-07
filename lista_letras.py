import random
letras = ["R", "G", "B"]
lista_nova = (' '.join(random.choice(letras) for letra in range(15)))
print(lista_nova.split(" ")) #split pra quebrar a lista única em posicoes



