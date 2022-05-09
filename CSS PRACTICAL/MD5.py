import hashlib
message = input("Enter the message: ")
message = message.encode()
result = hashlib.md5(message)
print("\nThe byte equivalent of hash is : ", end ="")
print(result.digest())
print("\nThe hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
