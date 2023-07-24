key = int(input())
number = int(input())
output = ""
for i in range(number):
    letter = input()
    result = ord(letter) + key
    output += chr(result)
print(output)
