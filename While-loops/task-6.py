deposit = input()
total_sum = 0
valid_operation = True
while deposit != "NoMoreMoney":
    current_deposit = float(deposit)
    if current_deposit < 0:
        valid_operation = False
        print("Invalid operation!")
        print(f"Total: {total_sum:.2f}")
        break
    print(f"Increase: {current_deposit:.2f}")
    total_sum += current_deposit
    deposit = input()
if valid_operation:
    print(f"Total: {total_sum:.2f}")
    