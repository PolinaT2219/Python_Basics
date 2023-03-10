pages_count = int(input())
pages_per_hour = int(input())
days = int(input())

time_needed = pages_count // pages_per_hour
time_per_day = time_needed / days

print(time_per_day)