mounth_income = int(input("Enter your monthly income: "))
mounth_expenses = int(input("Enter your total monthly expenses: "))

#Calculate the monthly savings
mounth_savings = mounth_income - mounth_expenses

#Calculate the projected savings after one year, incorporating the interest of 5%
projected_savings = mounth_savings * 12 + (mounth_savings * 12 * 0.05)

print("Your mounthly savings are: ",mounth_savings)
print("Projected savings after one year""," " with interest"","" is: $",projected_savings)