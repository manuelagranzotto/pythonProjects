######### JOGOS SANTA CASA - EUROMILHÕES ######### 

'''
Para jogar:
Escolher 5 números na tabela "números" [1:50]
Escolher 2 números na tabela "estrelas" [1:12]

ORDEM DE PREMIOS:
Premio 01 ->    5 números + 2 estrelas da sorte: €1.000.000
Premio 02 ->    5 números + 1 estrela da sorte:  €250.000
Premio 03 ->    5 números + 0 estrela da sorte:  €18.000
Premio 04 ->    4 números + 2 estrelas da sorte: €1.000
Premio 05 ->    4 números + 1 estrela da sorte:  €100
Premio 06 ->    3 números + 2 estrelas da sorte: €40
Premio 07 ->    4 números + 0 estrela da sorte:  €35
Premio 08 ->    2 números + 2 estrelas da sorte: €10
Premio 09 ->    3 números + 1 estrela da sorte:  €9
Premio 10 ->    3 números + 0 estrela da sorte:  €8
Premio 11 ->    1 número  + 2 estrela da sorte:  €5
Premio 12 ->    2 números + 1 estrela da sorte:  €4
Premio 13 ->    1 número  + 2 estrelas da sorte: €3

'''
import random

# define functions
"""
Essa função são usadas para gerar números aleatórios e não repetidos, utilizando como parâmetro o tamanho da lista
Os valores serão armazenados nas variáveis globais winningNumbers e winningStars
"""
def getRandom(size, min, max):
    listNum = []
    while True:
        if len(listNum) == size:
            return listNum
        number = random.randint(min,max)
        if number not in listNum:
            listNum.append(number)

"""
Essa função vai retornar as listas geradas do input do usuário.
Esses valores serão armazenados nas variáveis globais betNumbers e betStars
Os parâmetros vão ser o tamanho da lista, e uma mensagem apenas para ajudar na mensagem ao usuário.

A função getValue serve de apoio para verificar os limites mínimo e máximos do input do usuário
"""
# Função para receber os números VÁLIDOS dos números e das entrelas
def getValue(count, min, max, msg):
    while True:
        print(f"Digite um número entre [{min}:{max}]: ")
        num = int(input(f"{msg} - Aposta {count}: "))
        if min <= num <= max:
            return num
        else:
            print(f"Valor inválido, digite um número entre [{min}:{max}]")

def appendList(size, msg):
    numbers = []
    count = 1
    if size == 5:
        max = 50
    else:
        max = 12
    while True:
        if len(numbers) == size:
            return numbers
        num = getValue(count,1,max, msg)
        if num not in numbers:
            numbers.append(num)
            count+=1
        else:
            print(f"Já digitou esse valor, escolha outro número [1:{max}]")

"""
Função que vai comparar o input com os valores gerados aleatóriamente
Recebe a lista com numeros aleatórios e os inputs do usuário
Retorna um contador com o número de acertos (valores iguais em ambas as listas)
"""
# Comparar as listas de números e contabilizar acertos
def compareLists(randonList, userList):
    count = 0
    for num in userList:
        if num in randonList:
            count+=1
    return count

# Premiação dos Jogos Santa Casa
"""
A função da premiação vai imprimir o resultado do sorteio e o jogo realizado
Com um match case com a quantidade de acertos de números e estrelas vai realizar a premiação.
"""
def prizeEuroMilhoes():
    # variaveis locais para receber a contagem de acertos:
    numCount = compareLists(winningNumbers, betNumbers)
    starCount = compareLists(winningStars, betStars)

    # mostrar os valores das listas:
    print(f"\nNúmeros Sorteados: Números {sorted(winningNumbers)}, Estrelas {sorted(winningStars)}")
    print(f"Números Jogados:   Números {sorted(betNumbers)}, Estrelas {sorted(betStars)}\n")

    # atribuir a premiação
    match numCount,starCount:
        case 5,2:
            print(f"""
                  JACKPOT!!
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO MÁXIMO DE €1.000.000
                """)
        case 5,1:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €250.000
                """)
        case 5,0:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €18.000
                """)
        case 4,2:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €1.000
                """)
        case 4,1:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €100
                """)
        case 3,2:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €40
                """)
        case 4,0:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €35
                """)
        case 2,2:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €10
                """)
        case 3,1:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €9
                """)
        case 3,0:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €8
                """)
        case 1,2:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €5
                """)
        case 2,1:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €4
                """)
        case 2,0:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount} 
                  PARABÉNS, VOCÊ GANHOU O PRÊMIO DE €3
                """) 
        case _,_:
            print(f"""
                  Acertos: 
                  Números: {numCount} Estrelas: {starCount}
                  VOCÊ NÃO FOI PREMIADO. OBRIGADA PELA PARTICIPAÇÃO!"
                  """)

# globals 
winningNumbers = [] # Lista de números sorteados
winningStars = []   # Lista de estrelas sorteadas
betNumbers = []     # Lista dos números do jogador
betStars = []       # Lista das estrelas do jogador

# call functions
winningNumbers = getRandom(5,1,50)
winningStars = getRandom(2,1,12)
betNumbers = appendList(5, "NÚMEROS")
betStars = appendList(2, "ESRTELAS")
prizeEuroMilhoes()