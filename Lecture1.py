go = True
print('Введіть 0 для виходу')
while go:
    answ = int(input("Введіть номер задачі: "))
    if (answ == 0):
        go = False
    match answ:
        case 1:
            n = int(input("Введіть кількість школярів: "))
            k = int(input("Введіть кількість яблук: "))
            apples_per_pupil = k // n
            left = k % n
            print("Кожному школяру дістанеться: ", apples_per_pupil)
            print("У кошику залишиться: ", left)

        case 2:
            sleep = int(input("Кількість хвилин для сну: "))
            hours = int(input("Години: "))
            minutes = int(input("Хвилини: "))
            hours += sleep//60
            minutes += sleep % 60
            print("Година: ", hours)
            print("Хвилина: ", minutes)

        case 3:
            a = int(input("Клас а: "))
            b = int(input("Клас б: "))
            c = int(input("Клас в: "))
            sum = round(a/2)+round(b/2)+round(c/2)
            print("Всього парт потрібно: ", sum)

        case 4:
            a = int(input("Введіть перше число: "))
            b = int(input("Введіть друге число: "))
            c = int(input("Введіть третє число: "))

            max_num = (a + b + abs(a - b)) // 2
            max_num = (max_num + c + abs(max_num - c)) // 2
            min_num = (a + b - abs(a - b)) // 2
            min_num = (min_num + c - abs(min_num - c)) // 2
            remaining_num = a + b + c - max_num - min_num

            print("Максимальне число: ", max_num)
            print("Мінімальне число: ", min_num)
            print("Залишок: ", remaining_num)
        case 5:
            a = int(input("a: "))
            b = int(input("b: "))
            l = int(input("l: "))
            N = int(input("N: "))
            length = (N - 1) * a + N * b + 2 * l
            print("Довжина: ", length)
