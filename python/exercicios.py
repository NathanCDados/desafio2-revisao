#import math
#
## 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#base=int(input('Digite o valor da base: '))
#expoente=int(input('Digite o valor do expoente: '))
#resultado = base ** expoente
#print(f'A potencia da base {base} e o expoente {expoente} é {resultado}')
#
## 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#raio_circ=float(input('Digite o raio: '))
#area_circ= math.pi * raio_circ ** 2
#print(f'O valor da area do circulo é {area_circ:.2f}') #o :.2f limita o resutlado a duas casas decimais
#
## 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#nome=input('Digite seu nome: ')
#print(nome.upper())
#
## 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#nome=input('Digite seu nome completo: ')
#print(nome.lower())
#
## 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data= input('Digite a data: ')
#dataform=data.split('/')
#dia = dataform[0]
#mes = dataform[1]
#ano = dataform[2]
#print(f'o dia é {dia}, o mes é {mes} e o ano é {ano}')
## 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#nome=input('nome: ')
#sobrenome=input('sobrenome: ')
#print(nome + ' '+ sobrenome)
#
## #### try-except e if
#
## 21: Conversor de Temperaturas
#print('Convertendo de Celcius para Fahrenheit')
try:
    tempCelc = float(input('Digite a temperatura: '))
    if tempCelc == 0:
        print('A temperatura é 32 Fahrenheit')
    else:
        tempFahr = (tempCelc * 1.8) + 32   
        print(f'A temperatura em fahrenheit é: {tempFahr:.2f} graus ')
except ValueError:
   print('entrada invalida')


# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
