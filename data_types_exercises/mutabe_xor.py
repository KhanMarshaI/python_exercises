# Mutable XOR 
# Create a function xor_bytes(data: bytearray, key: int) that XORs each byte with a one-byte key in place.

def xor_bytes(data: bytearray, key: int):
    for i in range(len(data)):
        data[i] = data[i] ^ key
    return data

user_message = str(input("Enter the message: "))
key = int(input("Enter one-byte key(0-255): "))

while key < 0 or key > 255:
    print("Key isn't one-byte.")
    key=int(input("Enter key: "))

message_bytes = bytes(user_message, 'utf-8')
message_byteArray = bytearray(message_bytes)

result_xor_byteArray = xor_bytes(message_byteArray, key)

print(result_xor_byteArray)
print("XOR Message hex:", result_xor_byteArray.hex())