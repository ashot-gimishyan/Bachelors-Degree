# Метод Парабол
# Язык Python (версия 3.9.7)

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    def foo(x_i):
        return x_i ** 2 
    if isinstance(x,float) or isinstance(x,int):
        return foo(x)
    
    return [foo(i) for i in x]

# Функция, находящая точку минимума параболы, проходящей через 3 определенные точки аппроксимируемой функции:
def XMin ( x1, x2, x3, func):
    X = x2 - 0.5 * ( ((x2 - x1)**2) * (func (x2) - func ( x3 ))
                    - ((x2 - x3)**2) * (func (x2) - func ( x1 ))) \
    / ( (x2 - x1) * (func (x2) - func ( x3 )) - (x2 - x3) * (func (x2) - func ( x1 )))
    return X

# Начальные условия
a = -1 ; c = 4
b = ( a + c ) / 2
Eps = 10 ** (-3)

minimum = XMin (a, b, c, f)

# Сама функция поиска
while abs(minimum-b )>Eps:
    # сортирует точки по возрастанию (для унимодальной на отрезке функции правомочно)
    dots = sorted ( [ a, b, c, minimum] )
    Values = f (dots)
    FMax = max ( Values)
    # ищет индекс точки, в которой функция принимает наибольшее из четырех значение
    for i in range ( len(Values) ):
        if Values[i] == FMax:
            break
    # убирает точку с этим индексом
    dots.remove ( dots [ i ] )             
    a , b , c = dots   
    minimum = XMin (a, b, c, f)
    
print (minimum)
