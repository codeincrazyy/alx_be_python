print("Enter your monthly income:")
monthly_income = int(input())
print("Enter your total monthly expenses:")
monthly_expenses = int(input())

monthly_savings = monthly_income - monthly_expenses

projected_saveing = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("your monthly savings are ", monthly_savings)

print("projected saving after one year, with interest, is: ", projected_saveing)
