class Funcionario:
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

func_1 = Funcionario("Thor", "Odisons", 10000)

print(func_1.nome_completo())

