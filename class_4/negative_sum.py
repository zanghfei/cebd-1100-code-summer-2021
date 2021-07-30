# Given a list of numbers, return the SUM of the numbers in the list which are NEGATIVE
# If there are no negative numbers, return 0
# example
# values = [-5, -6, 0, 5, 6] -> -11
# values = [5, 6, 7] -> 0

def count_negative_alternate2(input_list):
    alist2 = []
    for x in input_list:
        if x < 0:
            alist2.append(x)
    return sum(alist2)


def count_negative_alternate(a):
    negsum = 0
    for x in range(0, (len(a))):
        if a[x] <= 0:
            negsum = negsum + a[x]
    return negsum


def count_negative(input_list):

    negative_counter = 0

    for val in input_list:
        if val < 0:
            negative_counter += val

    return negative_counter

values = [5, 6, 0, 5, 6]
print(count_negative_alternate2(values))

