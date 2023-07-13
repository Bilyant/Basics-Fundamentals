""" How many hour per day should you read in order to
finish a book from start to end based on the reading
speed and the pages count """

total_book_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())
total_reading_hours = total_book_pages / pages_per_hour
hours_per_day = total_reading_hours / days_for_reading
print(int(hours_per_day))
