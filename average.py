print("Qual o seu nome?")
nome = input()
print(f"Prazer {nome}, qual ano você está na escola?")
ano = input()

print(f"Qual nota você tirou no 1° trimestre?")
nota_1 = input()

print(f"Qual nota você tirou no 2° trimestre?")
nota_2 = input()

print(f"Qual nota você tirou no 3° trimestre?")
nota_3 = input()

media_geral = ((float(nota_1) + float(nota_2)+ float(nota_3))/3)
print(f"Caro {nome}, durante o seu {ano} ano você ficou com a média geral de {media_geral}")
if(media_geral >= 7.0):
    print("Portanto, você foi aprovado")
else:
    print("Você foi reprovado")
