class Atores:
    def __init__(self, nome, idade, sexo, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.nacionalidade = nacionalidade

    def get_origin(self):
        origens = {'american': 'from the U.S', 'brazilian': 'from Brazil', 'mexican':'from Maxico'}
        if self.nacionalidade.lower() in origens.keys():
            origin = origins[self.nacionalidade.lower()]
            return origin
        else:
            return f"I'm {self.nacionalidade}"

    def actor_intro(self):
        return f"Hi, my name is {self.name} and I'm a {self.sexo}"

class Big_Bang(Atores): #herdando os valores de atores
    pass
 
act1 = Big_Bang("Rodrigo", 45, "masculino", "Brasileiro")
act2 = Atores("Rodrigo Santoro", 45, "masculino", "Brasileiro")

print(act1.nome)
#print(act1.get_origin())
#print(act1.nacionalidade)