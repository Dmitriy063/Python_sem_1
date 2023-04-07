# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(0, 1000)
print("Программай отгада число! Загадывает в диапазоне от 0 до 1000")
k = 0


def find_number(answer):
    if answer > num:
        print("Загаданное число меньше")
    elif answer < num:
        print("Загаданное число больше")
    elif answer == num:
        print("Ура, вы угадали! Это было число: ", num)


while True:
    num_answer = int(input("Введите число: "))
    find_number(num_answer)
    k += 1
    if k > 10:
        print("Слишком много попыток, ты проиграл...")
        break
    elif num == num_answer:
        break
