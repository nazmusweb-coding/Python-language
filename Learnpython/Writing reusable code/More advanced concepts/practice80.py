# None – Exercise

def sum_between(a, b):
    if b < a:
        return None
    else:
        sum = 0
        for i in range(a, b+1): 
            sum += i
        return sum

sum_between(1, 4)