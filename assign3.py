variable = tuple(map(int,input().split()))
def sum_numbers(num):
    total = 0
    for x in num:
        total += x
    return total
print(sum_numbers(variable))
