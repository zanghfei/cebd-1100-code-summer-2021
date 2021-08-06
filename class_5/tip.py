import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


# values
bill_amount = float(input("bill amount: "))
nr_of_diners = int(input("nr of diners?: "))
fed_tax = float(.0995 * bill_amount)
prov_tax = float(.05 * bill_amount)


# exception if customer did not enter correct value then prompt to enter correct value.
# this exception only work if customer enter value below zero
try:
    tip_amount = float(input("pls enter tip percentage choice: 0,10,15,20 :"))
    assert (tip_amount >= 0), "Pls enter valid value"
except ValueError:
    print("press Ok")
    tip_amount = float(input("pls enter tip percentage choice: 0,10,15,20:"))

# formula and calculations
total_tax = float(fed_tax + prov_tax)
total_bill = float(bill_amount + tip_amount + total_tax)
bill_per_diner = round_down(float(total_bill / nr_of_diners), 2)

# result receipt for customer
print()
print(f"total bill before tax is ${bill_amount:2.2f}")
print(f"tip amount is ${tip_amount:2.2f}")
print(f"fed tax is ${fed_tax:2.2f}")
print(f"prov tax is ${prov_tax:2.2f}")
print(f"total tax is ${total_tax:2.2f}")
print(f"total bill including tax and tip is ${total_bill:2.2f}")

# total bill per diner. how to make this not round off?
# Must round off no matter what, but one person in the group must pay the extra cent.
# If we discard the cent (pay the whole bill minus a cent, delete the last 2 lines).

if nr_of_diners == 1:
    print(f"This single diner must pay, ${total_bill:2.2f}")
else:
    print(f"bill per diner is ${bill_per_diner:2.2f}")
    if bill_per_diner % total_bill != 0:
        print(f"Note:  One of the diners must pay, ${bill_per_diner + 0.01:2.2f}")
