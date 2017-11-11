#!/usr/bin/env python3
import random


def shuffle_letters(input_string):
    input_string_list = list(input_string)
    random.shuffle(input_string_list)
    return print(''.join(input_string_list))


name = input('Привет, как тебя зовут?:')
print('Вот это да, я тоже ' + name + '.')
while True:
    input_str = input('Введи слово или "q", чтобы выйти: ')
    if input_str == 'q':
        print('Чё, бля, ' + name + ', наигра(лся/лась)? Ну, пока, заходи ещё).')
        break
    else:
        shuffle_letters(input_str)
