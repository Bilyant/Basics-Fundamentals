day_of_the_week = input()
cinema_ticket_price = 0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Friday":
    cinema_ticket_price = 12
elif day_of_the_week == "Wednesday" or day_of_the_week == "Thursday":
    cinema_ticket_price = 14
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    cinema_ticket_price = 16
print(cinema_ticket_price)
