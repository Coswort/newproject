#1
import random

numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))

print(numbers)

numbers.sort()

half_size = len(numbers) // 2
print(half_size)

median = None

if numbers_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2

print(median)


#2
with open('second.py', 'r+') as f:
   #f.write('Здарова братан!')
    print(f.read)


#3
def some_func(abc, param):
    return abc(*param)

def abc(name):
    print('Hello {}'.format(name))

some_func(abc, ['friend'])


#4
print(list(map(lambda x: x ** 2, range (1, 10))))
print(list(filter(lambda x: x > 5, range (1, 10))))


#5
def str_list(num_list):
    return list(map(str, num_list))

print(str_list(range(5)))


#6
from functools import reduce

def some_func(par):
    return par

print(reduce(some_func, ['тест']))


#7
from functools import partial

def func(firstname, secondname):
    return '{} {}'.format(firstname, secondname)

hier = partial(func, secondname = 'Bakursky')

print(hier('Andrey'))


#8
num_list = range(6)
squared_list = [x ** 2 for x in num_list]

print(list(zip(num_list, squared_list)))


#9
import functools

def logger(func):
    @functools.wraps(func)
    def wrapped(num_list):
        result = func(num_list)
        with open('second.py', 'w') as f:
            f.write(str(result))

        return result
    return wrapped

@logger
def summ(num_list):
    return sum(num_list)

summ([1, 2, 3])

with open('second.py', 'r') as f:
    print('second.py: {}'.format(f.read()))

print(summ.__name__)


#10
def func(start, end):
    current = start
    while current < end:
        yield current
        current += 2

for number in func(0, 10):
    print(number)


#11
class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

earth = Planet("Earth")
print(earth)


#12
class Plan:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Planet {}".format(self.name)

mars = Plan("Mars")
print(mars)


#13
class Planet:
    """planet = Planet.__new__(Planet, "Earth")"""

    def __new__(cls, *args, **kwargs):
        print("__new__called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__called")
        self.name = name

earth = Planet("Earth")


#14
class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print("Welcome to {}, {}!".format(self.name, human.name, ))
        self.population.append(human)

mars = Planet("Mars")
bob = Human("Bob")
mars.add_human(bob)


#15
from datetime import date

def extract_description(user_string):
    return "Открытие чемпионата мира по футболу"

def extract_date(user_stirng):
    return date(2018, 6, 14)

class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return "Event \"{}\" at {}".format(self.description, self.date)

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)

event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)


#16
class Robot:

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("make robot useless")
        del self._power

wall_e = Robot(50)
wall_e.power = -20
print(wall_e.power)

del wall_e.power







