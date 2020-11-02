cursos = ['ingles', 'port', 'hist', 'python', 'alemao']
notas = [7.5, 4, 8, 2, 10]

cursos_e_notas = cursos+notas #unindo duas listas
#print(cursos[0:3]) #3 primeiros valores
#print(cursos_e_notas)
#print(cursos[1:-2])
#cursos.append('karate') #add elemento 
cursos.extend(notas) #unindo listas
#.insert(0, 'karate') #add elemento num lugar específico da lista
print(cursos)
if('port' in cursos):
    cursos.remove('port') #remover um elemento da lista
    print(cursos)