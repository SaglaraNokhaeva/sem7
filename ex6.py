# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from string import ascii_letters
from random import randint, sample, randbytes
import os


def makefile(extention, smallest=6, largest=30, min_bytes=256, max_bytes=4096, count=42):
    names = set()
    while len(names) < count:
        names.add(''.join(sample(ascii_letters, randint(smallest, largest))))

    for name in names:
        with open(f'{name}.{extention}', 'wb') as file:
            temp = randbytes(randint(min_bytes, max_bytes))
            file.write(temp)
            print(len(temp))


def makefiles(**extentions):
    for extention, count in extentions.items():
        makefile(extention=extention, count=count)


def makefile_topath(path, extention):
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    makefile(extention)

makefile_topath('test', 'txt')
