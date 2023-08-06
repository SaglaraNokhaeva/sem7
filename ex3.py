# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.


names_size = len(list(1 for _ in open('names.txt')))
numbers_size = len(list(1 for _ in open('numbers.txt')))
count = max(names_size, numbers_size)
with open('names.txt', 'r', encoding='utf-8') as names, \
        open('numbers.txt', 'r') as numbers, \
        open('result.txt', 'r') as res:
    names_str = names.readline()
    while count > 0:
        # print(type(names_str))
        numbers_str = numbers.readline()
        # print(numbers_str)
        number_one, number_two = numbers_str.split('|')
        prod = int(number_one) * float(number_two)
        if prod < 0:
            res.write(f'{names_str.lower()} {abs(prod)}\n')
        else:
            res.write(f'{names_str.upper()} {round(prod)}\n')
    count -=1
