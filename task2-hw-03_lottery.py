import random

def get_numbers_ticket(min,max,quantity):
    range = []
    i= min
    while i <= max:
        range.append(i)
        i = i + 1
    print(range)
    result = random.sample(range,quantity)
    result.sort()
    return  result


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
