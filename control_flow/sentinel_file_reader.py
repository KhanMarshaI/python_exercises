# Sentinel File Reader
# Read lines from a file until a line containing only STOP\n is found; count how many non-empty lines were read.

def readFileLines():
    count = 0
    with open("sample.txt", "r") as file:
        while (line := file.readline()):
            if line == "STOP\n":
                break
            if line.strip():
                count += 1
    return count
                
print(readFileLines())