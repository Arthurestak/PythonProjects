import os 
import random as rd

numero_cpfs = input('Digite quantos CPFs você quer: ')

numero_cpfs = int(numero_cpfs)

numero_cpfs_para_range = numero_cpfs + 1

numerador = 0

for i in range(1,numero_cpfs_para_range):
    decrescenteUm = 10

    contador = 9

    cpf_nove_digitos = []

    while contador >= 1:
        cpf_nove_digitos.append(rd.choice(range(0,10)))
        contador -= 1  
        continue
    
    if len(cpf_nove_digitos) == 9:

        cpf_multi = []

        for i in cpf_nove_digitos:

            try:
                iNum = int(i)
            except:
                os.system('cls')
                print('Digite um valor válido!')
                continue

            multi = decrescenteUm * iNum

            cpf_multi.append(multi)

            decrescenteUm -= 1 



        soma = sum(cpf_multi)    

        multi2 = soma * 10

        resto = multi2 % 11
    else:
        print('Digite um valor válido, apenas os 9 primeiros números!\n')
        

    decrescenteDois = 11


    cpf_novo_lista = []
    for i in cpf_nove_digitos:
        cpf_novo_lista.append(i)
    cpf_novo_lista.append(resto) if resto <= 9 else cpf_novo_lista.append(0)

    cpf_multi2 = []
    cpf_completo = []
    for i in cpf_novo_lista:
        iNum = int(i)
        multi3 = decrescenteDois * iNum
        cpf_multi2.append(multi3)
        decrescenteDois -= 1 

    soma2 = sum(cpf_multi2)
    multi4 = soma2 * 10    
    resto2 = multi4 % 11
    numerador += 1
    if resto2 <= 9:
        cpf_novo_lista.append(resto2)
        print(f'CPF {numerador} gerado: ',"".join(map(str,cpf_novo_lista)))
    else:
        cpf_novo_lista.append(0)
        print(f'CPF {numerador} gerado: ',"".join(map(str,cpf_novo_lista)))
