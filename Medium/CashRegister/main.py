def _to_price_repr(dollar_value):
    return round(dollar_value * 100)

def _from_price_repr(change):
    return {k / 100.: v for k, v in change.items()}

def _get_num_denominations_and_remainder(change_needed, denomination):
    num_of_denomination = change_needed // denomination
    remainder = change_needed - (denomination * num_of_denomination)

    return num_of_denomination, remainder

def accumulate_change(change_needed, denominations, accumulator):
    if change_needed <= 0 or len(denominations) == 0:
        return

    if denominations[0] > change_needed:
        accumulate_change(change_needed, denominations[1:], accumulator)
        return
    
    num_of_denomination, remainder = _get_num_denominations_and_remainder(change_needed, denominations[0])

    accumulator[denominations[0]] = num_of_denomination
    accumulate_change(remainder, denominations[1:], accumulator)

def get_change(price, tendered):
    change_required = _to_price_repr(tendered - price)
    denominations = [_to_price_repr(x) for x in [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]]
    change = {}

    accumulate_change(change_required, denominations, change)

    return _from_price_repr(change)

if __name__ == '__main__':
    price = 17.99
    tender = 20.

    change = get_change(price, tender)

    for denomination, amount_required in change.items():
        print(f'${denomination} --> {amount_required}')
