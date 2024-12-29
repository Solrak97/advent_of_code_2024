import copy

guard_map = []

with open("./data/06") as file:

    for row in file:
        guard_map.append(list(row))

walked_map = copy.deepcopy(guard_map)

#find ^
guard_coord = (0,0)

for y in range(len(guard_map)):
    for x in range(len(guard_map[y])):

        if guard_map[y][x] == '^':
            guard_coord = (y, x)
            break




# Siulate the Guard movement
# Can it become a cycle?

def rotate(y, x):
    return (x, -y)

dir_x = 0
dir_y = -1

guard_y, guard_x = guard_coord
next_y, next_x = guard_y, guard_x

while 0 <= next_y < len(walked_map) and 0 <= next_x < len(walked_map[next_y]):
    while walked_map[guard_y + dir_y][guard_x + dir_x] == '#':
        dir_y, dir_x = rotate(dir_y, dir_x)
    
    guard_y += dir_y
    guard_x += dir_x

    walked_map[guard_y][guard_x] = 'X'

    next_y = guard_y + dir_y
    next_x = guard_x + dir_x


for row in walked_map:
    print(''.join(row), end='')