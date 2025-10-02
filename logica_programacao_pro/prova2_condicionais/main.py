# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

velocidade = int(input("Digite a velocidade do carro: "))

if velocidade > 80:
    excede = velocidade - 80
    multa = excede * 20
    print(f"Você excedeu o limite de velocidade em {excede}km/h e sua multa foi de R${multa},00.")
else:
    print(f"Você está dentro da velocidade permitida de 80km/h e passou a {velocidade}hm/h.")   