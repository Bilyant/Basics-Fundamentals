love_greeting = 'Hello, my love!'
boyfriend = 'Johnny'
greeting = ''

name = input()

if name != boyfriend:
    greeting = f'Hello, {name}!'
else:
    greeting = love_greeting

print(greeting)
