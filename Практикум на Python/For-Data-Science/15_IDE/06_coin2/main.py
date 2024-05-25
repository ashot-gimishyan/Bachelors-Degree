def define(x,y,r):
    if (x ** 2 + y ** 2) ** 0.5 <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


x = float(input())
y = float(input())
r = float(input())

define(x,y,r)