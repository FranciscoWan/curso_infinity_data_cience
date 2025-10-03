# Desenvolva um programa em Python que funcione como um processador de texto simples. O programa deverá realizar diversas operações em um texto fornecido, incluindo:

# Contar palavras
# Contar letras
# Inverter o texto
# Substituir palavras-chave

# Requisitos:
# Crie uma função chamada processador_texto que aceite uma string de texto como argumento.

# A função também deve aceitar uma série de operações através de argumentos de palavra-chave usando **kwargs. As operações que podem ser realizadas incluem:

# "contar_palavras": Contar o número de palavras no texto.
# "contar_letras": Contar o número de letras no texto (desconsiderando espaços).
# "inverter_texto": Inverter o texto de entrada.
# "substituir_palavra": Substituir uma palavra específica no texto por uma nova palavra.
# Utilize funções lambda para realizar as operações de acordo com as palavras-chave especificadas nos argumentos de **kwargs.

# Para a operação de substituição de palavras, a função deve aceitar palavras adicionais: uma palavra a ser substituída (por exemplo, substituir_palavra) e uma nova palavra (por exemplo, nova_palavra).

# A função deve aplicar todas as operações em sequência e retornar o texto resultante após todas as operações.

def processador_texto(frase_para_processar:str, troca_palavra=False) -> tuple[int, int, str] | tuple[int, int, str, str]:
    '''Recebe um texto e o processa, retornando: 
    O número de palavras no texto
    O número de letras (incluíndo os espaços)
    O texto invertido
    Substitui palavras-chave
    --- Caso queira trocar alguma palavra, passar o valor da nova palavra para o parâmetro 'troca_palavra' e retorna a nova frase ---
    '''
    lista_palavras_texto = frase_para_processar.split(" ")
    palavras_no_texto = len(lista_palavras_texto)
    num_letras = len(frase_para_processar)
    txt_invertido = frase_para_processar[::-1]
    if troca_palavra:
        lista_nova_frase = []
        palavra_para_trocar = str(input("Digite a palavra que deseja trocar: "))
        nova_palavra = str(input("Digite a nova palavra: "))
        for palavra in lista_palavras_texto:
            if palavra == palavra_para_trocar:
                palavra = nova_palavra
            lista_nova_frase.append(palavra)
        return palavras_no_texto, num_letras, txt_invertido, " ".join(lista_nova_frase)
    return palavras_no_texto, num_letras, txt_invertido

print(processador_texto("Olá mundo", troca_palavra=True))


