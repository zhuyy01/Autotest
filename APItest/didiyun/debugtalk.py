import random
import time

import os


def ENV(keyname):
    values = os.environ.get(keyname,"")
    return values

def sleep(n_secs):
    print("睡眠开始了,预计睡眠%i"%n_secs)
    time.sleep(n_secs)


def rand():
    str="12345678qwerty"
    a=random.choice(str)
    b=random.choice(str)
    c=random.choice(str)
    d=random.choice(str)
    e=a+b+c+d
    print(e)
    return e

if __name__ == '__main__':
    rand()

