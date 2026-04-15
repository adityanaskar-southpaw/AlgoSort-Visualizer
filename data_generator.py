import random
#random data
def generate_random(n):
    return [random.randint(1, 1000) for _ in range(n)]
#sorted data
def generate_sorted(n):
    return list(range(n))
#reversed data
def generate_reversed(n):
    return list(range(n, 0, -1))
#duplicate data
def generate_duplicates(n):
    return [random.choice([10, 20, 30, 40, 50]) for _ in range(n)]
