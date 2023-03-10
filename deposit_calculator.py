deposit_sum = float(input())
months = int(input())
interest_rate = float(input())

interest = deposit_sum * (interest_rate/100)
interest_per_month = interest/12

total_sum = deposit_sum + months * interest_per_month
print(total_sum)