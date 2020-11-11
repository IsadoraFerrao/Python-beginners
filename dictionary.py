funcionario = {'nome': 'Thor', 'idade':35, 'salario':7350.34,
'funcao':['ser lindo']}

funcionario['estavo_civil'] = 'solteiro' #add
#del funcionario['idade'] #deletar
#print(funcionario.get('salario')) #pegar algo
#print(funcionario)
#pop deletar o último item da lista
#para atualizar basta usar atribuicao

for coisa in funcionario.items(): #mostra a lista
    print(f"{coisa} oi")
    #print(coisa)