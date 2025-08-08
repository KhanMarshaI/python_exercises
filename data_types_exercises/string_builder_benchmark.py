# String Builder Benchmark
# Compare execution time between concatenating 10 000 lines with += versus collecting them in a list and "".join. Use time.perf_counter.

from time import perf_counter

t1_start = perf_counter()

line = "this is a line"

result = ""

for i in range(10000):
    result += line

t1_stop = perf_counter()

print("Concat time:", t1_stop - t1_start)

t2_start = perf_counter()

another_line = "this is a line"

lineList = [another_line for _ in range(10000)]

joinedList = "".join(lineList)

t2_stop = perf_counter()

print("Join time:", t2_stop - t2_start)

