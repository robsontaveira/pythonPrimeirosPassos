#Calculadora simples

#---Funções para as operações da calculadora---
def soma(x,y):
    return x + y

def subtra():
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    subtracao = num1 - num2
    print(subtracao)

def mult():
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    multipicacao = num1 * num2
    print(multipicacao)

def div():
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    divisao = num1 / num2
    print(divisao)

#---Menu da calculadora---

print('**********Calculadora simples em Python**********\n')
print('Selecione a operação desejada:\n')
print('1 - Soma\n2 - Subtração\n3 - Muliplicação\n4 - Divisão\n')
opcao = int(input('Digite sua opção (1/2/3/4):'))

#---Bloco de condicionais---

if opcao == 1:
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    print(soma(num1,num2))
elif opcao == 2:
    subtra()
elif opcao == 3:
    mult()
elif opcao == 4:
    div()
else:
    print('Opção invalida')



