import math


def area(r):
    ''' Принимает радиус окружности и находит ее площадь
            area(3)
            area(5)
            area(10)
    
            >> 28.27 78.54 314.16'''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает радиус окружности и находит ее периметр
            perimeter(3)
            perimeter(5)
            perimeter(10)

            >> 18.84 31.41 62.83'''
    return 2 * math.pi * r

