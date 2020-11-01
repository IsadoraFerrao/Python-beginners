# Programa para calcular se um numero e par ou impar

numero = 0

while(numero != -1):
    print("Informe um número OU digite -1 para sair")
    numero = int(input())

    resto = numero%2
    if(resto == 0):
        print(f"\nO número {numero} é par :)")
    elif (numero == -1):
        print("Bye bye")
        exit()
    else:
        print(f"\nO número {numero} ímpar :)")


