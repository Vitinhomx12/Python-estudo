# CPF
# Descrição: Programa criado com a finalidade de validação e geração de CPF's.

from random import randint

def validar_cpf(cpf):
    #Remove a pontuação
    cpf = ''.join(x for x in cpf if x.isalnum())
    
    #Verifica se o CPF possui 11 digítos
    if len(cpf) != 11:
        return False

    #Verifica se o CPF é composto de números repetidos
    if cpf == cpf[::-1]:
        return False

    digito1 = 0
    digito2 = 0
    
    #Primeiro dígito verificador
    for i,r in enumerate(range(10,1,-1)):
        calculo1 = int(cpf[i])*r
        digito1 += calculo1
    digito1 = (((digito1 * 10) %11) %10)
    
    #Segundo dígito verificador
    for i2,r2 in enumerate(range(11,1,-1)):
        calculo2 = int(cpf[i2])*r2
        digito2 += calculo2    
    digito2 = (((digito2 * 10) %11) %10) 
    
    #Verifica se os dígitos são correspondentes ao do CPF
    if str(digito1) == cpf[-2] and str(digito2) == cpf[-1]:
        return True 
        
def gerar_cpf():
    #Gera os primeiros 9 números e verifica se não são iguais
    while True:
        cpf = str(randint(100000000,999999999))
        if str(cpf) != str(cpf)[::-1]:
            break
    
    digito1 = 0
    digito2 = 0

    #Gera primeiro dígito verificador
    for i,r in enumerate(range(10,1,-1)):
        calculo1 = int(cpf[i])*r
        digito1 += calculo1
    digito1 = (((digito1 * 10) %11) %10)
    cpf += str(digito1)
    
    #Gera o segundo dígito verificador
    for i2,r2 in enumerate(range(11,1,-1)):
        calculo2 = int(cpf[i2])*r2
        digito2 += calculo2    
    digito2 = (((digito2 * 10) %11) %10)
    cpf += str(digito2)

    return cpf

#Menu de opções
while True:
    print("-=-"*15)
    print("           DIGITE A OPÇÃO DESEJADA")
    print("-=-"*15)
    print('''    OPÇÕES: 
    [1] VALIDAR UM CPF
    [2] GERAR UM CPF
    [3] SAIR\n''')
    opcao = input("Escolha: ")
    
    if opcao == "1":
        cpf = input("\nDigite o CPF para validação: ")
        if validar_cpf(cpf):
            print("\nO CPF informado é VÁLIDO.\n")
            input("Pressione ENTER para continuar.")
            break
        else:
            print("\nO CPF informado é INVÁLIDO.\n")
            input("Pressione ENTER para continuar.")
            break
    elif opcao == "2":
        cpf = gerar_cpf()
        if validar_cpf(cpf):
            print(f"\nCPF gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}\n")
            input("Pressione ENTER para continuar.")
            break
    elif opcao == "3":
        input("\nPrograma encerrado, pressione ENTER para continuar.\n")
        break
    else:
        print("\nOpção inválida\n")
        continue 