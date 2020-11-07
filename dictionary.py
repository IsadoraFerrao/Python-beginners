funcionario = {'nome': 'Thor', 'idade':35, 'salario':7350.34,
'funcao':['ser lindo']}

funcionario['estavo_civil'] = 'solteiro' #add
del funcionario['idade'] #deletar
print(funcionario.get('salario')) #pegar algo
#print(funcionario)

#para atualizar basta usar atribuicao