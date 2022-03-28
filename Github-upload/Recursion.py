#                                                                              Compund Interest Calculator                           by Robert Smith

# Recursion start on line 51


# The money’s current worth, or present value, is exactly $10,000
# But if you take the money today, you can put it in a savings account and
# earn 2 % interest per year, giving you a total of $11,040 in five years—its future value# and the other will pay you back $1,100 in four years.
present_value = 10000
discount_rate = .02
time = 5
#         To determine future value(formula)
future_value = present_value * (1 + discount_rate) ** time
print(future_value)
#         To determine present value(formula)
# Would you take 1000 today or 1500 in 5 years with a 10 % discount rate
future_value = 1500
discount_rate = .10
time = 5

present_value = future_value / (1 + discount_rate) ** time


#                             Saving Calculator


# If i want a million dollars by the age of 40 (compound interest)
age = 18

retirment_Age = 60

time_until_retirement = retirment_Age - age

Goal = 1000000

return_on_investment = (10 / 100)

initial_investment = Goal / (1 + return_on_investment) ** time_until_retirement

print(
    f'Intially investment of {round(initial_investment)}$ results in {Goal}$ in {time_until_retirement} years.')

# this is how much money intiallly you need to invest
current_amount = 0
monthly_contribution = 2000
months_recurred = 0

return_on_investment_monthly = (10 / 100)/12
# 10% is very common for return on investment(S&P 500)
# return on investment is being added everymonth


def monthly(current_amount, months_recurred):
    if current_amount <= Goal:
        current_amount += current_amount * return_on_investment_monthly
        current_amount += monthly_contribution
        months_recurred += 1
        return monthly(current_amount, months_recurred)
        # recussion is taking place because we is calling the def function monthly
        # the values from (current_amount, months_recurred) have not chnage
        # and will keep running and changing until if statement false

    else:
        return print(f'With an investment of {monthly_contribution}$ a month, you will have {round(current_amount)}$ in {(months_recurred) / 12} years.')
#  divided by 12 so we can get how many years printed out


monthly(current_amount, months_recurred)
