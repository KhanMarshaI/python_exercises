# Generator Pipeline
# Compose generator functions to read a file, strip whitespace, 
# filter out blank lines, and yield line numbers plus text.

# Each yield pauses the function and gives one line to whoever is consuming the generator
# First call to generator: reads line 1, yields it, pauses
def read_file(file_name):
    with open(f"{file_name}", "r") as file:
        for line in file:
            yield line

