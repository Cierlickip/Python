import random

def zero_one_iterator():
    while True:
        yield 0
        yield 1

zero_one_gen = zero_one_iterator()
for _ in range(10):
    print(next(zero_one_gen))

def random_direction_iterator():
    directions = ["N", "E", "S", "W"]
    while True:
        yield random.choice(directions)


direction_gen = random_direction_iterator()
for _ in range(10):
    print(next(direction_gen))


def day_of_week_iterator():
    days_of_week = list(range(7))
    while True:
        for day in days_of_week:
            yield day


day_of_week_gen = day_of_week_iterator()
for _ in range(15):
    print(next(day_of_week_gen))
