deposit_sum = float(input())
deposit_in_months = int(input())
interest_year = float(input())

interest_payment = deposit_sum * interest_year / 100 / 12
debt = interest_payment * 0.08

final_sum = deposit_sum + deposit_in_months * interest_payment - debt

print(final_sum)
