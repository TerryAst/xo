turn = 'x'
has_winner = False
schetchik = 1
xo = [[' ', 0, 1, 2], [0, '-', '-', '-'], [1, '-', '-', '-'], [2, '-', '-', '-']]
def vivod():
    for i in xo:
        for j in i:
            print(j, end='\t')
        print('\n')
def proverka():
    global has_winner
    if xo[1][1] == turn and xo[1][2] == turn and xo[1][3] == turn:
        has_winner = True
    elif xo[2][1] == turn and xo[2][2] == turn and xo[2][3] == turn:
        has_winner = True
    elif xo[3][1] == turn and xo[3][2] == turn and xo[3][3] == turn:
        has_winner = True
    elif xo[1][1] == turn and xo[2][1] == turn and xo[3][1] == turn:
        has_winner = True
    elif xo[1][2] == turn and xo[2][2] == turn and xo[3][2] == turn:
         has_winner = True
    elif xo[1][3] == turn and xo[2][3] == turn and xo[3][3] == turn:
        has_winner = True
    elif xo[1][1] == turn and xo[2][2] == turn and xo[3][3] == turn:
        has_winner = True
    elif xo[3][1] == turn and xo[2][2] == turn and xo[1][3] == turn:
        has_winner = True
    elif schetchik == 9:
        has_winner = True
        print('Ничья')
    if has_winner == True and schetchik != 9:
        print('Победил - ', turn)

vivod()

while has_winner == False:
    print('Сейчас ходит - ', turn)
    stlbec = int(input('Введити столбец куда хотите поставить символ: '))
    stroka = int(input('Введити строку куда хотите поставить символ: '))
    if 0 <= stroka < 3 and 0 <= stlbec < 3:
        if xo[stroka +1][stlbec +1] != '-':
            print('Строка занята')
        else:
            xo[stroka + 1][stlbec + 1] = turn
            vivod()
            proverka()
            schetchik += 1
            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'
    else:
        print('Вводите значения 0-2')





