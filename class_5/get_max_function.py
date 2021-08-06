def get_max(n1, n2, n3):
    if n2 > n1 and n2 > n3:
        return n2
    if n3 > n2:
        return n3
    return n1

def get_max_alternate(n1, n2, n3):
    numlist = [n1, n2, n3]
    numlist.sort()
    #numlist.reverse()
    return numlist[-1]

def get_max_alternate2(num_list):
    num_list.sort()
    return num_list[-1]

b = get_max(1, 2, 3)

print(str(b))

def abc(*args):
    return(list(args))

print(abc(1,2,3,4))


