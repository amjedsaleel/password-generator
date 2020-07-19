import string
from random import randint
import random


upper_alphabet = string.ascii_uppercase
lower_alphabet = string.ascii_lowercase
special_character = ['!', '@', '$', '&', '*', ':', ';', '.', '?']

pass_list = []


def generate(password_length):
    for i in range(password_length):
        comp_1 = random.choice(lower_alphabet)
        comp_2 = random.choice(upper_alphabet)
        comp_3 = randint(0, 9)
        comp_4 = random.choice(special_character)
        value = str(random.choice([comp_1, comp_2, comp_3, comp_4]))
        # print(value, end='')
        pass_list.append(value)
    password = ''.join([str(elem) for elem in pass_list])
    return password

