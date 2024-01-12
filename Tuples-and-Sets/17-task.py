from collections import deque

colors_substrings = deque(c for c in input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
final_colors = []

while colors_substrings:
    if len(colors_substrings) > 1:
        first_substring = colors_substrings.pop()
        last_substring = colors_substrings.popleft()
        result = last_substring + first_substring
        opposite_result = first_substring + last_substring
        if result in main_colors or opposite_result in main_colors:
            if result in main_colors:
                final_colors.append(result)
            else:
                final_colors.append(opposite_result)
        elif result in secondary_colors or opposite_result in secondary_colors:
            if result in secondary_colors:
                final_colors.append(result)
            else:
                final_colors.append(opposite_result)
        else:
            first_substring = first_substring[:-1]
            last_substring = last_substring[:-1]
            result = last_substring + first_substring
            half = 0
            if len(colors_substrings) % 2 == 0:
                half = len(colors_substrings) / 2
            else:
                half = len(colors_substrings) // 2 + 1
            for i in range(len(colors_substrings) + 1):
                if i == half:
                    colors_substrings.append(result)
                else:
                    colors_substrings.append(colors_substrings.popleft())

    else:
        last_substring = colors_substrings.pop()
        if last_substring in main_colors:
            final_colors.append(last_substring)
        elif last_substring in secondary_colors:
            final_colors.append(last_substring)

for color in final_colors:
    if color == 'orange':
        if 'red' not in final_colors or 'yellow' not in final_colors:
            final_colors.remove(color)
    elif color == 'purple':
        if 'red' not in final_colors or 'blue' not in final_colors:
            final_colors.remove(color)
    elif color == 'green':
        if 'yellow' not in final_colors or 'blue' not in final_colors:
            final_colors.remove(color)

print(final_colors)
