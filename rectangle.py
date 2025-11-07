def area(a, b):
    '''Принимает числа a и b, возвращает произведение a на b'''
    '''Проверяем, являются ли a,b (стороны) числами '''
    if not (isinstance(a, (int,float)) and isinstance(b, (int,float))):
        raise TypeError("Аргументы должны быть числами")

    '''Проверяем, являются ли a,b (стороны) неотрицательными числами '''
    if a<0 or b<0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def perimetr(a, b):
    '''Принимает числа a и b, возвращает удвоенную сумму a на b'''
    '''Проверяем, являются ли a,b (стороны) числами '''
    if not (isinstance(a, (int,float)) and isinstance(b, (int,float))):
        raise TypeError("Аргументы должны быть числами")

    '''Проверяем, являются ли a,b (стороны) неотрицательными числами '''
    if a<0 or b<0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)