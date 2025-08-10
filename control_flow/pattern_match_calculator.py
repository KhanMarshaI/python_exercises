# Pattern-Match Calculator
# Accept strings like "ADD 4 5" or "MUL 3 9". Use match … case to parse and compute the result.

print("Format for calculator: " \
"ADD X Y " \
"MUL X Y " \
"DIV X Y " \
"SUB X Y ")

operation = str(input("Enter an operation: "))

result = None
match operation.split():
    case ["ADD", x, y]:
        result = int(x) + int(y)
    case ["MUL", x, y]:
        result = int(x) * int(y)
    case ["SUB", x, y]:
        result = int(x) - int(y)
    case ["DIV", x, y]:
        result = int(x) / int(y)
    case _:
        print("Incorrect syntax.")

print("Result of the opeartion: ",result)
