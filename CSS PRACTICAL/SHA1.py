import hashlib
message = input("Enter the message: ")
message = message.encode()
result = hashlib.sha1(message)
print("\nThe byte equivalent of hash is : ", end ="")
print(result.digest())
print("\nThe hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())