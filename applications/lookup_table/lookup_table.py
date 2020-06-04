# Your code here
import math
cache = {}

def build_lookup_table():
    for i in range(2, 13):
        cache[i] = i

build_lookup_table()

# table should contain
# 2-13
# to the base of 3,4,5 each as integers
# 2: 8 > /5 > %982451653

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # am i to replicate the logic in lines 13-16 here?
    # or am i to do that at the top and put this all in a cache?


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
