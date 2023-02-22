# Крестики-нолики
pole = [['-']*3 for _ in range(3)]
def igra(k):
    print('  0 1 2 ')
    for i in range(len(pole)):
        print(str(i), *pole[i])
igra(pole)

def users_input(f):
    while True:
        place = input("Введите координаты: ").split()
        if len(place) != 2:
            print("Введите только две координаты: ")
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числа!: ")
            continue
        x,y = map(int, place)
        if not(0 <= x < 3 and 0 <= y < 3):
            print("Числа должны быть от 0 до 3!")
            continue
        if f[x][y] != "-":
            print("Ячейка уже использовалась!")
            continue
        break
    return x,y
users_input(pole)

def victory(f, znak):
    def chek_line(a1,a2,a3, znak):
        if a1 == znak and a2 == znak and a3 == znak:
            return True
    for n in range (3):
        if chek_line(f[n][0], f[n][1], f[n][2], znak) or \
                chek_line(f[0][n], f[1][n], f[2][n], znak) or \
                chek_line(f[0][0], f[1][1], f[2][2], znak) or \
                chek_line(f[2][0], f[1][1], f[0][2], znak):
            return True
    return False

count = 0
while True:
    if count % 2 == 0:
        znak = 'x'
    else:
        znak = '0'
    igra(pole)
    x,y = users_input(pole)
    pole[x][y] = znak
    if count == 9:
        print("Ничья")
    if victory(pole, znak):
        igra(pole)
        print(f'Выиграл {znak}!!!')
        break
    count +=1
