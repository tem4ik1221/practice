# %% [markdown]
# # Углублённый урок Python: переменные и функции
#
# Формат файла: Python Percent (`# %%`)
#
# Такой файл удобно открывать в VS Code, PyCharm или других средах,
# которые поддерживают выполнение отдельных ячеек.
#
# В этом уроке:
# - как Python хранит переменные;
# - ссылки на объекты и `id()`;
# - изменяемые и неизменяемые типы;
# - распаковка и множественное присваивание;
# - области видимости LEGB;
# - `global` и `nonlocal`;
# - аргументы функций;
# - `*args` и `**kwargs`;
# - позиционные и именованные параметры;
# - значения по умолчанию;
# - функции как объекты;
# - вложенные функции и замыкания;
# - аннотации типов;
# - `lambda`;
# - рекурсия;
# - документирование функций;
# - практические задания.

# %% [markdown]
# # Что такое переменная в Python
#
# Переменная в Python — это **имя, связанное с объектом**.
#
# Очень важно не представлять переменную как коробку, внутри которой физически
# лежит значение.
#
# Когда мы пишем:
#
#     age = 25
#
# концептуально происходит следующее:
#
#     имя `age`  ─────────────►  объект `25`
#
# Имя `age` существует в некотором пространстве имён (namespace),
# а объект `25` существует в памяти Python.
#
# Оператор `=` создаёт связь между именем и объектом.
#
# Более точная формулировка:
#
# > Переменная в Python — это имя, которое ссылается на объект.
#
# У самого имени нет собственного типа.
# Тип принадлежит объекту, на который имя ссылается.

# %%
age = 25

print("Значение:", age)
print("Тип объекта:", type(age))
print("Идентификатор объекта:", id(age))

# %% [markdown]
# ## Что находится в памяти
#
# Упрощённо можно представить:
#
#     namespace
#     ┌───────────────┐
#     │ age           │
#     │   │           │
#     └───│───────────┘
#         │
#         ▼
#
#     память с объектами
#     ┌─────────────────────┐
#     │ объект int          │
#     │ значение: 25        │
#     │ тип: int            │
#     │ служебные данные    │
#     └─────────────────────┘
#
# Python хранит не только само значение.
# Объект также содержит служебную информацию, необходимую интерпретатору.
#
# Детали внутреннего устройства зависят от реализации Python.
# Наиболее распространённая реализация — CPython.
#
# В CPython каждый объект содержит служебную информацию,
# например данные о типе объекта и управлении временем его жизни.
#
# Для изучения Python обычно достаточно понимать модель:
#
#     ИМЯ -> ССЫЛКА -> ОБЪЕКТ
#
# а не конкретные байты в оперативной памяти.

# %%
number = 100

print("number:", number)
print("type(number):", type(number))
print("id(number):", id(number))

# `id()` возвращает уникальный идентификатор объекта
# на протяжении времени его существования.
#
# В CPython этот идентификатор обычно связан с адресом объекта в памяти,
# но в общем случае язык Python не требует,
# чтобы `id()` буквально являлся физическим адресом памяти.

# %% [markdown]
# ## Одному объекту могут соответствовать несколько имён
#
# Рассмотрим:
#
#     a = 1000
#     b = a
#
# После `b = a` значение объекта не обязательно копируется.
#
# Концептуально:
#
#     a ─────┐
#            ├────────► объект 1000
#     b ─────┘
#
# Имена `a` и `b` могут ссылаться на один объект.

# %%
a = 1000
b = a
print("id(a) =", id(a))
b=1002

print("a =", a)
print("b =", b)

print("id(a) =", id(a))
print("id(b) =", id(b))

print("a is b:", a is b)

# %%
# `==` сравнивает значения.
# `is` проверяет, один ли это объект.

x = [1, 2, 3]
y = [1, 2, 3]
z=x

print("x == y:", x == y)
print("x is y:", x is y)
print("x is z:", x is z)

print("id(x):", id(x))
print("id(y):", id(y))

# Значения одинаковые, но объекты разные.

# %% [markdown]
# ## Что происходит при повторном присваивании
#
# Код:
#
#     score = 10
#     score = 20
#
# не изменяет объект `10`.
#
# Вместо этого имя `score` начинает ссылаться на другой объект:
#
# Сначала:
#
#     score ─────► 10
#
# Затем:
#
#     score ─────► 20
#
# Если на старый объект больше ничего не ссылается,
# Python сможет освободить связанную с ним память,
# когда объект больше не нужен.

# %%
score = 10

old_id = id(score)

print("До:")
print("score =", score)
print("id =", old_id)

score = 20

print("\nПосле:")
print("score =", score)
print("id =", id(score))

print("Объект изменился:", old_id != id(score))

# %% [markdown]
# ## Изменяемые и неизменяемые объекты
#
# Это напрямую связано с тем, как переменные ведут себя в памяти.
#
# Неизменяемые объекты нельзя изменить "на месте".
#
# Например:
#
#     x = 10
#     x = x + 1
#
# Python не превращает объект `10` в `11`.
# Имя `x` начинает ссылаться на другой объект.
#
# К распространённым неизменяемым типам относятся:
#
# - `int`
# - `float`
# - `bool`
# - `str`
# - `tuple`
# - `frozenset`

# %%
x = 10

before = id(x)

x = x + 1

after = id(x)

print("x =", x)
print("id до:", before)
print("id после:", after)

# %%
# Со списком ситуация другая.
#
# list — изменяемый объект.
#
# Его содержимое можно менять без создания нового списка.

numbers = [1, 2, 3]

before = id(numbers)

numbers.append(4)

after = id(numbers)

print(numbers)
print("id до:", before)
print("id после:", after)
print("Тот же объект:", before == after)

# %% [markdown]
# Концептуально:
#
# До append:
#
#     numbers ─────► [1, 2, 3]
#
# После append:
#
#     numbers ─────► [1, 2, 3, 4]
#
# Ссылка может остаться той же,
# а содержимое объекта изменилось.

# %%
# Особенно важно понимать алиасы — несколько имён одного объекта.

first = [10, 20]
second = first

second.append(30)

print("first:", first)
print("second:", second)

print("first is second:", first is second)

# Оба имени ссылаются на один список.

# %% [markdown]
# ## Ссылка и копия — не одно и то же
#
# Код:
#
#     second = first
#
# не создаёт копию списка.
#
# Он создаёт ещё одно имя для того же объекта.
#
# Чтобы получить независимый список, нужно сделать копию.

# %%
first = [10, 20]

same_object = first
independent_copy = first.copy()

first.append(30)

print("first:", first)
print(id(first))
print("same_object:", same_object)
print(id(same_object))
print("independent_copy:", independent_copy)
print(id(independent_copy))

print("first is same_object:", first is same_object)
print("first is independent_copy:", first is independent_copy)


# %% [markdown]
# ## Где хранятся локальные переменные и объекты
#
# При изучении низкоуровневых языков часто говорят:
#
# - стек (stack);
# - куча (heap).
#
# Для Python полезно относиться к этому осторожно.
#
# В CPython объекты Python обычно размещаются в динамической памяти,
# управляемой интерпретатором.
#
# При вызове функции Python также создаёт объект состояния выполнения
# (frame), содержащий информацию о локальных именах, выполняемом коде
# и других данных.
#
# Поэтому учебное утверждение:
#
#     "все переменные хранятся в стеке"
#
# для Python является слишком грубым и часто вводит в заблуждение.
#
# Намного полезнее модель:
#
#     область видимости / namespace
#              │
#              ▼
#            имя
#              │
#              ▼
#           объект
#
# А конкретным размещением и освобождением памяти управляет
# реализация Python.

# %%
local_number = 123
print("id(local_number):", id(local_number))
print(local_number)

def memory_demo():
    global local_number 
    local_number=124
    local_list = [1, 2, 3]

    print("id(local_number):", id(local_number))
    print(local_number)
    print("id(local_list):", id(local_list))


memory_demo()

print(local_number)
print(id(local_number))


# %% [markdown]
# ## Время жизни объекта
#
# Объект живёт, пока он нужен программе.
#
# В CPython важную роль играет подсчёт ссылок.
# Упрощённо:
#
#     data = [1, 2, 3]
#
# создаёт ссылку от имени `data` к списку.
#
# Если затем:
#
#     data = None
#
# имя `data` перестаёт ссылаться на этот список.
#
# Если других ссылок на список нет, он становится недоступным,
# и память может быть освобождена.
#
# Python также имеет сборщик мусора для обработки некоторых циклических ссылок.

# %%
data = [1, 2, 3]

print("До:", data)
print("id:", id(data))

data = None

print("После:", data)
print(id(data))

data=10


print("После:", data)
print(id(data))
# Старый список больше не доступен через имя data.

# %% [markdown]
# ## Важный итог
#
# Запомните четыре идеи:
#
# 1. Переменная в Python — это **имя**.
# 2. Имя **ссылается на объект**.
# 3. Объект имеет **тип, значение и служебную информацию**.
# 4. Несколько имён могут ссылаться на **один и тот же объект**.
#
# Поэтому хороший мысленный образ:
#
#     name ─────► object
#
# а не:
#
#     переменная = коробка со значением
#
# Эта модель особенно важна при работе со списками, словарями,
# функциями, классами и передачей аргументов в функции.

# %%
# ------------------------------------------------------------
# 1. ПЕРЕМЕННЫЕ: НЕ "КОРОБКИ", А ИМЕНА, ССЫЛАЮЩИЕСЯ НА ОБЪЕКТЫ
# ------------------------------------------------------------

x = 10
y = x

print("x =", x)
print("y =", y)

print("id(x) =", id(x))
print("id(y) =", id(y))

# x и y сейчас ссылаются на один и тот же объект целого числа 10.
print("x is y:", x is y)

# %% [markdown]
# В Python переменная — это имя, связанное с объектом.
#
# В выражении:
#
#     x = 10
#
# создаётся или используется объект `10`, а имя `x` начинает ссылаться на него.
#
# Оператор `=` не означает "положить число внутрь переменной".
# Он означает "связать имя с объектом".

# %%
x = 10
print("До изменения:", x, id(x))

x = 20
print("После изменения:", x, id(x))

# Имя x теперь ссылается на другой объект.

# %%
# ------------------------------------------------------------
# 2. ДИНАМИЧЕСКАЯ ТИПИЗАЦИЯ
# ------------------------------------------------------------

value = 100
print(value, type(value))

value = "Python"
print(value, type(value))

value = 3.14
print(value, type(value))

# Тип принадлежит объекту, а не имени переменной.

# %%
# ------------------------------------------------------------
# 3. НЕИЗМЕНЯЕМЫЕ И ИЗМЕНЯЕМЫЕ ОБЪЕКТЫ
# ------------------------------------------------------------

# Неизменяемые типы:
# int, float, bool, str, tuple, frozenset

a = 5
b = a

a += 1

print("a =", a)
print("b =", b)

# a теперь указывает на новый объект 6.
# b продолжает ссылаться на 5.

# %%
# Изменяемый объект: список

list_a = [1, 2, 3]
list_b = list_a

print("До изменения:")
print("list_a:", list_a)
print("list_b:", list_b)

list_a.append(4)

print("После изменения:")
print("list_a:", list_a)
print("list_b:", list_b)

print("Один объект?", list_a is list_b)

# %% [markdown]
# Это одна из важнейших особенностей Python.
#
# Если две переменные ссылаются на один изменяемый объект,
# изменение объекта видно через обе переменные.

# %%
# Как создать независимую копию списка:

original = [1, 2, 3]
copy_1 = original.copy()
copy_2 = list(original)
copy_3 = original[:]

copy_1.append(100)

print("original:", original)
print("copy_1:", copy_1)

# %%
# ------------------------------------------------------------
# 4. МНОЖЕСТВЕННОЕ ПРИСВАИВАНИЕ
# ------------------------------------------------------------

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# %%
# Обмен значений без временной переменной

left = "A"
right = "B"

left, right = right, left

print(left, right)

# %%
# Распаковка последовательности

person = ("Anna", 25, "Sofia")

name, age, city = person

print(name)
print(age)
print(city)

# %%
# Распаковка с *

numbers = [1, 2, 3, 4, 5, 6]

first, *middle = numbers

print("first:", first)
print("middle:", middle)
#print("last:", last)

# %%
# ------------------------------------------------------------
# 5. СОГЛАШЕНИЯ ОБ ИМЕНАХ
# ------------------------------------------------------------

user_name = "Ivan"       # snake_case для переменных
MAX_RETRIES = 5          # UPPER_CASE для условных констант
_private_value = 42      # подчёркивание: внутреннее использование

print(user_name, MAX_RETRIES, _private_value)

# %% [markdown]
# В Python нет настоящих констант на уровне языка.
# `MAX_RETRIES = 5` — это соглашение между программистами:
# переменную предполагается не изменять.

# %%
# ------------------------------------------------------------
# 6. УДАЛЕНИЕ ИМЕНИ
# ------------------------------------------------------------

temp = 123
print(temp)

del temp

# Следующая строка вызвала бы NameError:
# print(temp)

# %%
# ------------------------------------------------------------
# 7. ФУНКЦИИ: БАЗОВЫЙ СИНТАКСИС
# ------------------------------------------------------------

def greet():
    print("Привет из функции!")


greet()

# %%
# Функция с параметром

def greet_user(name):
    print(f"Привет, {name}!")


greet_user("Anna")
greet_user("Ivan")

# %%
# Функция с возвращаемым значением

def square(number):
    return number ** 2


result = square(5)
print(result)

# %% [markdown]
# `print()` выводит значение.
#
# `return` возвращает значение вызывающему коду.
#
# Это принципиально разные действия.

# %%
def wrong_square(number):
    print(number ** 2)


result = wrong_square(5)

print("Результат функции:", result)
# Результат будет None, потому что return отсутствует.

# %%
# ------------------------------------------------------------
# 8. RETURN НЕМЕДЛЕННО ЗАВЕРШАЕТ ФУНКЦИЮ
# ------------------------------------------------------------

def check_age(age):
    if age < 0:
        return "Ошибка: возраст не может быть отрицательным"

    if age < 18:
        return "Несовершеннолетний"

    return "Совершеннолетний"


print(check_age(-5))
print(check_age(15))
print(check_age(25))

# %%
# ------------------------------------------------------------
# 9. НЕСКОЛЬКО ВОЗВРАЩАЕМЫХ ЗНАЧЕНИЙ
# ------------------------------------------------------------

def min_max(values):
    return min(values), max(values)


minimum, maximum = min_max([5, 1, 9, 3])

print("minimum:", minimum)
print("maximum:", maximum)

# На самом деле функция возвращает tuple.

# %%
result = min_max([1, 2, 3])
print(result)
print(type(result))
print(result[1])


# %%
# ------------------------------------------------------------
# 10. ПОЗИЦИОННЫЕ И ИМЕНОВАННЫЕ АРГУМЕНТЫ
# ------------------------------------------------------------

def describe_person(name, age, city):
    print(f"{name=}, {age=}, {city=}")


describe_person("Maria", 30, "Varna")

describe_person(
    name="Maria",
    age=30,
    city="Varna",
)

# %%
# Можно смешивать, но позиционные аргументы должны идти раньше именованных.

describe_person("Alex", age=22, city="Plovdiv")

# %%
# ------------------------------------------------------------
# 11. ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
# ------------------------------------------------------------

def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(5, 3))

# %%
# ВАЖНАЯ ЛОВУШКА:
# изменяемое значение по умолчанию.

def bad_add_item(item, items=[]):
    items.append(item)
    return items


print(bad_add_item("A"))
print(bad_add_item("B"))
print(bad_add_item("C"))

# Один и тот же список используется между вызовами!

# %%
# Правильный вариант:

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item("A"))
print(add_item("B"))
print(add_item("C"))

# %%
# ------------------------------------------------------------
# 12. *args
# ------------------------------------------------------------

def total(*numbers):
    print("numbers =", numbers)
    return sum(numbers)


print(total(1, 2, 3))
print(total(10, 20, 30, 40))

# `numbers` внутри функции — tuple.

# %%
# ------------------------------------------------------------
# 13. **kwargs
# ------------------------------------------------------------

def show_profile(**info):
    print("info =", info)

    for key, value in info.items():
        print(f"{key}: {value}")


show_profile(
    name="Ivan",
    age=28,
    city="Sofia",
)

# %%
# ------------------------------------------------------------
# 14. *args И **kwargs ВМЕСТЕ
# ------------------------------------------------------------

def demo(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)


demo(
    1,
    2,
    3,
    4,
    5,
    name="Python",
    level="advanced",
)

# %%
# ------------------------------------------------------------
# 15. РАСПАКОВКА АРГУМЕНТОВ ПРИ ВЫЗОВЕ
# ------------------------------------------------------------

def add(a, b, c):
    return a + b + c


values = [10, 20, 30]

print(add(*values))

# %%
settings = {
    "name": "Anna",
    "age": 32,
    "city": "Burgas",
}

describe_person(**settings)

# %%
# ------------------------------------------------------------
# 16. ПОЗИЦИОННЫЕ-ТОЛЬКО ПАРАМЕТРЫ: /
# ------------------------------------------------------------

def divide(a, b, /):
    return a / b


print(divide(10, 2))

# Так нельзя:
# divide(a=10, b=2)

# Параметры до "/" принимаются только позиционно.

# %%
# ------------------------------------------------------------
# 17. ИМЕНОВАННЫЕ-ТОЛЬКО ПАРАМЕТРЫ: *
# ------------------------------------------------------------

def connect(host, *, timeout=5, retries=3):
    print(f"host={host}, timeout={timeout}, retries={retries}")


connect("example.com", timeout=10, retries=5)

# Нельзя:
# connect("example.com", 10, 5)

# %%
# ------------------------------------------------------------
# 18. КОМБИНАЦИЯ / И *
# ------------------------------------------------------------

def advanced_function(a, b, /, c, *, d):
    print(a, b, c, d)


advanced_function(1, 2, 3, d=4)

# %%
# ------------------------------------------------------------
# 19. ОБЛАСТИ ВИДИМОСТИ LEGB
# ------------------------------------------------------------

# L — Local
# E — Enclosing
# G — Global
# B — Built-in

x = "GLOBAL"


def outer():
    x = "ENCLOSING"

    def inner():
        x = "LOCAL"
        print(x)

    inner()


outer()

# %%
# Python ищет имя по правилу LEGB.

message = "global message"


def show_message():
    print(message)


show_message()

# %%
# ------------------------------------------------------------
# 20. ЛОКАЛЬНАЯ ПЕРЕМЕННАЯ
# ------------------------------------------------------------

value = 100


def example():
    value = 200
    print("inside:", value)


example()
print("outside:", value)

# %%
# ------------------------------------------------------------
# 21. GLOBAL
# ------------------------------------------------------------

counter = 0


def increment_global():
    global counter
    counter += 1


increment_global()
increment_global()
increment_global()

print(counter)

# %% [markdown]
# `global` позволяет изменять глобальное имя внутри функции.
#
# Но частое использование `global` обычно ухудшает архитектуру программы.
# Чаще лучше передавать значения через параметры и `return`.

# %%
# Более чистый вариант:

def increment(value):
    return value + 1


counter = 0

counter = increment(counter)
counter = increment(counter)
counter = increment(counter)

print(counter)

# %%
# ------------------------------------------------------------
# 22. NONLOCAL
# ------------------------------------------------------------

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_function = make_counter()

print(counter_function())
print(counter_function())
print(counter_function())

# %% [markdown]
# `nonlocal` означает:
# "использовать переменную из ближайшей внешней функции,
# но не из глобальной области".

# %%
# ------------------------------------------------------------
# 23. ФУНКЦИИ — ОБЪЕКТЫ ПЕРВОГО КЛАССА
# ------------------------------------------------------------

def hello(name):
    return f"Hello, {name}"


another_name = hello

print(another_name("Python"))

# Функцию можно присвоить переменной.

# %%
# Функцию можно передать в другую функцию.

def apply_operation(operation, value):
    return operation(value)


def double(x):
    return x * 2


print(apply_operation(double, 10))

# %%
# Функция может возвращать другую функцию.

def make_multiplier(multiplier):
    def multiply(value):
        return value * multiplier

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))
print(triple(10))

# %%
# ------------------------------------------------------------
# 24. ЗАМЫКАНИЯ
# ------------------------------------------------------------

def create_power(exponent):
    def power(base):
        return base ** exponent

    return power


square = create_power(2)
cube = create_power(3)

print(square(5))
print(cube(5))

# Внутренняя функция "помнит" exponent.

# %%
# ------------------------------------------------------------
# 25. LAMBDA
# ------------------------------------------------------------

square_lambda = lambda x: x ** 2

print(square_lambda(6))

# Эквивалент:

def square_regular(x):
    return x ** 2


print(square_regular(6))

# %%
# lambda особенно полезна для коротких функций.

names = ["Bob", "Alexander", "Eva", "Christopher"]

sorted_names = sorted(names, key=lambda name: len(name))

print(sorted_names)

# %%
# ------------------------------------------------------------
# 26. АННОТАЦИИ ТИПОВ
# ------------------------------------------------------------

def calculate_price(price: float, quantity: int) -> float:
    return price * quantity


print(calculate_price(9.99, 3))

# Аннотации сами по себе не запрещают передавать другие типы.
# Они помогают IDE, анализаторам типов и другим программистам.

# %%
def greet_typed(name: str, age: int | None = None) -> str:
    if age is None:
        return f"Привет, {name}!"

    return f"Привет, {name}! Тебе {age} лет."


print(greet_typed("Anna"))
print(greet_typed("Anna", 25))

# %%
# ------------------------------------------------------------
# 27. DOCSTRING
# ------------------------------------------------------------

def calculate_discount(price: float, percent: float) -> float:
    """
    Рассчитывает цену после применения скидки.

    Args:
        price: Исходная цена.
        percent: Размер скидки в процентах.

    Returns:
        Цена после применения скидки.
    """
    return price * (1 - percent / 100)


print(calculate_discount(1000, 15))

print(calculate_discount.__doc__)

# %%
# ------------------------------------------------------------
# 28. ПАРАМЕТР percent: ПРАКТИЧЕСКИЙ ПРИМЕР
# ------------------------------------------------------------

def increase_by_percent(value: float, percent: float) -> float:
    """Увеличивает значение на заданный процент."""
    return value * (1 + percent / 100)


def decrease_by_percent(value: float, percent: float) -> float:
    """Уменьшает значение на заданный процент."""
    return value * (1 - percent / 100)


salary = 2000

print("После повышения:", increase_by_percent(salary, 10))
print("После уменьшения:", decrease_by_percent(salary, 10))

# %% [markdown]
# Обратите внимание:
#
# увеличить число на 10% и затем уменьшить результат на 10%
# — это не значит вернуться к исходному значению.
#
# 2000 -> +10% = 2200
# 2200 -> -10% = 1980

# %%
# ------------------------------------------------------------
# 29. ПРОВЕРКА АРГУМЕНТОВ
# ------------------------------------------------------------

def apply_discount(price: float, percent: float) -> float:
    if price < 0:
        raise ValueError("price не может быть отрицательным")

    if not 0 <= percent <= 100:
        raise ValueError("percent должен быть от 0 до 100")

    return price * (1 - percent / 100)


print(apply_discount(500, 20))

# Попробуйте:
# print(apply_discount(500, 150))

# %%
# ------------------------------------------------------------
# 30. РЕКУРСИЯ
# ------------------------------------------------------------

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n должно быть >= 0")

    if n in (0, 1):
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# %% [markdown]
# Рекурсивная функция вызывает саму себя.
#
# Обязательно должен быть базовый случай, который прекращает рекурсию.
#
# Для многих задач цикл в Python проще и эффективнее,
# но рекурсия полезна для деревьев, вложенных структур и некоторых алгоритмов.

# %%
# ------------------------------------------------------------
# 31. ФУНКЦИЯ БЕЗ ЯВНОГО RETURN
# ------------------------------------------------------------

def do_nothing():
    pass


result = do_nothing()

print(result)
print(result is None)

# %%
# ------------------------------------------------------------
# 32. NONE И "НЕТ ЗНАЧЕНИЯ"
# ------------------------------------------------------------

def find_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

    return None


print(find_even([1, 3, 4, 7]))
print(find_even([1, 3, 5, 7]))

# %%
# ------------------------------------------------------------
# 33. ПЕРЕДАЧА ИЗМЕНЯЕМЫХ ОБЪЕКТОВ В ФУНКЦИИ
# ------------------------------------------------------------

def append_value(items, value):
    items.append(value)


numbers = [1, 2, 3]

append_value(numbers, 4)

print(numbers)

# Функция изменила исходный список.

# %%
# Если менять исходный список не нужно:

def appended_copy(items, value):
    new_items = items.copy()
    new_items.append(value)
    return new_items


numbers = [1, 2, 3]
new_numbers = appended_copy(numbers, 4)

print("numbers:", numbers)
print("new_numbers:", new_numbers)

# %%
# ------------------------------------------------------------
# 34. ПЕРЕМЕННЫЕ ВНУТРИ ЦИКЛОВ
# ------------------------------------------------------------

for i in range(3):
    temporary = i * 10

print("i =", i)
print("temporary =", temporary)

# В Python for не создаёт отдельную блочную область видимости.
# Переменные остаются доступны после цикла.

# %%
# ------------------------------------------------------------
# 35. ФУНКЦИИ И СЛОВАРЬ ОПЕРАЦИЙ
# ------------------------------------------------------------

def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


operations = {
    "+": add_numbers,
    "-": subtract_numbers,
    "*": multiply_numbers,
}

operator = "*"

result = operations[operator](10, 5)

print(result)

# %%
# ------------------------------------------------------------
# 36. ПРАКТИКА 1
# ------------------------------------------------------------

# Задание:
# Создайте переменные:
# product_name
# product_price
# discount_percent
#
# Затем вычислите итоговую цену со скидкой.

product_name = "Laptop"
product_price = 1500
discount_percent = 12

final_price = product_price * (1 - discount_percent / 100)

print(product_name)
print(final_price)

# %%
# ------------------------------------------------------------
# 37. ПРАКТИКА 2
# ------------------------------------------------------------

# Напишите функцию calculate_tax(amount, percent),
# которая возвращает размер налога.

def calculate_tax(amount: float, percent: float) -> float:
    return amount * percent / 100


print(calculate_tax(1000, 20))

# %%
# ------------------------------------------------------------
# 38. ПРАКТИКА 3
# ------------------------------------------------------------

# Напишите функцию final_price(price, discount_percent=0, tax_percent=0),
# которая сначала применяет скидку,
# затем начисляет налог.

def final_price(
    price: float,
    discount_percent: float = 0,
    tax_percent: float = 0,
) -> float:
    price_after_discount = price * (1 - discount_percent / 100)
    price_after_tax = price_after_discount * (1 + tax_percent / 100)

    return price_after_tax


print(final_price(1000, discount_percent=10, tax_percent=20))

# %%
# ------------------------------------------------------------
# 39. ПРАКТИКА 4: ФУНКЦИЯ С *args
# ------------------------------------------------------------

# Напишите функцию average(*numbers),
# возвращающую среднее арифметическое.

def average(*numbers: float) -> float:
    if not numbers:
        raise ValueError("Нужно передать хотя бы одно число")

    return sum(numbers) / len(numbers)


print(average(10, 20, 30, 40))

# %%
# ------------------------------------------------------------
# 40. ПРАКТИКА 5: ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА
# ------------------------------------------------------------

def apply_to_each(function, values):
    return [function(value) for value in values]


numbers = [1, 2, 3, 4]

print(apply_to_each(lambda x: x ** 2, numbers))
print(apply_to_each(lambda x: x * 10, numbers))

# %%
# ------------------------------------------------------------
# 41. ПРАКТИКА 6: ЗАМЫКАНИЕ
# ------------------------------------------------------------

def make_discount(percent: float):
    def apply(price: float) -> float:
        return price * (1 - percent / 100)

    return apply


student_discount = make_discount(10)
vip_discount = make_discount(25)

print(student_discount(1000))
print(vip_discount(1000))

# %%
# ------------------------------------------------------------
# 42. ЗАДАНИЯ ДЛЯ САМОСТОЯТЕЛЬНОЙ РАБОТЫ
# ------------------------------------------------------------

# 1.
# Создайте функцию `convert_temperature(value, scale)`.
# Она должна переводить:
# - Celsius -> Fahrenheit
# - Fahrenheit -> Celsius
#
def convert_temperature(value, scale):
    if scale == "C":
        return value * 9 / 5 + 32  # Celsius to Fahrenheit
    elif scale == "F":
        return (value - 32) * 5 / 9  # Fahrenheit to Celsius
    else:
        raise ValueError("Scale must be 'C' or 'F'")
print(convert_temperature(100, "F"))

# %%
# 2.
# Создайте функцию:
#
#     calculate_profit(revenue, expenses, tax_percent=0)
#
# Функция должна вычислять прибыль после налога.
#
def calculate_profit(revenue, expenses, tax_percent=0):
    profit = revenue - expenses
    if profit > 0:
        profit = profit * tax_percent / 100
    return profit 
print (calculate_profit(1000, 800, 20))

# %%
# 3.
# Создайте функцию:
#
#     normalize_percent(percent)
#
# Если percent < 0, вернуть 0.
# Если percent > 100, вернуть 100.
# Иначе вернуть percent.
#
def normalize_percent(percent):
    if percent < 0: 
        return 0
    elif percent > 100:
        return 100
    else:
        return percent
print(normalize_percent(21))

# %%
# 4.
# Создайте функцию `make_prefix(prefix)`,
# которая возвращает функцию для добавления префикса к строке.
#
# Пример:
#
#     error = make_prefix("[ERROR] ")
#     print(error("Файл не найден"))
#
def make_prefix(prefix):
    def add_prefix(text):
        return prefix + text
    return add_prefix

error = make_prefix("[ERROR]")
print(error("Файл не найден"))

# %%
# 5.
# Создайте функцию:
#
#     summarize(*numbers)
#
# Она должна вернуть словарь:
#
# {
#     "count": ...,
#     "sum": ...,
#     "min": ...,
#     "max": ...,
#     "average": ...
# }
#
def summarize(*numbers):
    total = sum(numbers)
    count = len(numbers)
    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max (numbers),
        "average": total/count,   
    }
print(summarize(1, 2, 12, 21, 123, 321))

# %%
# ------------------------------------------------------------
# 43. КОНТРОЛЬНЫЕ ВОПРОСЫ
# ------------------------------------------------------------

questions = [
    "1. Является ли переменная контейнером или именем-ссылкой?",
    "2. В чём разница между `is` и `==`?",
    "3. Почему опасно использовать список как значение параметра по умолчанию?",
    "4. Что возвращает функция без `return`?",
    "5. Что такое *args?",
    "6. Что такое **kwargs?",
    "7. Как работает правило LEGB?",
    "8. Чем `global` отличается от `nonlocal`?",
    "9. Можно ли передать функцию как аргумент?",
    "10. Что такое замыкание?",
]

for question in questions:
    print(question)
answers = [
    "1. Переменная в Python — это имя, которое ссылается на объект.",
    "2. `is` проверяет, один ли это объект, `==` сравнивает значения.",
    "3. Список как значение по умолчанию сохраняется между вызовами функции, что может привести к неожиданным результатам.",
    "4. Функция без `return` возвращает `None`.",
    "5. *args собирет все позиционные аргументы в кортеж.",
    "6. **kwargs собирает все именованные аргументы в словарь.",
    "7. LEGB — это порядок поиска имени: Local, Enclosing, Global, Built-in.",
    "8. `global` позволяет изменять глобальные переменные, а `nonlocal` позволяет изменять переменные из ближайшей внешней функции.",
    "9. Да, можно.",
    "10. Замыкание — это функция, которая запоминает значения переменных из внешней функции.",
]
for answer in answers:
    print(answer) 


# %% [markdown]
# ## Краткое резюме
#
# **Переменные**
#
# - переменные в Python являются именами, которые ссылаются на объекты;
# - тип принадлежит объекту;
# - изменяемые объекты могут изменяться через разные ссылки;
# - распаковка позволяет удобно присваивать несколько значений.
#
# **Функции**
#
# - функции создаются через `def`;
# - `return` возвращает результат;
# - аргументы могут быть позиционными и именованными;
# - `*args` собирает дополнительные позиционные аргументы;
# - `**kwargs` собирает дополнительные именованные аргументы;
# - функции можно сохранять в переменные, передавать и возвращать;
# - вложенные функции позволяют создавать замыкания;
# - области видимости подчиняются правилу LEGB;
# - `global` и `nonlocal` позволяют изменять значения во внешних областях,
#   но использовать их следует осознанно.
#
# После этого урока полезно перейти к:
#
# 1. коллекциям (`list`, `dict`, `set`, `tuple`);
# 2. comprehensions;
# 3. исключениям;
# 4. модулям;
# 5. декораторам;
# 6. классам и ООП.
