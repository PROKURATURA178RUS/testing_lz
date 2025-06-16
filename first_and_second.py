import math

def test_uravnenie(a, b, c, d):
    try:
        result = math.sqrt(a - b) / (c - d)
        return result
    except ZeroDivisionError:
        return "Ошибка: Деление на ноль."
    except ValueError:
        return "Ошибка: Невозможно вычислить логарифм или корень из отрицательного числа."
    except Exception as e:
        return f"Ошибка: {e}"
    
    
"""
1)Деление на ноль
test = test_uravnenie(5,3,4,4)
print(test)

2)Отрицательное число под корнем
test1 = test_uravnenie(2,3,4,4)
print(test1)

3)Два положительных числа
test2 = test_uravnenie(5,3,5,4)
print(test2)

4)Отрицательное число в знаменателе
test3 = test_uravnenie(5,3,3,4)
print(test3)
"""
