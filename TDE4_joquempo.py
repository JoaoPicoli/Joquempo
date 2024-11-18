import random # Biblioteca random para seleções aleatórias.

placar_jogador1 = 0 # Contabiliza o placar do jogador 1.
placar_jogador2 = 0 # Contabiliza o placar do jogador 2.

continuar_jogo = True 

while continuar_jogo: # Esse loop se repete o código do jogo enquanto a variável continuar_jogo é verdadeira.
    while True: 
       
        # Seleção do modo de jogo.
        modalidades = int(input(("""Modos de Jogo: 
===========================                    
(1) humano x humano
(2) humano x computador
(3) computador x computador
===========================
Selecione um modo de Jogo: """)))
        if modalidades > 0 and modalidades <= 3:  
            break  
        else:
            print("Por favor, selecione um número entre 1 e 3.") 
        
    # Validação do modo de jogo.
    hxh = modalidades == 1
    hxc = modalidades == 2
    cxc = modalidades == 3

    '''
    A seleção do modo de jogo é feita lendo uma entrada do jogador que pode ser 1, 2 ou 3, através
    da variável modalidades, e define o modo de jogo através das variáveis bools hxh, hxc e cxc,
    o valor delas é atribuído de acordo com a entrada, por exemplo: para hxh ser verdadeira a entrada
    em modalidades deve ser igual a 1.
    '''

    # Opções dentro do jogo
    opcoes = ['pedra','papel','tesoura']
    opcoes_escolhidas = []

    '''
    A lista opções contém 3 valores que vão ser verificados quando o jogador digitar a opção que deseja
    escolher dentro do jogo, elas são: pedra, papel e tesoura. 
    A lista opções escolhidas fica inicialmente vazia mas depois é preenchida depois que um jogador faz 
    uma escolha, usando append. 
    '''
    

    while len(opcoes_escolhidas) < 2: # Loop se repete até que a lista 'opções escolhidas' tenha 2 valores.
        if hxh:
            escolha = input('Escolha [Pedra, Papel, Tesoura]: ').lower()
            if escolha in opcoes:
                opcoes_escolhidas.append(escolha)
                print(f'· {escolha} selecionado!')
            else:
                print(f"'{escolha}' é uma escolha inválida.")

            escolha = input('Escolha [Pedra, Papel, Tesoura]: ').lower()
            if escolha in opcoes:
                opcoes_escolhidas.append(escolha)
                print(f'· {escolha} selecionado!')
            else:
                print(f"'{escolha}' é uma escolha inválida.")

            '''
            No modo de jogo humano x humano cada jogador deverá fazer uma escolha, que é 
            feita através de uma entrada, usando a variável 'escolha'. Em seguida, essa entrada
            é adicionada a ultima posição da lista 'opções escolhidas' caso esteja na lista 'opções',
            caso contrário o jogador deve digitar novamente.
            '''
                
        elif hxc:
            escolha = input('Escolha [Pedra, Papel, Tesoura]: ').lower()
            if escolha in opcoes:
                opcoes_escolhidas.append(escolha)
                print(f'· {escolha} selecionado!')

                escolha = random.choice(opcoes)
                opcoes_escolhidas.append(escolha)
                print(f'· {escolha} selecionado!')

            else:
                print(f"'{escolha}' é uma escolha inválida.")

            '''
            Aqui a lógica é a mesma, a escolha do jogador é adicionada ao fim da lista 
            'opções escolhidas' caso esteja na lista 'opções'. O computador támbem faz 
            a mesma coisa, mas a sua escolha é definida aleatoriamente usando a através 
            da função random.choice, que adiciona 
            a escolha ao fim da lista 'opções escolhidas'.
            '''

        elif cxc:
            escolha = random.choice(opcoes)
            if escolha in opcoes:
                opcoes_escolhidas.append(escolha)
                print(f'· O computador 1 escolheu {escolha.upper()}!')

            escolha = random.choice(opcoes)
            if escolha in opcoes:
                opcoes_escolhidas.append(escolha)
                print(f'· O computador 2 escolheu {escolha.upper()}!')
            
            '''
            Novamente a escolha é feita através da função random.choice e adicionada 
            ao fim da lista 'opções escolhidas'.
            '''

    pedra = 'pedra' in opcoes_escolhidas 
    papel = 'papel' in opcoes_escolhidas 
    tesoura = 'tesoura' in opcoes_escolhidas 
    '''
    Seguindo a mesma lógica da escolha do modo de jogo, existem 3 bools e elas se tornam
    verdadeiras caso a string equivalente ao seu próprio nome esteja na lista 'opções escolhidas'.
    '''

    # Lógica de vitória
    if opcoes_escolhidas[0] == 'pedra' and opcoes_escolhidas[1] == 'tesoura':
        print('Jogador 1 ganhou (PEDRA)')
        placar_jogador1 += 1
    elif opcoes_escolhidas[0] == 'tesoura' and opcoes_escolhidas[1] == 'pedra':
        print('Jogador 2 ganhou (PEDRA)')
        placar_jogador2 += 1
    elif opcoes_escolhidas[0] == 'papel' and opcoes_escolhidas[1] == 'pedra':
        print('Jogador 1 ganhou (PAPEL)')
        placar_jogador1 += 1
    elif opcoes_escolhidas[0] == 'pedra' and opcoes_escolhidas[1] == 'papel':
        print('Jogador 2 ganhou (PAPEL)')
        placar_jogador2 += 1
    elif opcoes_escolhidas[0] == 'tesoura' and opcoes_escolhidas[1] == 'papel':
        print('Jogador 1 ganhou (TESOURA)')
        placar_jogador1 += 1
    elif opcoes_escolhidas[0] == 'papel' and opcoes_escolhidas[1] == 'tesoura':
        print('Jogador 2 ganhou (TESOURA)')
        placar_jogador2 += 1
    else:
        print('EMPATE')

    '''
    Aqui é definido quem foi o vencedor de cada rodada. Usando de exemplo
    a vitória de pedra: Se o indíce 0 for igual a string 'pedra' e o indice
    1 for igual a string 'tesoura', então ele imprime qual jogador ganhou e qual
    foi a opção selecionada por ele. 
    '''

    
    # placar
    print(f'PLACAR GERAL: J1: {placar_jogador1}  J2:{placar_jogador2}')
    


    continuar = input('''(1) continuar jogando
(2) encerrar jogo
selecione: ''')
    while True:
        if continuar == '1':
            print('NOVA RODADA...')
            break
        elif continuar == '2':
            continuar_jogo = False
            print(f'PLACAR GERAL: J1: {placar_jogador1}  J2:{placar_jogador2}')
            print('Obrigado por jogar. Desenvolvido por João Picoli')
            print('JOGO ENCERRADO')    
            break
        else:
            print('entrada inválida')
            continuar = input('''(1) continuar jogando
(2) encerrar jogo
selecione: ''')
        
    '''
    No final de cada rodada o jogador pode digitar 1 para continuar o jogo ou 2 para encerrar.
    Essa entrada é lida através da variável continuar, caso ela seja igual à 1 uma mensagem
    dizendo novo jogo é impressa e o loop acaba, mas uma nova rodada se inicia pois a condição
    que mantém o loop principal rodadno ainda é verdadeira. 
    Caso seja igual à 2 uma mensagem dizendo jogo encerrado é impressa, o valor da variável 
    'continuar jogo' é alterado pra falso e o loop acaba, e consequentente o código inteiro.
    Qualquer outra entrada é inválida e o jogador tem que digitar novamente.
    O placar final também é exibido.
    '''