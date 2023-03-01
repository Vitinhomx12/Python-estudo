# Maior e menor
# Descrição: O script recebe 3 números e mostra o maior e menor.

numeros = []    #Lista que recebe os números

while True:
    try:   #Adiciona os números na lista 
        x = numeros.append(float(input("Digite um número: ")))
        y = numeros.append(float(input("Digite outro número: ")))
        z = numeros.append(float(input("Digite mais um número: ")))
    
        numeros.sort()  #Ordena a lista
    
        if numeros[0] != numeros[1] or numeros[1] != numeros[2]:
            print(f"O número maior é {numeros[2]} e o número menor é {numeros[0]}")
            input("\nPressione ENTER para continuar.")
            break

        else:
            print("Os números são iguais.")
            input("\nPressione ENTER para continuar.")
            break

    except ValueError:  #Trata input inválido
        print("Digite somente números.")