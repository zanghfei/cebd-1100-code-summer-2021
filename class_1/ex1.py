# Exercise 1 - Calculate months and days from year difference.

purchase_year = 2012
current_year = 2021   # We should be using the "Date" function here normally.

year_difference = (current_year - purchase_year)

number_months = year_difference * 12
number_days = year_difference * 365




print("Number of months since purchase " +  str(number_months))
print("Number of days since purchase " + str(number_days))


