"""
Você recebe os preços atuais das ações em forma de dicionário onde o código identificador do mercado é uma chave e o valor é o preço da ação. 
Você tem que descobrir quais ações custam mais e retornar o código identificador de mercado (símbolo de ação) como uma string.
"""

def best_stock(data):
    maior_valor = max(data, key=data.get) #pegando a chave do maior valor
    return maior_valor

if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }) == 'ATX', "First"
    assert best_stock({
        'CAC': 91.1,
        'ATX': 1.01,
        'TASI': 120.9
    }) == 'TASI', "Second"
    print('Terminou')