<<<<<<< HEAD
from math import *


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return    
    root=0
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {CalculateSquareRoot(your_number)}')
print(message)
calc(25.5)
=======
def is_rhomb(a_size: float, b_size: float) -> bool:
    """Проверяет, является ли параллелограмм ромбом."""
    # Вернёт True или False в зависимости от истинности выражения.
    return a_size == b_size  
 

# Функция print_hi() ожидает строковый аргумент, 
# значение этого аргумента по умолчанию — 'stranger'.
# Функция ничего не возвращает, и для неё тип возвращаемых данных — None.
def print_hi(name: str = 'stranger') -> None:
    print('Hi,' + name + '!')

# Можно напечатать типы данных функций.
print(is_rhomb.__annotations__)
    {'a_size': <class 'float'>, 'b_size': <class 'float'>, 'return': <class 'bool'>}

print(print_hi.__annotations__)
    {'name': <class 'str'>, 'return': <class 'None'>} 
>>>>>>> a459ef30904b699cf49192b2ea5bbfc2b67d1d46
