# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada.

print("### Gerador de Tabuada ###")
num = int(input("Digite um número para ver a tabuada: "))
print("-"*40)

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")