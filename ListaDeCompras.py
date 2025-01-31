import os

print('BEM VINDO À SUA LISTA DE COMPRAS!\n')

itens_inseridos = []


while(True):
    print("LISTA:")
    for indice, nome in enumerate(itens_inseridos):
        print(indice,nome)
    print('\n')
    opcao = input('Selecione a opção que deseja executar:\n[I]nserir, [A]pagar, [L]istar: ').lower()
    
    if opcao.startswith('i'):
        os.system('cls')
        inserir = input('Item: ')
        itens_inseridos.append(inserir)
        os.system('cls')
        
        
    elif opcao.startswith('a'):
        os.system('cls')
        for i,n in enumerate(itens_inseridos):
            print(i,n)
        print('\n')
        apagar = input("Apagar item: ")
        os.system('cls')

        if not apagar.isdigit():
            print('Digite apenas o índice!\n')
            continue
        else:
            apagar1 = int(apagar)
        if 0 <= apagar1 < len(itens_inseridos):
            item_removido = itens_inseridos.pop(apagar1)
            print('Item: ',item_removido, 'apagado com sucesso!')
        else: print('Indice inválido!')
    
    elif opcao.startswith('l'):
        if len(itens_inseridos) >= 1:
            os.system('cls')
            print('LISTA:')
            for i,n in enumerate(itens_inseridos):
                print(i,n)
            print('\n')
            sair_lista = input('Tecle ENTER para voltar ao menu...')
            os.system('cls')
            continue
        else:
            print('Ainda não há itens na lista')
    else:
        os.system('cls')
        print('Digite alguma das operações [I],[A],[L] \n!')
        continue









#os.system('cls')