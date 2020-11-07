def media_geral(nota_1, nota_2, nota_3):
    media_geral = ((float(nota_1) + float(nota_2)+ float(nota_3))/3)
    print(f"Você ficou com média geral de {round(media_geral,2)}")
    if(media_geral >= 7.0):
        print("Portanto, você foi aprovado")
    else:
        print("Portanto, você foi reprovado")

print(f"Qual nota você tirou no 1° trimestre?")
nota_1 = input()

print(f"Qual nota você tirou no 2° trimestre?")
nota_2 = input()

print(f"Qual nota você tirou no 3° trimestre?")
nota_3 = input()

media_geral(nota_1, nota_2, nota_3)


