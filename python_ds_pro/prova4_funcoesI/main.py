# Desenvolva um programa em Python que funcione como uma calculadora simples, permitindo ao usuário realizar as seguintes operações matemáticas:

# Soma
# Subtração
# Multiplicação
# Divisão
# Sair do programa
# Requisitos:
# O programa deve exibir um menu de opções, permitindo ao usuário escolher qual operação ele deseja realizar (soma, subtração, multiplicação, divisão ou sair).
# Para cada operação escolhida, o programa deve solicitar ao usuário dois números e exibir o resultado da operação entre eles.
# As operações matemáticas (soma, subtração, multiplicação e divisão) devem ser implementadas em funções separadas. Cada função deve receber dois argumentos (números) e retornar o resultado da operação.
# O programa deve funcionar indefinidamente, permitindo ao usuário realizar quantas operações quiser, até que ele escolha a opção de sair.
# Caso o usuário selecione a divisão, o programa deve garantir que a divisão por zero seja evitada, exibindo uma mensagem de erro apropriada e solicitando novos valores.
# Use condicionais e laços de repetição para controlar o fluxo do programa e garantir que ele continue até o usuário escolher a opção de sair.

def soma(num1:int, num2:int) -> int:
    '''Função de soma:
    Recebe dois números inteiros e retorna a soma deles
    num1 + num2'''
    return num1+num2

def sub(num1:int, num2:int) -> int:
    '''Função de subtração:
    Recebe dois números inteiros e retorna a subtração deles
    num1 - num2'''
    return num1-num2

def div(num1:int, num2:int) -> int:
    '''Função de divisão:
    Recebe dois números inteiros e retorna a divisão deles
    num1 / num2'''
    try:
        num1/num2
    except ZeroDivisionError:
        print("O divisão não pode ser realizada por ZERO")
        return None

    return num1/num2

def mult(num1:int, num2:int) -> int:
    '''Função de multiplicação:
    Recebe dois números inteiros e retorna a multiplicação deles
    num1 * num2'''
    return num1 * num2

def menu(operador_aritimetico:str, numero1:int, numero2:int) -> None:
    '''Função responsável por chamar as funções matemáticas
    return = None'''

    if operador_aritimetico == "+":
        print(f"O resultado é: {soma(numero1,numero2)}")
    elif operador_aritimetico == "-":
        print(f"O resultado é: {sub(numero1,numero2)}")
    elif operador_aritimetico == "*":
        print(f"O resultado é: {mult(numero1,numero2)}")
    elif operador_aritimetico == "/":
        print(f"O resultado é: {div(numero1,numero2)}")


print("### Calculadora ###")
while True:
    opc = str(input("Digite um opção:\nSim - realiza operação matemática\nNão - encerrar calculadora\nOpção: "))
    print("-"*40)
    if opc.lower().strip() in ["não", "nao", "n"]:
        print("Calculadora encerrada")
        break
    elif opc.lower().strip() in ["sim", "s"]:
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))
        print("Digite a operação matemática que deseja fazer\n+, -, *, /")
        operacao = str(input("Opção: "))
        menu(operador_aritimetico=operacao,numero1=num1,numero2=num2)
        print("-"*40)
    else:
        print("Digite uma opção válida.")