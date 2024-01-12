guests = int(input())
code = input()
regulars = set()
vip = set()
count = 0

while code != 'END':
    if count < guests:
        if code[0].isdigit():
            vip.add(code)
        else:
            regulars.add(code)
    else:
        if code in vip:
            vip.remove(code)
        elif code in regulars:
            regulars.remove(code)

    count += 1
    code = input()

vip = sorted(list(vip))
regulars = sorted(list(regulars))
left = len(vip) + len(regulars)
print(left)
print(*vip, sep='\n')
print(*regulars, sep='\n')
