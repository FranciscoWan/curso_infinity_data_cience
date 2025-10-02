# Você deve desenvolver um programa em Python para gerenciar o cadastro de alunos. O programa deve ter as seguintes funcionalidades:

# Cadastro de Alunos:
# O programa deve permitir ao usuário cadastrar vários alunos.
# Para cada aluno, as seguintes informações devem ser coletadas:
# Nome: O nome do aluno.
# Idade: A idade do aluno.
# Notas: As notas em três disciplinas: Matemática, Ciências e História.

# Essas informações devem ser armazenadas em um dicionário, com as seguintes chaves:
# 'nome': O nome do aluno.
# 'idade': A idade do aluno.
# 'notas': As notas em uma tupla com três valores, representando as disciplinas mencionadas.

# Visualização de Alunos:
# O programa deve permitir que o usuário visualize a lista de todos os alunos cadastrados.
# Para cada aluno, o programa deve exibir:
# O nome
# A idade
# As notas em cada disciplina

# Cálculo da Média de Notas:
# O programa deve calcular a média das notas para cada aluno.
# A média deve ser exibida junto com as informações de cada aluno.

# Aluno com a Melhor Média:
# O programa deve identificar e exibir o aluno que tem a melhor média de notas entre todos os alunos cadastrados.

lista_alunos = []

qtd_alunos = int(input("Digite o número de alunos que deseja cadastrar: "))
print("-"*40)
for i in range(1, qtd_alunos+1):
    dicionario_alunos = {}
    dicionario_alunos["nome"] = str(input("Digite o nome do aluno: "))
    dicionario_alunos["idade"] = int(input("Digite a idade do aluno: "))
    for j in range(3):
        if j == 0:
            materia = "Matemática"
            nota1 = float(input(f"Digite a nota de {materia}: "))
        elif j == 1:
            materia = "Ciências"
            nota2 = float(input(f"Digite a nota de {materia}: "))
        elif j == 2:
            materia = "Historia"
            nota3 = float(input(f"Digite a nota de {materia}: "))
        else:
            raise IndexError("Out of range.")
    tupla_notas = (nota1,nota2,nota3)
    dicionario_alunos["notas"] = tupla_notas
    dicionario_alunos["media"] = sum(tupla_notas)/len(tupla_notas)
    lista_alunos.append(dicionario_alunos)
    print("-"*40)

for i in range(len(lista_alunos)):
    print(f"Aluno {i+1}: {lista_alunos[i]["nome"]}")
    print(f"Idade: {lista_alunos[i]["idade"]}")
    print(f"Notas - \nMatemática: {lista_alunos[i]["notas"][0]}\nCiências: {lista_alunos[i]["notas"][1]}\nHistoria: {lista_alunos[i]["notas"][2]}")
    print(f"Média do aluno: {lista_alunos[i]["media"]}")
    print("-"*40)

maior_nota = sorted(lista_alunos, key=lambda item: item["media"], reverse=True)

print(f"A maior nota é do aluno: {maior_nota[0]["nome"]}\nCom média: {maior_nota[0]["media"]}.")