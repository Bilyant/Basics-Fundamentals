"""  Deposit Calculator """

deposited_sum = float(input())
deposited_time_months = int(input())
annual_interest = float(input())
interest_accumulated = (deposited_sum * annual_interest) / 100
monthly_interest = interest_accumulated / 12
final_amount = deposited_sum + (deposited_time_months * monthly_interest)
print(final_amount)
