def make_visited_array(map):
    visits = []
    for row in map:
        visits.append([False] * len(row))
    return visits

def mark_visited(visits, i: int, j: int) -> None:
    visits[i][j] = True

def is_visited(visits, i: int, j: int) -> bool:
    return visits[i][j]

def is_island(map, visits, i: int, j: int) -> bool:
    if i >= len(map) or j >= len(map[i]):
        return False

    isisland = map[i][j] == 1
    mark_visited(visits, i, j)

    if isisland:
        is_island(map, visits, i, j + 1)
        is_island(map, visits, i + 1, j)

    return isisland

def get_num_islands(map) -> int:
    num_islands = 0
    visits = make_visited_array(map)

    for i in range(len(map)):
        for j in range(len(map[i])):
            if is_visited(visits, i, j):
                continue

            if is_island(map, visits, i, j):
                num_islands += 1
    
    return num_islands


if __name__ == '__main__':
    map = [
        [1,1,1,1,1,0,0,0,0,0],
        [1,1,1,0,1,0,0,0,0,0],
        [1,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    num_islands = get_num_islands(map)
    print(num_islands)
