import os 

while True:
    decrescenteUm = 10
    cpf_nove_digitos = input('Digite os 9 primeiros dígitos do CPF (Não inclua ponto.): ')
    confirma = input('Digite "Enter" se digitou corretamente e "N" se não: ').lower()
    os.system('cls')
    if confirma.startswith('n'):
        continue
    if len(cpf_nove_digitos) == 9:

        cpf_multi = []

        for [i] in cpf_nove_digitos:

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

        if resto >= 10:
            print('O próximo número do CPF é: 0')

            reiniciar = input('Digite [S] se deseja refazer operação, e ENTER para prosseguir: ').lower()

            if reiniciar.startswith('s'):
                os.system('cls')
                continue
            else:
                os.system('cls')
                break
        else:
            print('O próximo número do CPF é: ',resto)
            
            reiniciar = input('Digite [S] se deseja refazer operação, e ENTER para prosseguir: ').lower()

            if reiniciar.startswith('s'):
                os.system('cls')
                continue
            else:
                os.system('cls')
                break
    else:
        print('Digite um valor válido, apenas os 9 primeiros números!\n')
        continue

decrescenteDois = 11

cpf_dez_digitos = input('Deseja que eu descubra o último número também? [S], [N] ').lower()
os.system('cls')
if cpf_dez_digitos.startswith('s'):
    cpf_novo_lista = []
    for [i] in cpf_nove_digitos:
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

    if resto2 <= 9:
        cpf_novo_lista.append(resto2)
        print('O seu CPF completo é: ',"".join(map(str,cpf_novo_lista)))
else:
    os.system('cls')
    ...
