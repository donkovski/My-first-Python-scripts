number_of_pages = int(input())

pages_per_hour = int(input())

days = int(input())

hours_needed_per_day = (number_of_pages / pages_per_hour // days)

print(hours_needed_per_day)