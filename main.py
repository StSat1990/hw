#Типы данных, переменные и условные операторы
a = 30 #Задаем первую переменную a типа int
b = '3' #Задаем вторую переменную b типа str
c = a + int(b) #Задаем третью переменную, где складываем первые две переменные, переводя str в int
print(c) #Выводим результат

#Списки и кортежи
list = ['One'] #Создаем список
list.append('Two') #Добавляем в конец списка занчение
print(list) #Выводим результат
list.pop(0) #Удаляем из списка значение под нулевым индексом
print(list) #Выводим результат

#Циклы
squares = [] #Создаем пустой список
for value in range(1,11): #Создаем цикл, где в переменную value задаем все числа в диапозоне от 1 до 10
    square = value**2 #Создаем переменную square, которой пристаиваем все значения value в квадрате
    squares.append(square) #Передаем полученные значения в список square
print(squares) #Выводим результат

a = int(input('Введите число: ')) #Создаем переменную с вводом числового значения
while a <= 10:    #Создаем цикл пока a меньше или равно 10
    print(a)    #Выводим введенное значение
    a += 1      #Добавляем к введенному значению 1, пока значение не достигнет 10+1
while a > 10:    #Создаем цикл пока a больше 10
    print(a)    #Выводим введенное значение
    a -= 1      #Вычетаем с введенному значения 1, пока результат больше 10

#List comprehension
name = 'Sergey' #Создаем переменную name
n = [x for x in name] #Создаем переменную n и передаем ей все значения из x, которому предварительно передаем каждую букву и слова в переменной name
print(n) #Выводим результат

#Работа со словорями и сетами
favorite_language = {
    'Sergey': 'Python',
    'Nik': 'C',
    'Alex': 'Go',
} #Создаем словарь с ключами и значениями
language = favorite_language['Sergey'] #Создаем переменную language и передаем ей значение ключа Sergey из словаря
print(f'Любимый язык программирования у Сергея это {language}') #Выводим результат

#Функции
def create_list():  # Создаем функцию
    my_list = []    # Создаем пустой список
    my_list.append('Hello World!')  # Добавляем в список
    print(my_list)  #   Выводим результат
create_list()   #Вызываем функцию

#Лямбда
a = lambda x: x**2 # Создаем функцию с одним условием (присвоить переменной a значение x в квадрате)
print(a(9)) # Выводим результат, задав значение для x

#Классы и объекты
class Dog(): # Создаем класс
    def __init__(self, name, age): #Инициируем атрибы кличка и возраст
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} сидит') #Собака садится по команде

    def roll_over(self):
        print(f'{self.name} катается по полу') #Собака катается по полу по команде

dog = Dog('Jack', 5) # Создаем собаку присваивая ей кличку и возраст
dog.sit()
dog.roll_over() # Даем ей команды

#Наследование
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0 # Создаем простую модель автомобиля

    def get_decriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title() # Метод задания правильного имени автомобиля

    def read_odometer(self):
        print(f'Пробег автомобиля состявляет {self.odometr_reading}') # Чтение пробега

    def update_odometer(self, km):
        if km >= self.odometr_reading:
            self.odometr_reading = km
        else:
            print('Вы не можете скрутить пробег') #Обновление пробега, если он есть и запрет на скрутку

    def increment_odometer(self, km):
        self.odometr_reading += km # Добавление нового пробега

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #Создание дочернего класса, с наследованием у основного

my_tesla = ElectricCar('tesla', 'model s', 2019) # Создание модели
print(my_tesla.get_decriptive_name()) # Вывод правильного имени модели
