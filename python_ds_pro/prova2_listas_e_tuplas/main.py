# Você está responsável por gerenciar os resultados de uma competição esportiva. 
# Para isso, você tem uma lista de tuplas onde cada tupla representa uma equipe e suas respectivas 
# pontuações em diferentes rodadas. O formato de cada tupla é: ('nome_da_equipe', [lista_de_pontuacoes]).

# Tarefas a serem realizadas:
# Calcular a média das pontuações: Para cada equipe, calcule a média de suas pontuações e armazene esses valores em uma nova lista chamada medias. Cada média deve corresponder à equipe respectiva.
# Ordenar as médias: Organize a lista medias em ordem decrescente, de modo que a equipe com a maior média apareça primeiro.
# Criar uma lista de classificação: Crie uma nova lista chamada classificacao, que contenha tuplas. Cada tupla deverá ter o nome da equipe e sua média de pontuações, seguindo a ordem decrescente da média.
# Exibir a classificação final: Mostre na tela a classificação final das equipes, exibindo o nome da equipe e sua média, da equipe com a maior média para a menor.

lista_classificacao = []

qtd_equipes = int(input("Digite o número de equipes da competição: "))

for i in range(1, qtd_equipes+1):
    lista_pontuacao = []
    nome_equipe = str(input(f"Digite o nome da {i}º equipe: "))
    qtd_rodadas = int(input(f"Digite o número de rodadas que a equipe {nome_equipe} participou: "))
    for j in range(1, qtd_rodadas+1):
        pontuacao = float(input(f"Digite a pontuação de {j}º rodada: "))
        lista_pontuacao.append(pontuacao)
    media = sum(lista_pontuacao)/len(lista_pontuacao)
    estrutura_tupla = (nome_equipe, lista_pontuacao, media)
    lista_classificacao.append(estrutura_tupla)

lista_ordenada = sorted(lista_classificacao, key=lambda item: item[2], reverse=True)

for i in lista_ordenada:
    print("-"*40)
    print(f"### {i[0]} ###")
    print("Pontuação: ", end="")
    for j in i[1]:
        print(f"{j}", end="  ")
    print(f"\nMédia: {i[2]}")





