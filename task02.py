import random

def get_numbers_ticket(min: int, max: int, quantity:int) -> list:
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
    # 1. Let's check input values
    try:
        assert type(min)==int, f'"min" argument should be of type int, but got "{type(min)}" instead.'
        assert type(max)==int, f'"max" argument should be of type int, but got "{type(max)}" instead.'
        assert type(quantity)==int, f'"quantity" argument should be of type int, but got "{type(quantity)}" instead.'
        assert min>=1, f'"min" value should be 1 or greater.'
        assert max<=1000, f'"max" value should be 1000 or less.'
        assert min<=max, f'"min" value should not be greater than "max" value.'
        assert quantity>=0, f'"quantity" value should not be negative.'
        assert quantity<=max-min+1, f'"quantity" value should not be greater than a pool size of possible values.'
    except AssertionError as e:
        print(f"ERROR: {e}")
        return []
    else:
        # 2. Let's generate values
        chosen_values=random.sample(range(min,max+1),quantity)
        # 3. Let's sort values
        chosen_values.sort()
        return chosen_values
        

