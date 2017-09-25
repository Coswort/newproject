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

