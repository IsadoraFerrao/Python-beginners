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

class Empresa(Pessoa): #herança 
    def __init__(self, nome, idade, cidade, sexo, id, nome_empresa):
        super().__init__(nome, idade, cidade, sexo, id)
        self.nome_empresa = nome_empresa

pessoa = Pessoa("Deb", 10, "Natal","feminino", 25585)
#print(pessoa.nome)
#print(pessoa.maioridade())
#print(pessoa.estado("RN"))

empresa = Empresa("Deb", 32, "Natal", "Feminino", 3434, "Google")
print(empresa.nome)