animals = input().split(", ")
wolf = "wolf"
for animal in animals:
    wolf_index = abs(animals.index(wolf) - len(animals))
    wolf_actual_index = animals.index(wolf)
    last_index = len(animals) - 1
    if wolf_actual_index != last_index:
        sheep_number = wolf_index - 1
        print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
        break
    else:
        print("Please go away and stop eating my sheep")
        break
    