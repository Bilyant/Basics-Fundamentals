""" Calculations for filming expenses based
on the provided data """


budget = float(input())
statists_count = int(input())
statists_uniform_single_price = float(input())
decor = 0.1 * budget
statists_uniforms_total_price = statists_uniform_single_price * statists_count

if statists_count >= 150:
    statists_uniforms_total_price = statists_uniforms_total_price * 0.9
budget_required = statists_uniforms_total_price + decor
difference = abs(budget - budget_required)

if budget_required <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
