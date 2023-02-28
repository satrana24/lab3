from random import *
def first():
    n = int(input('сколько хотите ввести слов? '))
    s = []

    for i in range(1, n + 1):
        word = str(input())
        s.append(word)
    print(*s)

def second():
    s = []
    count = 0

    while count != 1:
        word = str(input())
        s.append(word)
        if word == 'stop':
            count += 1
    print(*s[:-1])

def third():
    count = 0
    while count != 1:
        word = str(input())
        if word.lower() == 'stop':
            break
        if 'ф' in word.lower():
            print('Это редкое слово')
        else:
            print('Это не редкое слово')

def fourth():
    count = 0
    while count != 3:
        a = randint(1, 10)
        b = randint(1, 100)
        print(a, '+', b, '= ')
        c = int(input())
        if c == a + b:
            print('Правильно, количество ошибок: ', count)
        elif c != a + b:
            count += 1
            print('Неправильно, количество ошибок: ', count)
