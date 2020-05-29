import random
import string
import numpy as np


def random_char(y):
    return ''.join((random.choice(string.ascii_letters)).upper() for x in range(y))


def random_number(y):
    return ''.join([str(i) for i in np.random.randint(low=0, high=10, size=y, dtype=np.uint8)])


def genre():
    return 'f' if np.random.randint(low=0, high=2) == 0 else 'm'


def random_date():
    '''
    generates random date of 'YYMMDD' format.
    :return: str
    '''
    yy = str(np.random.randint(low=1980, high=2020))[0:2]
    m = str(np.random.randint(low=1, high=12))
    mm = '0' + m if len(m) == 1 else m
    dd = str(np.random.randint(low=10, high=28))
    return yy+mm+dd