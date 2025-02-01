import os 

while True:
    decrescente = 10
    cpf_entrada = input('Digite os 9 primeiros dígitos do CPF (Não inclua ponto.): ')
    confirma = input('Digite "Enter" se digitou corretamente e "N" se não!').lower()
    os.system('cls')
    if confirma.startswith('n'):
        continue
    if len(cpf_entrada) == 9:

        cpf_multi = []

        for [i] in cpf_entrada:

            try:
                iNum = int(i)
            except:
                os.system('cls')
                print('Digite um valor válido!')
                continue

            multi = decrescente * iNum

            cpf_multi.append(multi)

            decrescente -= 1

        a,b,c,d,e,f,g,h,i = cpf_multi

        soma = a+b+c+d+e+f+g+h+i    

        multi2 = soma * 10

        resto = multi2 % 11

        if resto >= 10:
            print('O próximo número do CPF é: 0')

            reiniciar = input('Digite [S] se quiser realizar outra operação, e [N] para sair: ').lower()

            if reiniciar.startswith('s'):
                os.system('cls')
                continue
            elif reiniciar.startswith('n'):
                os.system('cls')
                break
            else:
                print('Digite uma das duas opções [S], [N]!!')
                continue
        else:
            print('O próximo número do CPF é: ',resto)
            
            reiniciar = input('Digite [S] se quiser realizar outra operação, e [N] para sair: ').lower()

            if reiniciar.startswith('s'):
                os.system('cls')
                continue
            elif reiniciar.startswith('n'):
                os.system('cls')
                break
            else:
                print('Digite uma das duas opções [S], [N]!!')
                continue
    else:
        print('Digite um valor válido, apenas os 9 primeiros números!\n')
        continue
