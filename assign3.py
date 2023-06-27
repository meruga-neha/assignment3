variable = tuple(map(int,input().split()))
def sum_num(numb):
    total = 0
    for x in numb:
        total += x
    return total
print(sum_num(variable))