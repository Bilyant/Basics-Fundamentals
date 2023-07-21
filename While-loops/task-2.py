name = input()
password = input()
password_attempt = input()
while password != password_attempt:
    password_attempt = input()
print(f"Welcome {name}!")
