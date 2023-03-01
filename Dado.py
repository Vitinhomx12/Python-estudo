# Dado
# Descrição: Programa que joga um dado virtual com números de 1 a 6.


pergunta = input("Você gostaria de jogar o dado? ").capitalize() #Pergunta de entrada
sim = ['Sim', 'S', 'Gostaria', 'Claro']     #Respostas positivas
nao = ['Nao', 'Não', 'N']                   #Respostas negativas

from random import randint        #importa função que gera número aleatório

#Enquanto for positivo, o loop continua.
while True:
    if pergunta in sim:     #Se usuario responder positivamente
        print(randint(1,6))
        pergunta = input("Gostaria de jogar novamente? ").capitalize()
    elif pergunta in nao:   #Se usuario responder negativamente
        print("Ok, programa encerrado.")
        break        
    else:                   #Tratamento de respostas inválidas
        pergunta = input("Por favor, responda com sim ou não: ").capitalize()
        continue