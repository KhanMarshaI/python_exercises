# Generator Pipeline
# Compose generator functions to read a file, strip whitespace, 
# filter out blank lines, and yield line numbers plus text.

# Each yield pauses the function and gives one line to whoever is consuming the generator
# First call to generator: reads line 1, yields it, pauses
def read_file(file_name):
    with open(f"{file_name}", "r") as file:
        for line in file:
            yield line

def stripper(line_generator):
    for line in line_generator:
        yield line.strip()

def filterer(line_generator):
    for line in line_generator:
        if line:
            yield line

def line_number_and_text(line_generator):
    n=0
    for line in line_generator:
        n+=1
        yield (n, line)

raw = read_file("sample.txt")
whitespace = stripper(raw)
filtered = filterer(whitespace)
output = line_number_and_text(filtered)

for item in output:
    print(item)