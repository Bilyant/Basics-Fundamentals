open_tabs_count = int(input())
salary = int(input())
fee = 0
website_name = ""
is_valid = False
for number in range(open_tabs_count):
    website_name = input()
    if website_name == "Facebook":
        fee += 150
    elif website_name == "Instagram":
        fee += 100
    elif website_name == "Reddit":
        fee += 50
    if fee > 0:
        salary -= fee
        fee = 0
    if salary <= 0:
        print("You have lost your salary.")
        is_valid = True
        break
if not is_valid:
    salary_left = salary - fee
    print(f"{salary_left}")
