from random import *

print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    if not num.isdigit():
        return False
    try:
        int(num)
        if int(num) > 100:
            return False
        else:
            return True
    except TypeError:
        print(TypeError)
        return False



var = randint(1, 100)
count = 1
print('Введите число')
while True:
    num = input()
    count = 1
    while not is_valid(num):
        print('А может быть все-таки введем целое число от 1 до 100?')
        num = input()
        count += 1
    num = int(num)
    if num < var:

        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num > var:

        print('Ваше число больше загаданного, попробуйте еще разок')
    elif num == var:

        print('Вы угадали, поздравляем!\n')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...', count)
        var = randint(1, 100)
