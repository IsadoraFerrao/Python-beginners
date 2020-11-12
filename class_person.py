class Pessoa:
    def __init__(self, nome, sexo, id):
        self.nome = nome
        self.sexo = sexo
        self.id = id

pessoa = Pessoa("Deb", "feminino", 25585)
print(pessoa.nome)