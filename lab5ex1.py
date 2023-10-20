import turtle
turtle.shape("turtle")
turtle.color("blue")


#Я пронумеровал все "палочки", из которых могут состоять цифры в почтовом индексе, и функция f ставит в соответствие каждой 
# цифре множество номеров "палочек", которые нужно закрасить, чтобы получить её.

def f(n):
    if n == 0:
        return set([1, 2, 3, 4, 5, 6])
    elif n == 1:
        return set([8, 2, 3])
    elif n == 2:
        return set([1, 2, 4, 9])
    elif n == 3:
        return set([1, 8, 7, 9])
    elif n == 4:
        return set([7, 2, 3, 6])
    elif n == 5:
        return set([1, 4, 3, 6, 7])
    elif n == 6:
        return set([8, 4, 3, 5, 7])
    elif n == 7:
        return set([1, 8, 5])
    elif n == 8:
        return set([1, 2, 3, 4, 5, 6, 7])
    elif n == 9:
        return set([1, 2, 6, 7, 9])


#Функция g принимает на вход координаты верхнего левого угла цифры, которую мы рисуем, и множество из функции f 
# и рисует нужные "палочки".


def g(x, y, s):
    if 1 in s:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(50)
    if 2 in s:
        turtle.penup()
        turtle.goto(x + 50, y)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
    if 3 in s:
        turtle.penup()
        turtle.goto(x + 50, y - 50)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
    if 4 in s:
        turtle.penup()
        turtle.goto(x, y - 100)
        turtle.pendown()
        turtle.forward(50)
    if 5 in s:
        turtle.penup()
        turtle.goto(x, y - 50)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
    if 6 in s:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
    if 7 in s:
        turtle.penup()
        turtle.goto(x, y - 50)
        turtle.pendown()
        turtle.forward(50)
    if 8 in s:
        turtle.penup()
        turtle.goto(x, y - 50)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(50*(2**0.5))
        turtle.right(45)
    if 9 in s:
        turtle.penup()
        turtle.goto(x, y - 100)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(50*(2**0.5))
        turtle.right(45)






k = [int(j) for j in input()]      #Массив из цифр вводимого индекса.

#Проверяем, из 6-ти ли цифр состоит введенный индекс, и если да, то с помощью цикла и введенных выше функций рисуем его.
#Если нет, то печатаем "Не индекс!...".

if len(k) == 6:
    for i in range(len(k)):
        g(-210 + 70 * i, 100, f(k[i]))
else:
    print("Не индекс! Должно быть 6 цифр, а не " + str(len(k)) + "!")
