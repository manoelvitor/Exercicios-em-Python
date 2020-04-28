lista = []
opcao = 0
while opcao !=3 :
    opcao = int(input('[1] CADASTRAR | [2] EXIBIR LISTA | [3] SAIR |'))
    if opcao == 1:
        for i in range(1):
            arquivo = open('dadosSalvos.txt', 'w+')
            nome = input('Nome: ')
            idade = input('Idade: ')
            curso = input('Curso: ')
            periodo = input('Periodo: ')
            lista.append([nome, idade, curso, periodo])
            gravar=str(lista)
            arquivo.write(f'{gravar}\n')
            arquivo.close()
    elif opcao == 2:
        for i in lista:
            print(i)
    elif opcao == 3:
        print('Você, saiu do programa.')
    else:
        print('Opção inválida.')
