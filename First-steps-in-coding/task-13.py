total_book_pages = int(input())
pages_per_hour = int(input())
days_for_reading = int(input())
total_reading_hours = total_book_pages / pages_per_hour
hours_per_day = total_reading_hours / days_for_reading
print(int(hours_per_day))
