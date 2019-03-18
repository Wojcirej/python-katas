def find_parity_outlier(integers):
    parities = [num % 2 for num in integers]
    loc = parities.index(ifeven(integers))
    return integers[loc]

def ifeven(list):
    return sum(n % 2 for n in list[:3]) <= 1
