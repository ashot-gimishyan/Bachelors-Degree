from random import *

errors = [
    (ValueError, 'ValueError'),
    (TypeError, 'TypeError'),
    (FileExistsError, 'FileExistsError'),
    (EOFError, 'EOFError'),
    (FileNotFoundError, 'FileNotFoundError'),
    (KeyError, 'KeyError'),
    (ArithmeticError, 'ArithmeticError'),
    (AssertionError, 'AssertionError'),
    (AttributeError, 'AttributeError'),
    (BlockingIOError, 'BlockingIOError'),
    (BrokenPipeError, 'BrokenPipeError'),
    (BufferError, 'BufferError'),
    (ChildProcessError, 'ChildProcessError'),
    (ConnectionAbortedError, 'ConnectionAbortedError'),
    (FloatingPointError, 'FloatingPointError'),
    (IndexError, 'IndexError'),
    (ModuleNotFoundError, 'ModuleNotFoundError'),
    (NameError, 'NameError'),
    (ZeroDivisionError, 'ZeroDivisionError'),
    (SystemError, 'SystemError'),
]

summa = 0
with open('nums.txt', 'a') as file:
    while summa <= 777:
        number = int(input("Введите число: "))
        summa += number
        if number == 13:
            try:
                error, message = choice(errors)
                raise error(message)
            except error as e:
                print(e)
                break
        print(number, file=file)
