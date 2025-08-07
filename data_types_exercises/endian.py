def int_to_little_endian(n, length):
    try:
        result = n.to_bytes(length, 'little')
        byteArray = bytearray(result)
        print(byteArray)
        return byteArray
    except OverflowError:
        print(f"Error: {n} doesn't fit in {length} bytes.")
        return None


n = int(input("The Number to convert: "))
while(n<0):
    print("Number may only be positive.")
    n = int(input("Enter positive number: "))

length = int(input("Length of the number: "))

int_to_little_endian(n, length)