"CardGameAdvinhação."


from random import randint
from time import sleep

def criaBaralho():
    cartas = ['A', 2, 3, 4, 5, 6, 7, 'Q', 'J', 'K']
    naipes = ['♠', '♣', '♥', '♦']
    baralho = []

    print("Criando o baralho", end='')
    espera()

    for carta in cartas:
        for naipe in naipes:
            baralho.append((carta, naipe))
    print(f"Baralho criado com {len(baralho)} cartas.")
    print(f"Para este jogo precisaremos de 21 cartas. Portanto, 19 cartas serão descartadas", end='')
    espera()

    for carta in range(len(baralho) - 21):
        baralho.pop() # descarta a última carta em b
    
    print(f"O baralho agora possui {len(baralho)} cartas.")

    return baralho

# faz a função de embaralhar as cartas no baralho b
def embaralhar(b):
    embaralhado = []
    print("Embaralhando", end='')
    espera()
    while len(b) > 0:
        r = randint(0, len(b)-1)
        embaralhado.append(b.pop(r))

    b = embaralhado
    print("Ok!") # agora o baralho está embaralhado
    return b

def showBaralho(b):
    for i in range(len(b)):
        if b[i][1] == '♥' or b[i][1] == '♦':
            print("\033[31m", end='') #pinta de vermelho
            print(f"|{b[i][0]}{b[i][1]}| ", end='')
            print("\033[m", end='')
        else:
            print("\033[37m", end='')  # pinta de preto
            print(f"|{b[i][0]}{b[i][1]}| ", end='')
            print("\033[m", end='')

    print("\n")

def porNaMesa(b):
# coluna1 = 0, 3, 6, 9, 12, 15, 18
# coluna2 = 1, 4, 7, 10, 13, 16, 19
# coluna3 = 2, 5, 8, 11, 14, 17, 20
    mesa = ([], [], [])

    for i in range(0, len(b), 3):
        mesa[0].append(b[i])

    for i in range(1, len(b), 3):
        mesa[1].append(b[i])

    for i in range(2, len(b), 3):
        mesa[2].append(b[i])

    return mesa

def ondeEstaCarta(m):
    resp = 5
    while True:
        try:
            resp = int(input("Em qual coluna aparece a carta memorizada? [1/2/3] ".upper()))
        except:
            pass
        if resp == 1 or resp == 2 or resp == 3:
            break
    m2 = m
    topo = m[0]
    centro = m[1]
    fundo = m[2]

    if resp == 1: #0
        topo = m2[1]
        centro = m2[0]
        fundo = m2[2]

    elif resp == 2: #1
        topo = m2[0]
        centro = m2[1]
        fundo = m2[2]

    elif resp == 3: #2
        topo = m2[0]
        centro = m2[2]
        fundo = m2[1]

    else:
        print("Resposta inválida. Jogo encerrado.")

    m = (topo, centro, fundo)

    b = []
    for c in range(0, 3):
        for l in range(0, 7):
            b.append(m[c][l])

    return m, b

def showMesa(m):

    for i in range(0, 3):
        print("-="*20)
        print(f"\033[33mColuna {i+1}: \033[m", end='')
        for l in range(0, 7):
            if m[i][l][1] == '♥' or m[i][l][1] == '♦':
                print("\033[31m", end='') # pinta de vermelho
                print(f"|{m[i][l][0]}{m[i][l][1]}| ", end='')
                print("\033[m", end='')
            else:
                print("\033[37m", end='')  # pinta de preto
                print(f"|{m[i][l][0]}{m[i][l][1]}| ", end='')
                print("\033[m", end='')
        sleep(1)
        print("\n")
    print("-=" * 20)

def advinha(b):
    print("Deixe-me advinhar a sua carta 🤨", end='')
    espera()
    if b[10][1] == '♥' or b[10][1] == '♦':
        print(f"A carta que você memorizou foi \033[31m |{b[10][0]}{b[10][1]}| \033[m", end='')

    else:
        print(f"A carta que você memorizou foi \033[37m |{b[10][0]}{b[10][1]}| \033[m", end='')

    print("\n")

def espera():
    print(".", end='')
    sleep(1)
    print(".", end='')
    sleep(1)
    print(".")
    sleep(1)

def jogo():
    baralho = criaBaralho()
    baralho = embaralhar(baralho)

    showBaralho(baralho)
    input(("Memorize uma carta acima. Quando estiver pronto, pressione enter "))

    for i in range(3):
        mesa = porNaMesa(baralho)
        showMesa(mesa)
        mesa, baralho = ondeEstaCarta(mesa)

    advinha(baralho)

jogo()