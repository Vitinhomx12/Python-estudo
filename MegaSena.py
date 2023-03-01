# Mega Sena
# Descrição: Programa que gera números aleatórios para Mega Sena.

import random

jogos = int(input("Quantidade de jogos: " ))

for jogo in range (jogos):
    numeros = (random.sample(range(1,61),6))
    numeros.sort()
    print(numeros)
    
print("\nBoa sorte !!!")
input("Pressione Enter para continuar.")