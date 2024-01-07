substring = input()
string = input()

if substring in string:
    while substring in string:
        string = string.replace(substring, '')

print(string)
