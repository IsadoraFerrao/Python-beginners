""" 
Você recebe um integer positivo. Sua função deve calcular o produto dos digitos excluindo qualquer Zeros.
Por exemplo: O numero dado é 123405. O resultado será 1*2*3*4*5=120 (Não esquece de excluir os Zeros).
"""

def checkio(number: int ) -> int:
    mult = 1 #comeca em 1 pq todo mundo mult por 1 é ele mesmo
    for numeros in str(number):
        if(numeros != "0"): 
            mult = mult*int(numeros) #mult é igual o valor da mult (atual com base na anterior) multiplicado pelos numeros
        else:
            continue
    return mult

if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
        
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print('Terminou')