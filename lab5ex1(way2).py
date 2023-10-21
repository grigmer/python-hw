import turtle
turtle.shape("turtle")
turtle.color("blue")


#Я пронумеровал все точки в узлах цифры в почтовом индексе, и функция f ставит в соответствие каждой 
#цифре массив точек (взятых в нужном порядке), при соединении которых получится эта цифра.

def f(n):
    if n == 0:
        return [1, 2, 4, 5, 1]
    elif n == 1:
        return [6, 2, 4]
    elif n == 2:
        return [1, 2, 3, 5, 4]
    elif n == 3:
        return [1, 2, 6, 3, 5]
    elif n == 4:
        return [1, 6, 3, 2, 4]
    elif n == 5:
        return [2, 1, 6, 3, 4, 5]
    elif n == 6:
        return [2, 6, 5, 4, 3, 6]
    elif n == 7:
        return [1, 2, 6, 5]
    elif n == 8:
        return [1, 2, 4, 5, 1, 6, 3]
    elif n == 9:
        return [3, 2, 1, 6, 3, 5]


#Функция h принимает на вход координаты верхнего левого угла цифры, которую мы рисуем, и номер точки
#и возвращает координаты этой точки в виде массива из 2 элементов.

def h(x, y, a):
    if a == 1:
        return [x, y]
    elif a == 2:
        return [x + 50, y]
    elif a == 3:
        return [x + 50, y - 50]
    elif a == 4:
        return [x + 50, y - 100]
    elif a == 5:
        return [x, y - 100]
    elif a == 6:
        return [x, y - 50]
    
#Функция g принимает на вход номер цифры в индексе и саму эту цифру и рисует ее, опираясь на функции f и h.

def g(n, c):
    l = f(c)
    turtle.penup()
    turtle.goto(h(-210 + 70 * n, 100, l[0]))
    turtle.pendown()
    for i in l[1:]:
        turtle.goto(h(-210 + 70 * n, 100, i))



k = [int(j) for j in input()]      #Массив из цифр вводимого индекса.

#Проверяем, из 6-ти ли цифр состоит введенный индекс, и если да, то с помощью цикла и введенных выше функций рисуем его.
#Если нет, то печатаем "Не индекс!...".

if len(k) == 6:
    for i in range(len(k)):
        g(i, k[i])
else:
    print("Не индекс! Должно быть 6 цифр, а не " + str(len(k)) + "!")