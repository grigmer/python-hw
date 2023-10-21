def flexible_get(a, b):
    c = int(b + 0.5)    #Округляем флотовый индекс до ближайшего целого
    try:
        return a[c]
    except IndexError:
        return None


#Вызываем функцию для вводимых с клавиатуры элементов массива (в строку, через пробел) и индекса (в следующей строчке)
#и печатаем результат ее работы.

print(flexible_get([i for i in input().split()], float(input())))