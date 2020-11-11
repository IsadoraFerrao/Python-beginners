"""
Você recebe duas strings e precisa encontrar um índice da segunda ocorrência da segunda string na primeira.
Vamos examinar o primeiro exemplo em que você precisa encontrar a segunda ocorrência de "s" em uma palavra "sims". 
É fácil encontrar sua primeira ocorrência com um índice de função ou encontrar que indicará 
que "s" é o primeiro símbolo em uma palavra "sims" e, portanto, o índice da primeira ocorrência é 0. 
Mas temos que encontrar o segundo " s "que é o quarto consecutivo e isso significa que o índice da 
segunda ocorrência (e a resposta a uma pergunta) é 3.
"""

def second_index(text: str, symbol: str) -> [int, None]:
    i = -1
    simbolos = []
    for letra in text:
        i = i+1
        if(letra == symbol):
            simbolos.append(letra)
        if(len(simbolos) == 2):
            return i
        else:
            continue


# Não escreva nada abaixo dessa linha
if __name__ == '__main__':
    print('Example:')
    print(second_index("find the river", "e"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('Terminou')
