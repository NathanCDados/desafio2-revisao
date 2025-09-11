import re #utilizando regex
nomeUsuario = input('digite o nome: ')

if re.search(r'\d',nomeUsuario):#chamamos a funçao re.search para procurar na variavel numeros de 0 -9 com (\d). 
    # O r antes da string '\d' é chamado de string bruta, importante quando se trabalha com expressoes regulares
    print('Digite apenas letras')
    exit()

elif len(nomeUsuario) == 0 or nomeUsuario.isspace(): # atribuindo duas condiçoes para tratar erros
    print('Campo em branco, por favor digite o nome') 

else:
    salario=float(input(f'Ola {nomeUsuario}, digite seu salario: '))
    if isinstance(salario,float):
        bonus = float(input('Digite o valor do bonus recebido em porcentagem: '))
        if bonus >100:
            print('o bonus pode ser de no maximo 100%')
        elif isinstance(bonus,float):
            valorBonus = (bonus/100) * salario + salario
            print(f'o valor do salario mais o bonus de {bonus}% sera: {valorBonus}')   

        else: 
            exit()
    else:
        exit()
  

