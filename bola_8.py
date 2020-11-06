import random 
print("Qual o seu nome?")
nome = input()

print(f"\n\nOlá {nome}, bem vindo a Bola 8 Mágica")
print("A Bola 8 irá te ajudar a tomar a decisão certa!")

dinheiro = ["Cuidado com o gasto extremo em 'brusinhas', em breve você verá o reflexo disso tudo","Se o dinheiro for a sua esperança de independência, você jamais a terá. A única segurança verdadeira consiste numa reserva de sabedoria, de experiência e de competência.", "O cofre do banco contém apenas dinheiro; frusta-se quem pensar que lá encontrará riqueza.", "Economize, em breve você passará por problemas familiares e precisará de uma renda extra"]
amor = ["Eu vejo um grande amor no seu futuro, ele está mais próximo do que você imagina", "Cuidado com quem diz que te ama e fala mal de você pelas costas", "Um novo amor está próximo, mas cuidado, ele pode ser devastador em sua vida"]
futuro = ["Confie no seu potencial, você está no caminho certo","Vejo uma criança sorridente chegando em sua vida, parabéns!", "Vejo em breve mudança de carreiras para você, siga com cautela nesta transição","Você tem a sensação de que está prestes a cometer um erro e não sabe o que decidir. Acredite: neste caso, será melhor ouvir sua intuição e seu coração", "Há um inimigo escondido entre seus entes queridos. Talvez você nem perceba, mas há uma grande influência negativa em sua vida", ""]
decisao = "SIM"

while(decisao == "SIM"):
    print("\nDigite SIM para fazer uma pergunta")
    print("Digite NAO para sair")
    decisao = input()
    decisao = decisao.upper() #garantia de execução caso o usuário digite minusculo

    if(decisao == "SIM"):
        print("Você quer saber sobre:")
        print("(1) Amor")
        print("(2) Dinheiro")
        print("(3) Futuro")

        tema_pergunta = int(input())
        if(tema_pergunta == 1):
            print("Digite sua pergunta: ")
            pergunta = input()
            resposta = random.sample(amor, 1)
            print(' - '.join(resposta))

        if(tema_pergunta == 2):
            print("Digite sua pergunta: ")
            pergunta = input()
            resposta = random.sample(dinheiro, 1)
            print(' - '.join(resposta))

        if(tema_pergunta == 3):
            print("Digite sua pergunta: ")
            pergunta = input() 
            resposta = random.sample(futuro, 1)
            print(' - '.join(resposta))   
    else:
        print("\nAté a próxima")
        exit()