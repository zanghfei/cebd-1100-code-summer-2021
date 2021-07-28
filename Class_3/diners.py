while True:
    try:
        num_diners = int(input("How many diners are sharing the cost? >"))
        if num_diners < 0:
            break
        # assert num_diners > 0, "You must enter a positive number."
    except ValueError:
        print("Sorry, the value you entered is not a whole number.")
    except AssertionError:
        print("Sorry you must enter a positive number.")
    else:
        break
