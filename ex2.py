# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import string
import random

vowel = 'аеёиоуэюя'
consonant = 'бвгджзйкдмнлнпрстфхцчшщъь'
# print(string.ascii_lowercase)

a = random.randint(4, 7)
v = random.randint(1, a-2)
s = random.sample(vowel, a) + random.sample(consonant, a-v)


print(x)
print(y)
print(s)
