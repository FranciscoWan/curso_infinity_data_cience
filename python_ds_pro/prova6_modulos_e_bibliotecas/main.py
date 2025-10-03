# Desenvolva um programa em Python que funcione como um sistema de gerenciamento de uma biblioteca. O programa deverá permitir que os usuários realizem as seguintes operações:

# Funcionalidades:

# Adicionar Livros à Biblioteca:
# O programa deve permitir que o usuário adicione novos livros à biblioteca. Para cada livro, o sistema deve armazenar:
# Título do livro
# Autor do livro
# Número de cópias disponíveis

# Listar Todos os Livros Disponíveis:
# O programa deve exibir uma lista de todos os livros disponíveis na biblioteca, incluindo o título, autor e o número de cópias disponíveis.

# Empréstimo de Livros:
# O programa deve permitir que os usuários façam o empréstimo de um livro, o que reduzirá o número de cópias disponíveis para aquele livro.
# Se não houver cópias disponíveis, o programa deve informar ao usuário que o livro não pode ser emprestado.

# Devolução de Livros:
# O programa deve permitir que os usuários devolvam livros, aumentando o número de cópias disponíveis.

# Verificar Disponibilidade de um Livro:
# O programa deve permitir que o usuário consulte se um livro específico está disponível na biblioteca, verificando o número de cópias.

# Mostrar Livros Emprestados a um Usuário Específico:
# O programa deve permitir que o usuário visualize a lista de todos os livros que ele já pegou emprestado.

lista_de_livros = []
lista_usuarios = []

def adc_livro(nome_livro:str, autor_livro:str, num_copias_disp:int) -> None:
    '''Permite adicionar novos livros a biblioteca. Retorna um dicionário do livro registrado.'''
    novo_livro = {}
    novo_livro["nome"] = nome_livro
    novo_livro["autor"] = autor_livro
    novo_livro["numero_copias"] = num_copias_disp
    lista_de_livros.append(novo_livro)

def listar_livros(lista_de_livros:list) -> None:
    '''Lista todos os livros disponíveis na biblioteca.'''
    print("Livros cadastrados -")
    for livro in lista_de_livros:
        print("-"*40)
        print(f"{livro["nome"]}")
        print(f"{livro["autor"]}")
        print(f"{livro["numero_copias"]}")

def emprestar_livros(nome_livro:str, nome_usuario:str) -> None:
    '''Recebe o nome de um livro e do usuário que irá pegar o livro, verifica a quantia de livros disponíveis para empréstimo. Caso não haja, aparecerá uma mensagem informando não ser possível pegar o livro na tela.'''
    dicionario_usuario = {}
    for livro in lista_de_livros:
        if livro["nome"] == nome_livro:
            if livro["numero_copias"] > 0:
                livro["numero_copias"] -= 1
                dicionario_usuario["nome"] = nome_usuario
                dicionario_usuario["nome_livro"] = nome_livro
                lista_usuarios.append(dicionario_usuario)
                print(f"O livro {livro["nome"]} foi emprestado com sucesso.")
            else:
                print(f"Não é possível pegar este livro emprestado. Existem {livro["numero_copias"]} para emprestar.")

def devolver_livro(nome_livro:str) -> None:
    '''Recebe o nome de um livro e "devolve" o livro para a biblioteca.'''
    cont = 0
    for livro in lista_de_livros:
        if livro["nome"] == nome_livro:
            livro["numero_copias"] += 1
            cont += 1
            print(f"O livro {livro["nome"]} foi devolvido com sucesso.")
    if cont == 0:    
        print(f"Não foi encontrado o livro para ser devolvido. Livro: ")

def verifica_livro_biblioteca(nome_livro:str) -> None:
    '''Verifica a disponibilidade de um livro'''
    for livro in lista_de_livros:
        if livro["nome"] == nome_livro:
            if livro["numero_copias"] == 0:
                print(f"O livro: {livro["nome"]} não possui cópias disponíveis para pegar emprestado.")
                continue
            print(f"O livro: {livro["nome"]}\nCópias disponíveis: {livro["numero_copias"]}")

def visualizar_lista_emprestados(nome_usuario:str) -> None:
    '''Mostra ao usuário todos os livros pego por um usuário específico.'''
    print(f"Livros emprestado por {nome_usuario}:", end=" ")
    for usuario in lista_usuarios:
        if usuario["nome"] == nome_usuario:
            print(f"{usuario["nome_livro"]}")

def menu(opcao:int) -> None:
    '''Menu responsável por chamar as outras funções do programa.'''
    if opcao == 1:
        livro = str(input("Nome do livro: "))
        autor = str(input("Autor: "))
        copias = int(input("Quantidade de cópias: "))
        adc_livro(livro,autor,copias)
    elif opcao == 2:
        listar_livros(lista_de_livros)
    elif opcao == 3:
        nome = str(input("Livro que deseja pegar emprestado: "))
        nome_usuario = str(input("Nome da pessoa que estápegando o livro: "))
        emprestar_livros(nome,nome_usuario)
    elif opcao == 4:
        livro = str(input("Nome do livro para devolver: "))
        devolver_livro(livro)
    elif opcao == 5:
        livro = str(input("Nome do livro para verifica disponibilidade: "))
        verifica_livro_biblioteca(livro)
    elif opcao == 6:
        usuario = str(input("Nome do usuário que deseja verificar histórico: "))
        visualizar_lista_emprestados(usuario)

while True:
    print("### Biblioteca Cultura ###")
    print("Digite a opção desejada")
    print('''1 - Adicionar um novo listro
2 - Listar livros
3 - Emprestar livro
4 - Devoler livro
5 - Verificar disponibilidade do livro
6 - Verificar empréstimos
0 - Encerrar o programa''')
    opcao = int(input("Opção: "))
    print("-"*40)
    if opcao in [1,2,3,4,5,6,0]:
        if opcao == 0:
            print("Programa encerrado.")
            break
        else:
            menu(opcao)
    else:
        print("Digite uma opção válida")