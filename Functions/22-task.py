def sorting_cheeses(**kwargs):
    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    result = []
    for cheese, values in sorted_kwargs.items():
        result.append(cheese)
        sorted_values = list(sorted(values, key=lambda x: -x))
        for value in sorted_values:
            result.append(str(value))
    return '\n'.join(result)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
