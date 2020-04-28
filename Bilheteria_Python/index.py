import Teatro
mt = Teatro.ingressoTeatro()
cadeiras = mt.montaTeatro(mt.lin,mt.col)
opc = 0
while  opc != 4:
    opc = int(input('[0] MAPA DE CADEIRAS | [1] Vender | [2] Devolver | [3] Trocar | [4] Sair: '))
    if opc == 1:
        print(15*'#','VENDER INGRESSO',15*'#')
        posiFila=int(input('Fileira desejada: '))
        posiCade=int(input('Cadeira da fileira desejada: '))
        if cadeiras[posiFila][posiCade] == '  Livre  ':
            mt.venderCadeira(cadeiras, posiFila, posiCade)
            print(f'Você comprou o ingresso da fileira {posiFila}, e cadeira {posiCade}')
        else:
            print('Lugar já vendido.')
    elif opc == 2:
            print(15*'#','DEVOLUÇÃO DE INGRESSO',15*'#')
            posiFila = int(input('Fileira desejada: '))
            posiCade = int(input('Cadeira da fileira desejada: '))
            if cadeiras[posiFila][posiCade] == 'Reservado':
                mt.devolverCadeira(cadeiras,posiFila,posiCade)
                print('Devolução efetuada com sucesso!')
            else:
                print('Lugar já está livre.')
    elif opc == 3:  
        print(15*'#', 'TROCA DE INGRESSO', 15*'#')
        posiFila = int(input('Fileira desejada: '))
        posiCade = int(input('Cadeira da fileira desejada: '))
        mt.trocarCadeira(cadeiras,posiFila,posiCade)
        '''if posiFilaCade == 'Reservado':
            tPosiFilaCade = ''
            while tPosiFilaCade != 'Reservado':
                trocaPFila = int(input('Fileira para qual deseja trocar:  '))
                trocaPCade = int(input('Cadeira para qual deseja trocar:  '))
                tPosiFilaCade = cadeiras[trocaPFila][trocaPCade]
                if tPosiFilaCade == 'Reservado':
                    print('Está Cadeira já está reservado.')
                else:
                    tPosiFilaCade = 'Reservado'
                    print(f'Você trocou o ingresso da fila {posiFila}, cadeira {posiCade}, para fila {trocaPFila} , cadeira {trocaPCade}')
                    print('Troca efetuada com sucesso!')
        else:
            print('Está cadeira já está livre.')'''
    elif opc == 0:
        print(15*'#', 'MAPA DE CADEIRAS', 15*'#')
        c = 0
        for i in cadeiras:
            print(c, i)
            c += 1
    elif opc == 4:
        print('Saindo...')
    else:
        print('Opção Inválida, escolha novamente uma opção!')





