""" Calculating the cost for repainting which
includes the materials needed as well as the
labor cost  """

price_nylon_per_cubic_meter = 1.5
price_paint_per_liter = 14.5
price_paint_thinner_per_liter = 5
price_bag = 0.4

nylon_needed_cubic_meters = int(input())
paint_needed_liters = int(input())
paint_thinner_needed = int(input())
labor_cost_per_hour = int(input())

additional_paint = paint_needed_liters * 1.1
additional_nylon = nylon_needed_cubic_meters + 2
materials_cost = (additional_paint * price_paint_per_liter) + (additional_nylon * price_nylon_per_cubic_meter) + (
        paint_thinner_needed * price_paint_thinner_per_liter) + price_bag
labor_total_cost = labor_cost_per_hour * (materials_cost * 0.3)
final_cot = materials_cost + labor_total_cost
print(final_cot)
