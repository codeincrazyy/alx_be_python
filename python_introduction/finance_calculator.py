print("Enter your monthly income:")
income = int(input())
print("Enter your total monthly expenses:")
expenses = int(input())

savings = income - expenses

projected_saveing = savings * 12 + (savings * 12 * 0.05)

print("your monthly savings are ", savings)

print("projected saving after one year, with interest, is: ", projected_saveing)
