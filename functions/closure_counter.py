# Closure Counter
# Build three independent counters from make_counter() and show that each maintains its own state

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1 
        return count
    return inc

a = make_counter()
print(a())


b = make_counter()
b(), print(b())


c = make_counter()
c(), c(), print(c())