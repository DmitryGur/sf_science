## Creating a playing field
board =[" ", 0, 1, 2, 0, "-", "-", "-", 1, "-", "-", "-",  2, "-", "-", "-"]

#№ The function of displaying the playing field in the console
def dis_board():
    for i in range(4):
        print(*board[i*4:(i+1)*4]) 
        
## The function of filling the playing field during the game
def control(mark,  x1, x2):
    if board[(x2+1)*4+x1+1] == "-":
        board[(x2+1)*4+x1+1] = mark
        if board[5:8] == [mark, mark, mark] or board[9:12] == [mark, mark, mark] or board[13:] == [mark, mark, mark] or (board[5] == mark and board[9] == mark and board[13] == mark) or (board[6] == mark and board[10] == mark and board[14] == mark) or (board[7] == mark and board[11] == mark and board[-1] == mark) or (board[5] == mark and board[10] == mark and board[-1] == mark) or (board[7] == mark and board[10] == mark and board[13] == mark):
            print(dis_board())
            return  control 
    else:
        print("Клетка занята")
        return False 
## The main function of the game is to check the correctness of the input data.                
def game():
    print(f"НАЧАЛО ИГРЫ!\nВведите номер ячейки.\nПервая цифра - номер столбца.\nВтрая цифра - номер строки")
    counter = 0
    win = False
    while not win:
        dis_board()
        if counter % 2 == 0:
            mark = 'X'
            player = 1
        else:
            mark = 'O'
            player = 2
        print(f"Ход игрока № {player}")
        t1 = False
        while not t1:
            x1 = input("Введите номер столбца: ")
            if x1 == '0' or x1 == '1' or x1 == '2':
                t1 = True
                x1 = int(x1)
            else:
                print("Введено некорректное значение")
        t2 = False
        while not t2:
            x2 = input("Введите номер строки: ")
            if x2 == '0' or x2 == '1' or x2 == '2':
                t2 = True
                x2 = int(x2)
            else:
                print("Введено некорректное значение")
        tmp = control(mark,  x1, x2)
        if tmp != False:
            counter += 1
        if tmp:
            print(f"ПОБЕДИЛ {player} ИГРОК")
            win = True
            break
        if counter == 9:
            print("НИЧЬЯ!")
            break
    return "КОНЕЦ ИГРЫ!"

print(game())