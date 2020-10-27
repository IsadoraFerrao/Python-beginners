print("Qual número você gostaria de saber a tabuada?")
numero = int(input())
print(f"Tabuada {numero}:")
for mult in range(0,11):
    result = numero*mult
    print(f"{numero}x{mult} = {result}")