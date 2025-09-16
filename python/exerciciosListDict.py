alunos = dict()
alunos_ls = list()
try:
  for a in range(0,2):
    alunos['nome']= str(input('Nome: '))
    alunos['idade']= int(input('Idade: '))
    alunos['media']= float(input('Media: '))
    if alunos['media']<5:
      alunos['status'] = 'reprovado'
    else:
      alunos['status'] = 'aprovado'
    alunos_ls.append(alunos.copy())
  for a in alunos_ls:
    for k,v in a.items():
      print(f'{k}: {v}', end='; ')
    print()

except TypeError as e:
     print(e)


