# Chute um número
# Descrição: Jogo onde você deve advinhar o número gerado pelo computador.

from random import randint #Importa função para gerar número aleatório

computador = randint(0,100) #Armazena o número aleatório gerado

while True:
    try:
        usuario = int(input("Chute um número entre 1 e 100: "))   #Tentativa do usuário
        if usuario > computador:
            print("Chutou alto, tente novamente.\n")
            
        elif usuario < computador:
            print("Chutou baixo, tente novamente.\n")

        elif usuario == computador:
            print(f"Parabéns, você acertou! O número é: {computador}")
            input("\nPressione ENTER para continuar.")
            break
    except ValueError:      #Trata input inválido
        print ("Por favor, utilize somente números inteiros.")
        