# Programa para o usuário adivinhar um número de 0 a 10
# Isadora G. Ferrão
# Univerisdade de São Paulo - Luiza <Code> 2020
import random

print("Olá, qual o seu nome?")
nome = input()
print(f"\nOlá {nome}, estou pensando em um número de 0 a 80.")
print("Você consegue adivinhar?")
print("(1) Sim (2) Não")
entrada = int(input())

num_sorteado = random.randint(1, 81)
cont = 0
resposta= "JOGAR"

if(entrada == 1):
    while(resposta== "JOGAR"):
        print("Qual número estou pensando?")
        numero = int(input())
        
        if(numero > num_sorteado):
            if((num_sorteado - numero) <= 10 ):
                print("O número é menor, tente novamente! Você está quase lá")
                cont = cont+1
            else:
                print("Você ainda está longe, se esforce mais")
                cont=cont+1
        elif(numero < num_sorteado):
            if((num_sorteado - numero) <= 10):
                print("O número é maior, tente novamente! Você está quase lá")
                cont=cont+1
            else:
                print("Você ainda está longe, se esforce mais")
                cont=cont+1
        elif(numero == num_sorteado):
            if(cont <= 5):
                print(f"Parabéns {nome}, você acertou o número na {cont+1}° tentativa")
                cont = 0
                print("Quer tentar novamente?")
                print("(1) Sim (2) Não")
                entrada = int(input()) 
                if(entrada == 1):
                    resposta == "JOGAR"
                else:
                    exit()
            else:
                print(f"Aleluia! Você acertou na {cont+1}")
                cont = 0
                print("Quer tentar novamente?")
                print("(1) Sim (2) Não")
                entrada = int(input()) 
                if(entrada == 1):
                    resposta == "JOGAR"
                else:
                    exit()
        else:
            print("Na próxima quem sabe, bye bye")
            exit()
