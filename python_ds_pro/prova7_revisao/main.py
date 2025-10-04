# Você tem um conjunto de dados fictícios que representa informações sobre a produção anual de diferentes culturas em várias fazendas ao longo de vários anos. Seu objetivo é realizar uma análise simples desses dados utilizando funções agregadoras.

# Tarefas:
# Encontre o ano com a produção total máxima e o ano com a produção total mínima:

# Você deve somar a produção total de todas as fazendas para cada ano e determinar qual foi o ano com a maior e a menor produção.
# Identifique a cultura com a maior e a menor produção total ao longo dos anos:

# Some a produção de cada cultura em todas as fazendas e anos, e identifique qual cultura teve a maior produção e qual teve a menor produção.
# Encontre a fazenda com a produção máxima e a fazenda com a produção mínima em um determinado ano:

# Selecione um ano e, dentro desse ano, identifique a fazenda que obteve a maior produção e a que obteve a menor produção.
# Dados Fictícios:
# Para simplificar, vamos construir dados fictícios representando a produção anual de três culturas (milho, soja e trigo) em três fazendas (Fazenda A, Fazenda B, Fazenda C) ao longo de três anos (2021, 2022, 2023).


import json

def importar_dados(nome_arquivo_p_abrir:str) -> dict:
    '''Importa o arquivo para análise posterior'''

    try:
        with open (nome_arquivo_p_abrir, "r") as data:
            data = json.load(data)
            return data
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo_p_abrir} não foi encontrado.")

def maior_menor_producao(dicionario_dados: dict) -> str:
    '''Calcula os anos de maior e menor produção considerando todas as fazendas'''

    totais_por_ano = {"2021": 0, "2022": 0, "2023": 0}

    for fazenda, dados_fazenda in dicionario_dados.items():
        for ano, culturas in dados_fazenda.items():
            totais_por_ano[ano] += sum(culturas.values())

    ano_maior = max(totais_por_ano, key=totais_por_ano.get)
    ano_menor = min(totais_por_ano, key=totais_por_ano.get)

    print("Produção total por ano:")
    for ano, total in totais_por_ano.items():
        print(f"  {ano}: {total}")

    print(f"\nAno com MAIOR produção: {ano_maior} ({totais_por_ano[ano_maior]})")
    print(f"Ano com MENOR produção: {ano_menor} ({totais_por_ano[ano_menor]})")

    return f"Ano com maior produção: {ano_maior}, ano com menor produção: {ano_menor}"

def cultura_maior_menor_producao(dicionario_dados: dict) -> str:
    '''Calcula a maior e menor produção entre as culturas'''

    totais_por_cultura = {"milho": 0, "trigo": 0, "soja": 0}

    for fazenda, dados_fazenda in dicionario_dados.items():
        for ano, culturas in dados_fazenda.items():
            for cultura, valor in culturas.items():
                totais_por_cultura[cultura] += valor

    cultura_maior = max(totais_por_cultura, key=totais_por_cultura.get)
    cultura_menor = min(totais_por_cultura, key=totais_por_cultura.get)

    print("Produção total por cultura (todas as fazendas e anos):")
    for cultura, total in totais_por_cultura.items():
        print(f"  {cultura.capitalize()}: {total}")

    print(f"\nCultura com MAIOR produção: {cultura_maior.capitalize()} ({totais_por_cultura[cultura_maior]})")
    print(f"Cultura com MENOR produção: {cultura_menor.capitalize()} ({totais_por_cultura[cultura_menor]})")

    return f"Cultura com maior produção: {cultura_maior}, cultura com menor produção: {cultura_menor}"

def maior_menor_producao_fazenda(dicionario_dados: dict) -> str:
    '''Determina qual a maior e menor produção por fazenda.'''

    total_prod_por_fazenda = {"fazenda_a": 0, "fazenda_b": 0, "fazenda_c": 0}

    for fazenda, ano in dicionario_dados.items():
        total_prod_por_fazenda[fazenda] = sum(ano["2021"].values()) + sum(ano["2022"].values()) + sum(ano["2023"].values())

    maior_prod_fazenda = max(total_prod_por_fazenda, key=total_prod_por_fazenda.get)
    menor_prod_fazenda = min(total_prod_por_fazenda, key=total_prod_por_fazenda.get)

    print(f"Fazenda com maior produção: {maior_prod_fazenda}\nFazenda com menor produção: {menor_prod_fazenda}")

    return f"Fazenda com maior produção: {maior_prod_fazenda}\nFazenda com menor produção: {menor_prod_fazenda}"


dados = importar_dados('dados.json')

maior_menor_producao(dados)
print("\n")
cultura_maior_menor_producao(dados)
print("\n")
maior_menor_producao_fazenda(dados)