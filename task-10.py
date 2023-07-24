number = int(input())
is_balanced = True
char = input()
while char:
    if char.strip() == "(":
        next_char = input()
        char_after_next_char = input()
        if char_after_next_char != ")":
            is_balanced = False
    if char.strip() == ")":
        next_char = input()
        char_after_next_char = input()
        if char_after_next_char != "(":
            is_balanced = False
    char = input()
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
    