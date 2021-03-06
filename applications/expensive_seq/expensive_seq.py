# Your code here
cache = {}

def expensive_seq(x, y, z):
    # Your code here
    key = (x, y, z)
    if key not in cache:   
        cache[key] = None # What expensive thing should go here?

    return cache[key]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
