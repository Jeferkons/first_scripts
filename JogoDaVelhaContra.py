import random

def jogada (numero,i):
    if (posicao[numero] == " "):
        posicao[numero] = "X"
        if verificar() == "true":
                tela()
                print("Jogador ganhou")
                return "acabou"


        computador = random.randint(0,8)
        while (computador == numero or posicao[computador] != " " ):
            computador = random.randint(0,8)
            if (posicao[0] != " " and posicao[1] != " " and
            posicao[2] != " " and posicao[3] != " " and
            posicao[4] != " " and posicao[5] != " " and
            posicao[6] != " " and posicao[7] != " " and
            posicao[8] != " "):
                print("Deu velha...")
                return "acabou"


        posicao[computador] = "O"
        if verificar() == "true":
                tela()
                print("Computador ganhou")
                return "acabou"


def tela ():
    print ("| %s | %s | %s |" % (posicao[0], posicao[1], posicao[2]))
    print ("|---+---+---|")
    print ("| %s | %s | %s |" % (posicao[3], posicao[4], posicao[5]))
    print ("|---+---+---|")
    print ("| %s | %s | %s |" % (posicao[6], posicao[7], posicao[8]))

def verificar():
    if (posicao[0] == posicao[1] == posicao[2] != " "):
        return "true"
    elif (posicao[3] == posicao[4] == posicao[5] != " "):
        return "true"
    elif (posicao[6] == posicao[7] == posicao[8] != " "):
        return "true"
    elif (posicao[0] == posicao[3] == posicao[6] != " "):
        return "true"
    elif (posicao[1] == posicao[4] == posicao[7] != " "):
        return "true"
    elif (posicao[2] == posicao[5] == posicao[8] != " "):
        return "true"
    elif (posicao[0] == posicao[4] == posicao[8] != " "):
        return "true"
    elif (posicao[2] == posicao[4] == posicao[6] != " "):
        return "true"



posicao = [" "," "," "," "," "," "," "," "," "]

i = 0

print ("| 0 | 1 | 2 |")
print ("|---+---+---|")
print ("| 3 | 4 | 5 |")
print ("|---+---+---|")
print ("| 6 | 7 | 8 |")

while i < 6:

    print("Jogador, escolha uma posicao:")
    numero = int(input())
    if (jogada(numero,i) == "acabou"):
        break
    tela()

    i += 1
