print("Olá, qual o seu nome?")
nome = input()
print(f"Olá {nome}, em qual ano você nasceu?")
ano = input()

print(f"Em qual mês você nasceu?")
mes = input()

mes_atual = 10

idade = 2020 - int(ano)

if(int(mes) > mes_atual):
    print(f"{nome}, você tem {idade-1} anos")
else:
    print(f"Você tem {idade} anos")
