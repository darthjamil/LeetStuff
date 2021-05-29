import math


def get_best_block(blocks, requirements):
    '''
    :param `blocks`: An array of city blocks, each containing a map indicating whether
    a facility is present on that block or not. Ex:
    [
        {'gym': False, 'school': True, 'store': False,},
        {'gym': True, 'school': False, 'store': False,},
        {'gym': True, 'school': True, 'store': False,},
        {'gym': False, 'school': True, 'store': False,},
        {'gym': False, 'school': True, 'store': True,},
    ]

    :param `requirements`: An array of required facilities. The names match the
    keys of the block facilities. Ex:
    ['gym', 'school', 'store']

    :returns: The index of the city block that minimizes the distance to all the 
    required facilities. Ex:
    2, 3, or 4 are all valid answers, because they each minimize total distance for 
    all required facilities to 2 blocks.

    O(n^2 x m) where n is the number of blocks and m is the number of required
    facilities.
    '''
    distances = [get_requirement_distances_from_block(blocks, requirements, i) for i, _ in enumerate(blocks)]
    distance_sums = get_sums(distances)
    min_distance_block = get_index_of_min(distance_sums)

    return min_distance_block


def get_requirement_distances_from_block(blocks, requirements, current_block):
    '''
    :param `blocks`: An array of blocks, each containing a map indicating whether
    a facility is present on that block or not. Ex:
    [
        {'gym': False, 'school': True, 'store': False,},
        {'gym': True, 'school': False, 'store': False,},
        {'gym': True, 'school': True, 'store': False,},
        {'gym': False, 'school': True, 'store': False,},
        {'gym': False, 'school': True, 'store': True,},
    ]

    :param `requirements`: An array of required facilities. The names matchs the
    keys of the block facilities. Ex:
    ['gym', 'school', 'store']

    :param `current_block`: The index of the current block in the blocks array.
    Ex: 2

    :returns: A map of facilities --> the min distance to that facility from the
    current_block. Ex.
    {'gym': 0, 'school': 0, 'Store': 2,}
    '''
    facilities = { facility: math.inf for facility in requirements }

    for i, block in enumerate(blocks):
        distance = abs(i - current_block)

        for f in requirements:
            if block.get(f) and facilities[f] > distance:
                facilities[f] = distance
    
    return facilities


def get_sums(distances):
    '''
    :param `distances`: An array of blocks, each containing the distance to the nearest
    facility for a specific set of facilities. Ex.
    [
        {'gym': 1, 'school': 0, 'Store': 4,},
        {'gym': 0, 'school': 1, 'Store': 3,},
        {'gym': 0, 'school': 0, 'Store': 2,},
        {'gym': 1, 'school': 0, 'Store': 1,},
        {'gym': 2, 'school': 0, 'Store': 0,},
    ]

    :returns: An array of blocks, each containing the total distance to all specified
    facilities. Ex:
    [5, 4, 2, 2, 2]
    '''
    return [sum(block.values()) for block in distances]


def get_index_of_min(list):
    '''
    :returns: The index of the minimum element of the int array. Ex:
    [5, 4, 2, 2, 2] --> 2 or 3 or 4
    '''
    return list.index(min(list))


if __name__ == "__main__":
    blocks = [
        {'gym': False, 'school': True, 'store': False,},
        {'gym': True, 'school': False, 'store': False,},
        {'gym': True, 'school': True, 'store': False,},
        {'gym': False, 'school': True, 'store': False,},
        {'gym': False, 'school': True, 'store': True,},
    ]

    requirements = ['gym', 'school', 'store']

    best_block = get_best_block(blocks, requirements)
    print(best_block)
