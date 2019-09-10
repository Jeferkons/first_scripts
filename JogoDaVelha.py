def jogada (numero,i):
    if (i % 2 == 1 and (posicao[numero] == " ")):
        posicao[numero] = "X"
    elif (i % 2 == 0 and (posicao[numero] == " ")):
        posicao[numero] = "O"
    else:
        print("Errou, jogue de novo")
        return "true"


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

while i < 9:

    print("Jogador %s, escolha uma posicao:" %(i % 2 + 1))
    numero = int(input())
    if (jogada(numero,i) == "true"):
        i = i -1
    tela()
    if verificar() == "true":
        print("Voce ganhou jogador %s" % (i % 2 + 1))
        break
    if i == 8 :
        print("Deu velha...")
        break
    i += 1
