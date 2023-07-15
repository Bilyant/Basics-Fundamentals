""" Calculating the final price for computer parts """


allowed_budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

single_price_video_card = 250
single_price_processor = 0.35 * (single_price_video_card * video_cards)
single_price_ram_memory = 0.1 * (single_price_video_card * video_cards)

budget_required = (video_cards * single_price_video_card) + (processors * single_price_processor) + (
            ram_memory * single_price_ram_memory)
if video_cards > processors:
    budget_required = budget_required * 0.85
if budget_required <= allowed_budget:
    print(f"You have {(allowed_budget - budget_required):.2f} leva left!")
else:
    print(f"Not enough money! You need {(budget_required - allowed_budget):.2f} leva more!")
