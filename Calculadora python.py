'''Programa simulando uma calculadora em python. 26/06/2026'''

num1 = int(input('Digite o primeiro dígito da operação: '))
sinal = input('["+", "-", "*" , "/"]: ').strip()
num2 = int(input('Digite o segundo dígito da operação: '))


if sinal == "+":
    resultado = num1 + num2
elif sinal == "-":
    resultado = num1 - num2
elif sinal == "*":
    resultado = num1 * num2
elif sinal =="/":
    resultado = num1 / num2
else:
    raise ValueError('Operação inválida. Use apenas: + - * /')


print(f'O resultado entre os dois dígitos é igual a: {resultado}')


'''O comando .strip faz com que o usuário do código ao utilizar espaços em branco ou caractéres indesejaveis não
quebre ao aplicar os sinais'''
'''Raise ValueError força a parada do programa'''