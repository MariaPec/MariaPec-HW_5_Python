from random import randint

desk = ["_" for i in range(3)], ["_" for i in range(3)], ["_" for i in range(3)]

win = False
move = 0
turn = 1

def PrintDesk(desk):
    for i in range(len(desk)):
        for j in range(len(desk[i])):
            print("|" + desk[i][j] + "|", end='')
        print()

def FillRandom(desk, sign):
    i = (randint(0,3)) - 1
    j = (randint(0,3)) - 1
    if desk[i][j] == "_":
        desk[i][j] = sign
    else:
        FillRandom(desk, sign)
        return

def Fill(desk, sign):
    i = (int(input("введите строку: ")) - 1)
    j = (int(input("введите столбец: ")) - 1)
    
    if (i > 2 or i < 0) or (j > 2 or j < 0):
        print("некорректный ввод. вводите значения от 1 до 3")
        Fill(desk, sign)
    elif desk[i][j] == "_":
        desk[i][j] = sign
    else: 
        print("поле занято. введите еще раз")
        Fill(desk, sign)
    return

def CheckForWin(desk):
    for i in range(len(desk)):
        if (desk[i][0] == desk[i][1] == desk[i][2] == "0") or (desk[i][0] == desk[i][1] == desk[i][2] == "X"):
            return True
    for j in range(len(desk)):
        if (desk[0][j] == desk[1][j] == desk[2][j] == "0") or (desk[0][j] == desk[1][j] == desk[2][j] == "X"):
            return True
    if (desk[0][0] == desk [1][1] == desk [2][2] == "0") or (desk[2][0] == desk [1][1] == desk [0][2] == "0"):
        return True
    if (desk[0][0] == desk [1][1] == desk [2][2] == "X") or (desk[2][0] == desk [1][1] == desk [0][2] == "X"):
        return True

PrintDesk(desk)

if move != 9:
    while win != True:
        if turn == 1:
            Fill(desk, "X")
            win = CheckForWin(desk)
            turn = 2
            move += 1
        else:
            print()
            FillRandom(desk, "0")
            win = CheckForWin(desk)
            turn = 1
            move += 1
            print(win)
        PrintDesk(desk)

if win == True and move % 2 == 0:
    print("Победил игрок 2")
elif win == True and move % 2 == 1:
    print("Победил игрок 1")
else:
    print("никто не выиграл")
