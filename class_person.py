class Pessoa:
    def __init__(self, nome, idade, cidade, sexo, id):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.sexo = sexo
        self.id = id
    def maioridade(self):
        idade = self.idade
        if(idade >= 18):
            return "maioridade"
        else:
            return "menor de idade"
    def estado(self, estado):
        return f"A cidade é {self.cidade} e o estado é {estado}"

pessoa = Pessoa("Deb", 10, "Natal","feminino", 25585)
print(pessoa.nome)
print(pessoa.maioridade())

print(pessoa.estado("RN"))