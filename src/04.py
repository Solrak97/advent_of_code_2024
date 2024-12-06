data = []

with open("data/04") as file:
    for line in file:
        data.append(line)


datas = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]

width = len(data)
length = len(data[0])



pos_list = [(-1,1), (0, 1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1, -1)]

def get_word(x, y, pos):

    word = ""
    _x, _y = x, y
    i, j = pos

    for k in range(4):
        
        if (0 <= _x < width ) and (0 <= _y < length):
            word += data[_x][_y]

            _x += i
            _y += j

        else:
            break

    return word




xmas_ctr = 0

for x in range(width):
    for y in range(length):

        if data[x][y] == 'X':
            for pos in pos_list:
                word = get_word(x, y, pos)
                
                if word == "XMAS":
                    xmas_ctr += 1


print(xmas_ctr)



# part II with a different approach
x_pos = [(0,0), (2,2), (1,1), (0,2), (2,0)]
ctr = 0

for x in range(width):
    for y in range(length):

        if x + 2 < width and y + 2 < length:
            x_blocks_p = [(x + i, y + j) for i, j in x_pos]
            x_blocks = [data[x + i][y + j] for i, j in x_pos]
            
            if x_blocks[2] == "A" and {x_blocks[0], x_blocks[1]} == {x_blocks[3], x_blocks[4]} and {x_blocks[3], x_blocks[4]} == {"M", "S"}:
                ctr += 1


print(ctr)