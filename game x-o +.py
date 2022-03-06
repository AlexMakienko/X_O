def draw_field(f):
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])


def user_input(f):
    while True:
        place = input("Введите координаты : ").split()
        if len(place) != 2:
            print("Требуется ввести две координаты через пробел")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Требуется ввести два числа через пробел")
            continue
        x, y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Диапазон ввода чисел от 0 до 2 через пробел")
            continue
        if f[x][y] != "-":
            print("Клетка занята. Повторите ввод")
            continue
        break
    return x, y


def check_win(f, user):
    def check_line(a, b, c, user):
        if a == user and b == user and c == user:
            return True

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], user) or \
                check_line(f[0][n], f[1][n], f[2][n], user) or \
                check_line(f[0][0], f[1][1], f[2][2], user) or \
                check_line(f[2][0], f[1][1], f[0][2], user):
            return True


print("*" * 3, " Игра Крестики-нолики для двух игроков ", "*" * 3)
field = [['-'] * 3 for _ in range(3)]
counter = 0
win = False
while not win:
    draw_field(field)
    x, y = user_input(field)
    if counter % 2 == 0:
        user = "X"
    else:
        user = "O"
    field[x][y] = user
    counter += 1
    if counter > 4:
        winer = check_win(field, user)
        if winer:
            draw_field(field)
            print(user, "выиграл!")
            win = True
            break
    if counter == 9:
        draw_field(field)
        print("Ничья!")
        break
