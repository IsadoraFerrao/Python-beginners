# Programa para o usuário adivinhar um número de 0 a 10
# Isadora G. Ferrão
# Univerisdade de São Paulo - Luiza <Code> 2020
import random

print("Olá, qual o seu nome?")
nome = input()
print(f"\nOlá {nome}, estou pensando em um número de 0 a 20.")
print("Você consegue adivinhar?")
print("(1) Sim (2) Não")
entrada = int(input())

num_sorteado = random.randint(1, 20)

if(entrada == 1):
    for cont in range(0,6):
        print("Qual número estou pensando?")
        numero = int(input())
        if(numero > num_sorteado):
            print("O número é menor, tente novamente")
            cont = cont+1
        elif(numero < num_sorteado):
            print("O número é maior, tente novamente")
            cont=cont+1
        else:
            print(f"Parabéns {nome}, você acertou o número na {cont+1}° tentativa")
            exit()
    print("Suas chances terminaram")
    print(f"O número correto seria {num_sorteado}")
    exit()
else:
    print("Na próxima quem sabe, bye bye")
    exit()