"""
Your mission here is to create a function that gets a tuple and returns a tuple with 3 elements - 
the first, third and second element from the last for the given array.
"""

def easy_unpack(elements: tuple) -> tuple:
    numeros = []
    for numero in elements:
        numeros.append(numero)
    return (numeros[0], numeros[2], numeros[-2])


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Terminou')