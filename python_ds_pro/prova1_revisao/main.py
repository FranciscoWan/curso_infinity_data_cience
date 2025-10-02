# Gerenciamento de Compras de Produtos
# Você foi contratado para desenvolver um programa que auxiliará no processo de compra de produtos em uma loja. O programa deve permitir que o usuário insira o nome e o preço de diversos produtos, e após a inserção de cada produto, deve perguntar se o usuário deseja adicionar mais produtos à lista. O processo de inserção de produtos continuará até que o usuário opte por parar.
# Ao término das inserções, o programa deve fornecer um resumo da compra com as seguintes informações:
# A) Total gasto na compra: O programa deve calcular e exibir a soma de todos os preços dos produtos inseridos.
# B) Quantidade de produtos que custam mais de R$1000: O programa deve contar e exibir quantos dos produtos cadastrados têm preço superior a R$1000.
# C) Nome do produto mais barato: O programa deve identificar e exibir o nome do produto com o menor preço.

dicionario_produtos = {}
total = 0
qtd_produtos_maior_1000 = 0

print("### Bem vindo ao gerenciador de compras ###")

while True:
    opc = str(input("Deseja adicionar mais compras?\nSim - Adicionar\nNão - Encerrar\nOpção: "))
    print("\n")
    if opc.lower().strip() in ["não", "nao", "n"]:
        print("Programa encerrado!")
        break
    elif opc.lower().strip() not in ["sim", "s"]:
        print("Opção inválida\nDigite uma opção válida\nSim | Não")
        print("\n")
        continue
    nome_produto = input("Nome do produto: ")
    dicionario_produtos[nome_produto] = int(input("Preço do produto: "))
    print("\n")

if len(dicionario_produtos) != 0:
    chave_menor_valor, menor_valor = min(dicionario_produtos, key=dicionario_produtos.get), min(dicionario_produtos.values())
else:
    chave_menor_valor, menor_valor = "Nenhum produto foi adquirido", 0

for c, v in dicionario_produtos.items():
    total += v
    if v > 1000:
        qtd_produtos_maior_1000 += 1

print("-"*60)
print(f"Número de produtos comprados: {len(dicionario_produtos)}.\nTotal da compra: R$ {total}.\nNúmeros de produtos que custam mais de R$ 1000: {qtd_produtos_maior_1000} itens.\nProduto mais barato: {chave_menor_valor} custando R${menor_valor}. ")
print("-"*60)