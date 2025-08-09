# Benchmark (time.perf_counter) deduplication of two million random URLs using a set versus list membership checks.

import random 
import time

def generate_urls(filename, amount, unique_urls):
    with open(filename, "w") as file:
        for i in range(amount):
            randomPart = random.randint(1, unique_urls)
            url = f"https://example.com/section/{randomPart}"
            file.write(url + "\n")

# generate_urls("urls_2m.txt", 2_000_000, 1_500_000)
# don't open the txt file in VS Code with a poo poo RAM

with open("urls_2m.txt", "r") as file:
    all_urls = [line.strip() for line in file]

t1_start = time.perf_counter()

uniqueURL_set = set(all_urls)

t1_stop = time.perf_counter()

print("Time for unique set:", t1_stop - t1_start)

# -------------------------------------------------------------------------------

t2_start = time.perf_counter()

uniqueURL_list = []

for url in all_urls:
    if url not in uniqueURL_list:
        uniqueURL_list.append(url)

t2_stop = time.perf_counter()

print("Time for unique list:", t2_stop - t2_start)