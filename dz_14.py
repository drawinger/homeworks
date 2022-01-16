# ---------------------------------- Задание 1---------------------------------------
# В приложении к заданию дан модуль testing_example.py В модуле вы найдете функцию calculate_credit для расчета
# месячного платежа по кредиту.
# Напишите для этой функции набор тестов используя модуль unittest.
# Ваши тесты должны учитывать как нормальный вариант работы функции, так и как можно большее число ошибочных
# вызовов этой функции.
# Доработайте функцию calculate_credit таким образом, чтобы она не ломалась при передаче ей ошибочных входных
# параметров, а возвращала какое-нибудь осмысленное значение (например, Null, -1 или строку с сообщением об
# ошибке).

import unittest
from testing_example import *

# основной контейнер тестов
class MyCreditTest(unittest.TestCase):
    
    def test_normal(self):
        self.assertEqual(calculate_credit_2(1, 1, 1), 1)

    # тест-кейс для тестирования вызова строки, вместо одного из аргументов функции
    def test_string(self):
        self.assertTrue(calculate_credit_2(1, 1, '1') == 'Строка вместо числа!')
    
    # тест-кейс для тестирования вызова строки, вместо одного из аргументов функции
    def test_list(self):
        self.assertTrue(calculate_credit_2([1], 1, 1) == 'Список вместо числа!')
    
    # тест-кейс для тестирования вызова словаря, вместо одного из аргументов функции
    def test_dict(self):
        self.assertTrue(calculate_credit_2({'1':1}, 1, 1) == 'Словарь вместо числа!')
       
    # тест-кейс для тестирования отсутствия одного из аргументов функции
    def test_empty_arg(self):
        self.assertIs(calculate_credit_2(1, 1), None)
        
    # тест-кейс для тестирования отсутствия одного из аргументов функции
    def test_zero_div(self):
        self.assertIs(calculate_credit_2(1, 0, 1), None)

# ---------------------------------- Задание 2---------------------------------------
# В приложении к заданию дан модуль testing_example.py В модуле вы найдете класс Calculator, у которого есть
# методы для выполнения простейших математических операций.
# С помощью модулей unittest или pytest напишите тесты для методов этого класса.
# Используйте фикстуры для того, чтобы создать объект класса Calculator, который вы будете использовать для
# тестирования

class MyCalculatorTest(unittest.TestCase):

    # подготовка окружения для теста
    def setUp(self): # fixture
        self.calc_res = Calculator

    # функци тестов
    def test_sum_normal(self):
        self.assertEqual( self.calc_res.sum(1,2), 3)
        
    def test_mult_normal(self):
        self.assertEqual( self.calc_res.mult(1,2), 2)
        
    def test_mult_empty_arg(self):
        self.assertEqual( self.calc_res.mult(1,), 2)

    # врать не буду, так и не придумал что можно придумать для уборщика в данном конкретном примере
    def tearDown(self): pass

# python dz_14.py -v
if __name__ == '__main__': unittest.main()