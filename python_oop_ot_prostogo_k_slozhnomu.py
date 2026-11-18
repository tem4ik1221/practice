# %% 0. Как работать с уроком
# ООП — объектно-ориентированное программирование.
# Объект объединяет данные (атрибуты) и действия с ними (методы).
# Класс описывает устройство объектов, а экземпляр — конкретный объект класса.
# Запускай блоки # %% по порядку или выполни файл целиком.
# Используется только стандартная библиотека Python 3.9+.
# В конце есть задания для самостоятельной работы.

print('Урок ООП: от классов к небольшому проекту')


# %% 1. Самый простой класс и два объекта
class Cat:
    pass  # Пустое тело класса: описание добавим позже.


cat_one = Cat()
cat_two = Cat()
# Атрибут можно добавить конкретному объекту после его создания.
cat_one.name = 'Мурка'
cat_two.name = 'Барсик'

print(cat_one.name)  # Мурка
print(cat_two.name)  # Барсик
print(cat_one is cat_two)  # False: это разные объекты.
print(isinstance(cat_one, Cat))  # True


# %% 2. __init__: начальные данные объекта
# __init__ вызывается автоматически при создании экземпляра.
# Точнее, это метод инициализации: сам объект создаёт __new__.
# self — ссылка на экземпляр, с которым сейчас работает метод.
# Имя self принято по соглашению; Python передаёт объект автоматически.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


dog = Dog('Рекс', 3)
print(f'{dog.name}, возраст: {dog.age}')
dog.age += 1
print(f'После дня рождения: {dog.age}')  # 4


# %% 3. Методы: действия объекта и возвращаемые значения
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def scale(self, factor):
        self.width *= factor
        self.height *= factor


rectangle = Rectangle(3, 4)
print('Площадь:', rectangle.area())  # 12
# rectangle.area() равнозначно Rectangle.area(rectangle).
rectangle.scale(2)
print('После увеличения:', rectangle.area())  # 48
# return возвращает результат вызывающему коду, print только выводит его.


# %% 4. Атрибут класса и атрибут экземпляра
class Student:
    school = 'Школа Python'  # Общий атрибут класса.

    def __init__(self, name):
        self.name = name  # Собственный атрибут каждого экземпляра.


anna = Student('Анна')
ivan = Student('Иван')
print(anna.school, ivan.school)
Student.school = 'Академия Python'
print(anna.school, ivan.school)  # Оба видят новое значение класса.
anna.school = 'Личная школа'  # Создаём атрибут экземпляра с тем же именем.
print(anna.school, ivan.school)  # Личная школа Академия Python


# %% 5. Частая ошибка: общий изменяемый атрибут
class BadTeam:
    members = []  # Один список на весь класс!


bad_first = BadTeam()
bad_second = BadTeam()
bad_first.members.append('Анна')
print(bad_second.members)  # ['Анна']: список общий.


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []  # Новый отдельный список при каждом вызове __init__.

    def add_member(self, name):
        self.members.append(name)


first_team = Team('Первая')
second_team = Team('Вторая')
first_team.add_member('Анна')
print(first_team.members)  # ['Анна']
print(second_team.members)  # []


# %% 6. Инкапсуляция: изменение состояния через методы
# Инкапсуляция позволяет сосредоточить правила работы с данными в классе.
# _balance: один подчёркивающий знак означает «внутренняя деталь».
# Это соглашение, а не запрет доступа со стороны Python.
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError('Начальный баланс не может быть отрицательным')
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Сумма снятия должна быть положительной')
        if amount > self._balance:
            raise ValueError('Недостаточно средств')
        self._balance -= amount

    @property
    def balance(self):
        # Свойство без setter доступно для чтения через account.balance.
        return self._balance


account = BankAccount('Анна', 100)
account.deposit(50)
account.withdraw(30)
print('Баланс:', account.balance)  # 120
try:
    account.withdraw(1000)
except ValueError as error:
    print('Ожидаемая ошибка:', error)
# Для реальных денежных расчётов обычно используют Decimal или целые копейки.


# %% 7. @property и setter: проверка присваиваемых значений
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # Уже проходит через setter ниже.

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Температура ниже абсолютного нуля')
        self._celsius = value

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


temperature = Temperature(20)
temperature.celsius = 25
print(f'{temperature.celsius} °C = {temperature.fahrenheit} °F')
try:
    temperature.celsius = -300
except ValueError as error:
    print('Ожидаемая ошибка:', error)


# %% 8. @classmethod и @staticmethod
class Product:
    def __init__(self, name, price):
        if not self.is_valid_price(price):
            raise ValueError('Цена должна быть неотрицательной')
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, text):
        # cls — класс, через который вызвали метод.
        # Альтернативный способ создания экземпляра.
        name, price = text.split(';')
        return cls(name, float(price))

    @staticmethod
    def is_valid_price(price):
        # Нет ни self, ни cls: функция не использует состояние объекта/класса.
        return price >= 0


product = Product.from_string('Книга;500')
print(product.name, product.price)  # Книга 500.0
print(Product.is_valid_price(-10))  # False


# %% 9. Наследование, переопределение и super()
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Какой-то звук'


class Puppy(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Инициализация части, описанной в Animal.
        self.breed = breed

    def speak(self):
        return 'Гав!'


puppy = Puppy('Бобик', 'Корги')
print(puppy.name, puppy.breed, puppy.speak())
print(isinstance(puppy, Animal))  # True
print(issubclass(Puppy, Animal))  # True
# Наследование подходит для отношения «является»: щенок является животным.


# %% 10. Полиморфизм и утиная типизация
# Один вызов .speak() работает с объектами разных классов.
class Robot:
    def speak(self):
        return 'Бип!'


def introduce(speaker):
    return f'Говорит: {speaker.speak()}'


for speaker in [Animal('Зверь'), Puppy('Тузик', 'Дворняга'), Robot()]:
    print(introduce(speaker))
# Robot не наследует Animal. Достаточно наличия нужного метода.


# %% 11. Композиция: объект содержит другой объект
class Engine:
    def start(self):
        return 'Двигатель запущен'


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def drive(self):
        return f'{self.model}: {self.engine.start()}, поехали!'


car = Car('Учебный автомобиль', Engine())
print(car.drive())
# Автомобиль содержит двигатель. Такое отношение удобно выражать композицией.


# %% 12. Специальные методы: __str__, __repr__, __eq__, __add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # Читаемый текст для print() и str().
        return f'Вектор ({self.x}, {self.y})'

    def __repr__(self):
        # Представление для отладки и отображения внутри коллекций.
        return f'Vector({self.x!r}, {self.y!r})'

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


vector = Vector(1, 2) + Vector(3, 4)
print(vector)  # Вектор (4, 6)
print(repr(vector))  # Vector(4, 6)
print([vector])  # [Vector(4, 6)]
print(vector == Vector(4, 6))  # True
# NotImplemented сообщает Python, что данный тип операнда не поддерживается.


# %% 13. Абстрактный класс: обязательный интерфейс наследников
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным')
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


print(f'Площадь круга: {Circle(3).area():.2f}')  # 28.27
try:
    Shape()
except TypeError:
    print('Нельзя создать экземпляр с нереализованным абстрактным методом')


# %% 14. dataclass: класс для хранения данных
from dataclasses import dataclass, field


@dataclass
class Course:
    title: str
    students: list[str] = field(default_factory=list)
    # default_factory создаёт отдельный список для каждого экземпляра.
    # dataclass автоматически добавляет __init__, __repr__, __eq__.
    # Аннотации типов сами по себе не проверяют значения во время выполнения.


python_course = Course('Python')
sql_course = Course('SQL')
python_course.students.append('Анна')
print(python_course)  # Course(title='Python', students=['Анна'])
print(sql_course.students)  # []
print(Course('SQL') == sql_course)  # True: сравнение полей.


# %% 15. Свой итератор: __iter__ и __next__
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


countdown = Countdown(3)
print(list(countdown))  # [3, 2, 1]
print(list(countdown))  # []: итератор уже исчерпан.
print(list(Countdown(3)))  # Новый объект — новый отсчёт.


# %% 16. Итоговый проект: корзина покупок
# Объединяем dataclass, композицию, проверки и специальные методы.
# Цены храним в целых копейках, чтобы избежать погрешностей float.
@dataclass(frozen=True)
class ShopItem:
    name: str
    price_kopecks: int

    def __post_init__(self):
        # Вызывается после автоматически созданного __init__.
        if type(self.price_kopecks) is not int or self.price_kopecks < 0:
            raise ValueError('Цена должна быть целым неотрицательным числом')


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add(self, item, quantity=1):
        if not isinstance(item, ShopItem):
            raise TypeError('Ожидается товар ShopItem')
        if type(quantity) is not int or quantity <= 0:
            raise ValueError('Количество должно быть целым положительным числом')
        self._items.append((item, quantity))

    @property
    def total_kopecks(self):
        return sum(item.price_kopecks * quantity for item, quantity in self._items)

    def __len__(self):
        # Здесь len(cart) означает количество единиц товара.
        return sum(quantity for _, quantity in self._items)

    def __iter__(self):
        return iter(self._items)


cart = ShoppingCart()
cart.add(ShopItem('Книга', 50000), quantity=2)
cart.add(ShopItem('Ручка', 7550))

for item, quantity in cart:
    rubles, kopecks = divmod(item.price_kopecks, 100)
    print(f'{item.name}: {quantity} шт. по {rubles}.{kopecks:02d} руб.')

total_rubles, total_remainder = divmod(cart.total_kopecks, 100)
print('Количество товаров:', len(cart))  # 3
print(f'Итого: {total_rubles}.{total_remainder:02d} руб.')  # 1075.50


# %% 17. Задания от простого к сложному
# 1. Создай класс Book с атрибутами title и author и методом description().
# 2. Добавь Rectangle метод perimeter(), возвращающий периметр.
# 3. Создай Counter с методами increment(), reset() и свойством value.
# 4. Добавь BankAccount метод transfer(other, amount). Продумай проверки:
#    при ошибке баланс обоих счетов должен оставаться прежним.
# 5. Создай наследника Animal — Bird, переопредели speak().
# 6. Добавь Shape наследника Square и выведи площади разных фигур в цикле.
# 7. Добавь Vector вычитание через __sub__.
# 8. Добавь ShoppingCart метод remove(name) и определи поведение для
#    отсутствующего товара и нескольких строк с одинаковым названием.
# 9. Создай Library, которая содержит объекты Book. Реализуй добавление,
#    поиск по автору, len(library) и перебор книг через for.
# 10. Объясни своими словами разницу между наследованием и композицией.

print('Урок завершён. Переходи к заданиям в блоке 17!')

# %% 1. 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f'«{self.title}», автор: {self.author}'
    
    def __repr__(self):
        return f'Book({self.title!r}, {self.author!r})'


book = Book('Капитанская дочка', 'А. С. Пушкин')
print(book.description()) 


# %% 2.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor


rectangle = Rectangle(3, 4)
print('Площадь:', rectangle.area())  
print('Периметр:', rectangle.perimeter())  
rectangle.scale(2)
print('Периметр после увеличения:', rectangle.perimeter())  


# %% 3. 
class Counter:
    def __init__(self):
        self._value = 0

    def increment(self):
        self._value += 1

    def reset(self):
        self._value = 0

    @property
    def value(self):
        return self._value


counter = Counter()
counter.increment()
counter.increment()
print('Счётчик:', counter.value)  # 2
counter.reset()
print('После сброса:', counter.value)  # 0
try:
    counter.value = 10  
except AttributeError:
    print('Ожидаемая ошибка: value доступно только для чтения')


# %% 4. 
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError('Начальный баланс не может быть отрицательным')
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной')
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Сумма снятия должна быть положительной')
        if amount > self._balance:
            raise ValueError('Недостаточно средств')
        self._balance -= amount

    def transfer(self, other, amount):
        if not isinstance(other, BankAccount):
            raise TypeError('Получатель должен быть счётом BankAccount')
        if other is self:
            raise ValueError('Нельзя переводить деньги на тот же счёт')
        if amount <= 0:
            raise ValueError('Сумма перевода должна быть положительной')
        if amount > self._balance:
            raise ValueError('Недостаточно средств для перевода')
    
        self._balance -= amount
        other._balance += amount

    @property
    def balance(self):
        return self._balance


anna = BankAccount('Анна', 100)
ivan = BankAccount('Иван', 20)
anna.transfer(ivan, 30)
print(anna.balance, ivan.balance)  

for bad_amount in (1000, -5, 0):
    try:
        anna.transfer(ivan, bad_amount)
    except ValueError as error:
        print('Ожидаемая ошибка:', error)
print(anna.balance, ivan.balance) 

try:
    anna.transfer(anna, 10)
except ValueError as error:
    print('Ожидаемая ошибка:', error)

try:
    anna.transfer('Иван', 10)
except TypeError as error:
    print('Ожидаемая ошибка:', error)
print(anna.balance, ivan.balance) 


# %% 5. 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'Какой-то звук'


class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        return 'Чирик!'


bird = Bird('Кеша')
print(bird.name, bird.speak()) 
print(isinstance(bird, Animal))  
print(Animal('Зверь').speak())  


# %% 6. 
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Радиус должен быть положительным')
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        if side <= 0:
            raise ValueError('Сторона должна быть положительной')
        self.side = side

    def area(self):
        return self.side ** 2


shapes = [Circle(3), Square(4), Square(2.5)]
for shape in shapes:
    print(f'{type(shape).__name__}: площадь {shape.area():.2f}')



# %% 7. 
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор ({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)


difference = Vector(5, 7) - Vector(2, 3)
print(difference)  
print(repr(difference))  
print(difference == Vector(3, 4)) 
try:
    Vector(1, 1) - 5
except TypeError as error:
    print('Ожидаемая ошибка:', error)


# %% 8.
from dataclasses import dataclass


@dataclass(frozen=True)
class ShopItem:
    name: str
    price_kopecks: int

    def __post_init__(self):
        if type(self.price_kopecks) is not int or self.price_kopecks < 0:
            raise ValueError('Цена должна быть целым неотрицательным числом')


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add(self, item, quantity=1):
        if not isinstance(item, ShopItem):
            raise TypeError('Ожидается товар ShopItem')
        if type(quantity) is not int or quantity <= 0:
            raise ValueError('Количество должно быть целым положительным числом')
        self._items.append((item, quantity))

    def remove(self, name):
        removed_units = sum(
            quantity for item, quantity in self._items if item.name == name
        )
        if removed_units == 0:
            raise ValueError(f'Товар «{name}» не найден в корзине')
        self._items = [
            (item, quantity) for item, quantity in self._items
            if item.name != name
        ]
        return removed_units

    @property
    def total_kopecks(self):
        return sum(item.price_kopecks * quantity for item, quantity in self._items)

    def __len__(self):
        return sum(quantity for _, quantity in self._items)

    def __iter__(self):
        return iter(self._items)


cart = ShoppingCart()
cart.add(ShopItem('Книга', 50000), quantity=2)
cart.add(ShopItem('Ручка', 7550))
cart.add(ShopItem('Книга', 45000)) 
print('До удаления:', len(cart))  

removed = cart.remove('Книга')
print('Удалено единиц:', removed) 
print('После удаления:', len(cart)) 
print('Итого копеек:', cart.total_kopecks)  

try:
    cart.remove('Книга')  
except ValueError as error:
    print('Ожидаемая ошибка:', error)


# %% 9.
class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        if not isinstance(book, Book):
            raise TypeError('Ожидается объект Book')
        self._books.append(book)

    def find_by_author(self, author):
        needle = author.casefold()
        return [book for book in self._books if book.author.casefold() == needle]

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)


library = Library()
library.add(Book('Капитанская дочка', 'А. С. Пушкин'))
library.add(Book('Евгений Онегин', 'А. С. Пушкин'))
library.add(Book('Война и мир', 'Л. Н. Толстой'))

print('Книг в библиотеке:', len(library))  # 3
print(library.find_by_author('а. с. пушкин'))
print(library.find_by_author('Гоголь'))  # []

for book in library:
    print(book.description())

try:
    library.add('Война и мир')
except TypeError as error:
    print('Ожидаемая ошибка:', error)


# %% 10.
# Наследование — отношение «является» (is-a): Puppy является Animal.
# Композиция — отношение «содержит / имеет» (has-a): Car содержит Engine.

