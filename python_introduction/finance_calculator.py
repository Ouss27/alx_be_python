monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

#Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

#Calculate the projected savings after one year, incorporating the interest of 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your mounthly savings are: ",monthly_savings)
print("Projected savings after one year""," " with interest"","" is: $",projected_savings)