import random

def get_numbers_ticket(min: int, max: int, quantity:int) -> list[int]:
    """
    Generate a sorted list of unique random numbers within given boundaries

    Returns empty list in case of wrong arguments.

    Parameters:
        min (int): minimum possible number in set, >=1
        max (int): maximum possible number in set, <=1000
        quantity (int): number of unique numbers to produce

    Returns:
        list[int]: list of numbers from range
    """
    
    chosen_values = []

    # 1. Let's check input values
    if type(min) != int:
        print(f'ERROR: "min" argument should be of type int, but got "{type(min)}" instead.')
    elif type(max) != int:
        print(f'ERROR: "max" argument should be of type int, but got "{type(max)}" instead.')
    elif type(quantity) != int:
        print(f'ERROR: "quantity" argument should be of type int, but got "{type(quantity)}" instead.')
    elif min < 1:
        print(f'ERROR: "min" value should be 1 or greater.')
    elif max > 1000:
        print(f'ERROR: "max" value should be 1000 or less.')
    elif min > max:
        print(f'ERROR: "min" value should not be greater than "max" value.')
    elif quantity < 0:
        print(f'ERROR: "quantity" value should not be negative.')
    elif quantity > (max - min + 1):
        print(f'ERROR: "quantity" value should not be greater than a pool size of possible values.')
    else:
        # 2. Let's generate values
        chosen_values = random.sample(range(min, max + 1), quantity)
        # 3. Let's sort values
        chosen_values.sort()
    
    return chosen_values

