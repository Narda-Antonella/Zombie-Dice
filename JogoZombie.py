'''Narda Antonella Choque Morales'''
'''Projeto ZOMBIE DICE'''

# Messagem que bem-vinda que aparecerá na tela
import random

print('Bem-vindo ao jogo ZOMBIE DICE!!');

# Lista para armazenar dados
tubo = []
listajogadores = []
play = True

# Definição do lado dos dados 'C' para cérebro, 'P' para pasos e 'T' para tiro
D_verde = ('CPCTPC')
D_amarelo = ('TPCTPC')
D_vermelho = ('TPTCPT')

# Quantidade de número de jogadores, se for maior que 1 irá imprimir iniciar jogo
numberplayers = int(input('entre com a quantidade de jogadores:\n'))

# Estrutura de repetição
while play:
    if numberplayers < 2: # Se o número de jogagores for menor que 2 aparecera a msg do print
        print('PARA INCIAR O JOGO PRECISA NO MINIMO 2 JOGADORES')
    else:
        print('INICIAR JOGO!') # Senão irá aparecer iniciar jogo

        for ind in range(0, numberplayers):  ##quantidade de jogadores
            nome = str(input('Digite o nome dos jogadores:\n*'))
            Cerebro = 0
            Tiro = 0
            Passos = 0


# Estrutura lista para contabilizar os nomes,cerebros e tiros
            jogador = [ind, nome, Cerebro, Tiro]
            listajogadores.append(jogador) #adiciona um jogador na lista

##adicionar os 13 dados no tubo
        for i in range(0, 6):
            tubo.append(D_verde)
        for i in range(0, 4):
            tubo.append(D_amarelo)
        for i in range(0, 3):
            tubo.append(D_vermelho)

# rodada do jogo por turnos
        for jogador in range(len(listajogadores)): #para os jogadores da lista de jogadores
            print(listajogadores[jogador][1])
            turno = True

            while turno == True: #enquanto for verdadeiro vai sortear os dados
                dado1 = random.choice(tubo)
                dado2 = random.choice(tubo)
                dado3 = random.choice(tubo)
        # sortear o lado dos dados
                ladodado1 = random.choice(dado1)
                ladodado2 = random.choice(dado2)
                ladodado3 = random.choice(dado3)
        # Condicionais lado dos dados, Cérebro, Tiro e Passos do lado 1, 2 e 3
                if ladodado1 == 'C':
                    print('você comeu um cérebro!')
                    Cerebro = Cerebro + 1      # O Cerébro + 1 irá adicionar um Cérebro para a lista de cada jogador e assim irá somar quantos cada um recebeu cada jogador
                elif ladodado1 == "T":
                    print('você recebeu um Tiro!')
                    Tiro = Tiro + 1        # O Tiro + 1 irá adicionar um Tiro para a lista de cada jogador e assim irá somar quantos cada um recebeu cada jogador
                else:  #se não sorteou nenhum dos dados de cima então o programa entende que deberá printar na tela que o jogador ganhou um passo
                    print('você ganhou um Passo!')
                    Passos = Passos + 1

                if ladodado2 == 'C':
                    print('você comeu um cérebro!')
                    Cerebro = Cerebro + 1
                elif ladodado2 == "T":
                    print('você recebeu um Tiro!')
                    Tiro = Tiro + 1
                else:
                    print('você ganhou um Passo!')
                    Passos = Passos + 1

                if ladodado3 == 'C':
                    print('você comeu um cérebro!')
                    Cerebro = Cerebro + 1
                elif ladodado3 == "T":
                    print('você recebeu um Tiro!')
                    Tiro = Tiro + 1
                else:
                    print('você ganhou um Passo!')
                    Passos = Passos + 1

                print(Cerebro)
                print(Tiro)
                print(Passos)

                if Tiro > 2: # se o jogador recebeu mais de 2 tiros aparecerá na tela que o jogador perdeu
                    print("você perdeu!")
                    turno = False  # se o jogador perder o jogo irá finalizar para o jogador
                    play = False
                if Cerebro > 12:  # se o jogador recebeu mais de 12 Cerebros aparecerá na tela que o jogador ganhou
                        print("você ganhou!")
                        turno = False # se o jogador perder o jogo irá finalizar
                        play = False
                playGame = input('continuar ou sair do jogo: (sim / não)\n') #aparecerá na tela uma pergunta para o jogador
                if playGame == "sim":  #se o jogador digitar sim, ira rodar o dado
                    print('rodar dado')
                    turno = False
                    play = False
                else: # se digitar não o jogo acabará
                    print("você saiu do jogo")
                    turno = False
                    play = False