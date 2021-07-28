# Python Functions

# def print_hello():
#     print("HELLO")
#     print("THANKS")
#
# print_hello()
# print_hello()
# print_hello()

PROV_TAX = 0.09975
FED_TAX = 0.05

def add_fed_tax(price):
    return price * FED_TAX

def add_prov_tax(price):
    return price * PROV_TAX

def add_all_taxes(price):
    return add_fed_tax(price) + add_prov_tax(price)

def add_numbers(a, b):
    result = a + b
    return result


my_result = add_numbers(1, 2)

print(my_result)

print (add_all_taxes(200.00))

