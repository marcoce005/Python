def empty_grid(grid):
    count = 0
    for row in grid:
        count = count + sum(row)
    return count

def distance(x1, y1, x2, y2, grid):
    if grid[y2][x2] == 0:
        return 72
    else:
        return abs((x1 - x2))  + abs((y1 - y2))

def find_next_hop(x, y, grid, coord):
    target = [72, 72]
    new_coord = [item for item in coord]
    for i in range(len(coord)):
        if new_coord[i] == [x, y]:
            break
    new_coord.pop(i)

    distances = []
    set_distances = set()
    for cord in new_coord:
        distances.append(distance(x, y, cord[0], cord[1], grid))
    [set_distances.add(item) for item in distances]
    
    min_x = len(coord)
    min_target_x = len(coord) 
    min_distance = min(distances)
    if len(set_distances) == len(distances):
        for i in range(len(distances)):
            if (distances[i] == min_distance) and (distances[i] != 72):
                target = new_coord[i]
    else:
        for i in range(len(distances)):
            if (distances[i] == min_distance) and (distances[i] != 72):
                if new_coord[i][0] <= min_x:
                    min_x = new_coord[i][0]
                    min_target_x = i
        target = new_coord[min_target_x]
    return target

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def solve_grid(x, y, coord, grid):
    #set current_coord to initial coord
    # current_coord = [coord[0][0], coord[0][1]]
    current_coord = coord[0]
    # decrease max visit for first location
    grid[current_coord[1]][current_coord[0]] -= 1
    total_distance = 0

    #until grid is empty find next hope and calculate total distance
    while empty_grid(grid) >0:
        #find next valid hope
        next_hop = find_next_hop(current_coord[0], current_coord[1], grid, coord)
        if next_hop[0] == 72 and next_hop[1] == 72:
            break
        #calculate distance from current coord to next hop
        total_distance += distance(current_coord[0], current_coord[1], next_hop[0], next_hop[1], grid)
        #decrease max visit for next hop
        grid[next_hop[1]][next_hop[0]] -= 1
        #set new coord
        current_coord = next_hop
    return total_distance

def process_input_file(fname):
    current_line = 0
    with open(fname, "r", encoding='utf8') as f:
        raw_lines = f.readlines()
        lines = [line.strip() for line in raw_lines]
        T = int(lines[0])
        current_line += 1

        with open("output.txt", "w", encoding='utf8') as outf:
            for i in range(T):
                N = int(lines[current_line].split()[0])
                M = int(lines[current_line].split()[1])
                grid = [[0 for i in range(N)] for j in range(N)]
                coord = [[0 for i in range(2)] for j in range(M)]
                current_line += 1
                for j in range(M):
                    X = int(lines[current_line].split()[0])
                    Y = int(lines[current_line].split()[1])
                    V = int(lines[current_line].split()[2])
                    grid[Y][X] = V
                    coord[j] = [X, Y]
                    current_line += 1
                distance = solve_grid(coord[0][0], coord[0][1], coord, grid)
                outf.write("Case #{}: {}".format(i + 1, distance))
                outf.write('\n')

#main

process_input_file("data.txt")
