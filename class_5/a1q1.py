PROV_TAX_RATE = 0.09975
FED_TAX_RATE = 0.05


def calculate():

    while True:
        try:
            num_diners = int(input("How many diners are sharing the cost? >"))
            assert num_diners > 0, "You must enter a positive number."
        except ValueError:
            print("Sorry, the value you entered is not a whole number.")
        except AssertionError:
            print("Sorry you must enter a positive number.")
        else:
            break

    while True:
        try:
            meal_cost = float(input("What is the cost of everybody's meal, before tax? >"))
            assert meal_cost > 0, "You must enter a positive number."
        except ValueError:
            print("Sorry, the value you entered is not a number.")
        except AssertionError:
            print("Sorry you must enter a positive number.")
        else:
            break

    prov_tax = meal_cost * PROV_TAX_RATE
    fed_tax = meal_cost * FED_TAX_RATE
    total_inc_tax = meal_cost + prov_tax + fed_tax

    while True:
        tip_percentage = input("How much would you like to tip? [A-Horrible(0%), B-Basic(10%), C-Good (15%), "
                               "D-Exceptional(20)] >")

        if len(tip_percentage) == 1 and tip_percentage.upper() in "ABCD":
            break
        else:
            print("Please enter A, B, C or D.")

    if tip_percentage == "A":
        tip_percentage = 0
    if tip_percentage == "B":
        tip_percentage = .1
    if tip_percentage == "C":
        tip_percentage = .15
    if tip_percentage == "D":
        tip_percentage = .2

    tip_amount = tip_percentage * meal_cost
    total_amount = tip_amount + total_inc_tax
    total_per_person = total_amount / num_diners

    print("*" * 50)
    print("Results of the Calculation")
    print("*" * 50)
    print("The number of diners is          : {:d}".format(num_diners))
    print("The price of the meal before tax : ${:.2f}".format(meal_cost))
    print("The provincial tax added is      : ${:.2f}".format(prov_tax))
    print("The federal tax added is         : ${:.2f}".format(fed_tax))
    print("The total including tax is       : ${:.2f}".format(total_inc_tax))
    print("The tip amount is                : ${:.2f}".format(tip_amount))
    print("GRAND TOTAL                      : ${:.2f}".format(total_amount))
    print("Each person pays                 : ${:.2f}".format(total_per_person))
    print("*" * 50)
    print("Exiting ...")
    exit(0)


if __name__ == '__main__':
    calculate()
