# Escreva um programa em python que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

num = 1
soma = 0
qtd_num = 0
while num != 0:
    print("-"*40)
    num = int(input("Digite um número qualquer.\n0 - Encerra\nNúmero: "))
    if num != 0:
        soma += num
        qtd_num += 1
    print("\n")

if qtd_num == 0:
    qtd_num = 1

media = soma/qtd_num
print(f"Quantia de números: {qtd_num}\nSoma: {soma}\nMédia: {media:.2f}")
