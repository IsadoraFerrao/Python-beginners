class Pessoa:
    def __init__(self, nome, idade, sexo, id):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.id = id
    def maioridade(self):
        idade = self.idade
        if(idade >= 18):
            return "maioridade"
        else:
            return "menor de idade"

pessoa = Pessoa("Deb", 10, "feminino", 25585)
print(pessoa.nome)
print(pessoa.maioridade())