# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Введите натуральное число не более 100 тысяч: '))
if 2 <= num <= 100000:
    for i in range(2, num + 1):
        if num % i == 0 and i != num:
            print('Число составное.')
            break
        elif i == num:
            print('Число простое.')
elif num == 1:
    print('Число не является ни простым, ни составным', 
          '(именно этим оно отличается от остальных натуральных чисел).')
else:
    print('Введенное число не соответствует условию.')     