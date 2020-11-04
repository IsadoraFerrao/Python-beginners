import random 
numero = random.randint(1,100)

if(numero%3 == 0 and numero%5 == 0):
    print("Dedezinha Querida")
elif(numero%3 == 0):
    print("Dedezinha")
elif(numero%5 == 0):
    print("Querida")
else:
    print(f"Numero = {numero}")
