class ingressoTeatro:
    def __init__(self):
        self.lin = 5
        self.col = 5
        self.totalLivre = self.lin*self.col
        print (f'Total de Cadeiras do Teatro: {self.totalLivre}')

    def montaTeatro(self,lin,col):
        self.matriz=[]
        c = 0
        for i in range (lin):
            fileira = []
            for j in range(col):
                if c == lin:
                    c = 0
                fileira.append('  Livre  ')
                c += 1
            self.matriz.append(fileira)

        return self.matriz


    def venderCadeira(self, matriz: object, posiFila: object, posiCadeira: object) -> object:
        matriz[posiFila][posiCadeira] = 'Reservado'
        c = 0
        for i in matriz:
            print(c,i)
            c += 1


    def devolverCadeira(self,matriz: object,posiFila: object,posiCadeira: object) -> object:
        c = 0
        if matriz[posiFila][posiCadeira] == 'Reservado':
            matriz[posiFila][posiCadeira] = '  Livre  '
            for i in matriz:
                print(c, i)
                c += 1


    def trocarCadeira(self, matriz: object, posiFila: object, posiCadeira: object )->object:
        if matriz[posiFila][posiCadeira] == 'Reservado':
            tPosiFilaCade = ''
            while tPosiFilaCade != '  Livre  ':
                trocaPFila = int(input('Fileira para qual deseja trocar:  '))
                trocaPCade = int(input('Cadeira para qual deseja trocar:  '))
                tPosiFilaCade = matriz[trocaPFila][trocaPCade]
                print('Está Cadeira já está reservado, escolha outra.')
            matriz[posiFila][posiCadeira] = '  Livre  '
            matriz[trocaPFila][trocaPCade] = 'Reservado'
            print(f'Você trocou o ingresso da fila {posiFila}, cadeira {posiCadeira}, para fila {trocaPFila} , cadeira {trocaPCade}')
            print('Troca efetuada com sucesso!')
        else:
            print('Está cadeira já está livre.')








'''opc=0
matriz=montaTeatro(5,5)
while opc != 4:
    opc = int(input(' [1] Vender | [2] Devolver | [3] Trocar | [4] Sair: '))
    if opc == 1:
        posiFileira = int(input('Fileira: '))
        posiCadeira = int(input('Cadeira: '))
        cadeiras = venderCadeira(matriz, posiFileira, posiCadeira)
        print(cadeiras)
        print(f'Você comprou o ingresso da fileira {posiFileira}, e cadeira {posiCadeira}')
    elif opc == 2:
        posiFileira = int(input('Fileira: '))
        posiCadeira = int(input('Cadeira: '))
        cadeiras = devolverCadeira(matriz, posiFileira, posiCadeira)
        print(cadeiras)
        print(f'Você devolveu o ingresso da fileira {posiFileira}, e cadeira {posiCadeira}')

    elif opc == 4:
        print('Obrigado volte sempre!')
    else:
        print('Opção invalida.')'''
