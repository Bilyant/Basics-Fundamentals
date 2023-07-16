""" Calculating the final prise of office supplies and
subtracting the given discount at the end   """

packet_of_pens_price = 5.8
packet_of_markers_price = 7.2
detergent_per_liter_price = 1.2

packet_of_pens_count = int(input())
packet_of_markers_count = int(input())
detergent_liters_count = int(input())
discount_percent = int(input())

expenses_for_supplies = (packet_of_pens_count * packet_of_pens_price) + (
            packet_of_markers_count * packet_of_markers_price) + (detergent_liters_count * detergent_per_liter_price)
discount = (expenses_for_supplies * discount_percent) / 100
final_sum = expenses_for_supplies - discount
print(final_sum)
