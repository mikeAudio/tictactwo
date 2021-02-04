x = 0
again = True
again1 = False
again2 = False
player1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player1win = False
player2win = False
line = "- - -"


def eingabe1():
    if player1[x - 1] == 1 or player2[x - 1] == 1:
        print("Bereits belegt.")
        again1 = True
    else:
        player1[x - 1] = 1
        again1 = False


def eingabe2():
    if player1[x - 1] == 1 or player2[x - 1] == 1:
        print("Bereits belegt.")
        again2 = True
    else:
        player2[x - 1] = 1
        again2 = False


def logik1():
    for y in range(3):
        if player1[y] == 1 and player1[y + 3] == 1 and player1[y + 6] == 1:
            player1win = True
    for z in range(3):
        if player1[z] == 1 and player1[z + 1] == 1 and player1[z + 2] == 1:
            player1win = True
        z = z + 2
    if player1[0] == 1 and player1[5] == 1 and player1[9] == 1:
        player1win = True
    if player1[7] == 1 and player1[5] == 1 and player1[4] == 1:
        player1win = True


def logik2():
    for y in range(3):
        if player2[y] == 1 and player2[y + 3] == 1 and player2[y + 6] == 1:
            player2win = True
    for z in range(3):
        if player2[z] == 1 and player2[z + 1] == 1 and player2[z + 2] == 1:
            player2win = True
        z = z + 2
    if player2[0] == 1 and player2[5] == 1 and player2[9] == 1:
        player2win = True
    if player2[7] == 1 and player2[5] == 1 and player2[4] == 1:
        player2win = True


def grafik():
    print(" ")
    i = 0
    while i <= 9:
        for z in range(3):
            if player1[z + i] == 1:
                line[z + z] = "X"
            if player2[z + i] == 1:
                line[z + z] = "O"
        print(line)
        i = i + 3
    print(" ")


while again == True:
    if again2 == False or player1win == False:
        x = input("Spieler 1 ist an der Reihe: ")
        eingabe1()
        logik1()
        grafik()

    if again1 == False or player2win == False:
        print("Spieler 2 ist an der Reihe.")
        input(x)
        eingabe2()
        logik2()
        grafik()

    if player1win:
        print("Spieler 1 hat gewonnen!")
        again = False
    elif player2win:
        print("Spieler 2 hat gewonnen!")
        again = False
