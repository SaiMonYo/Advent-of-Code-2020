# directions to get to neighbouring hexagons
directions = {
    "e": (2, 0),
    "se": (1, -2),
    "sw": (-1, -2),
    "w": (-2, 0),
    "nw": (-1, 2),
    "ne": (1, 2)
    }


def part_1(lines):
    blacks = set()
    for line in lines:
        # start at origin
        x, y = 0, 0
        while len(line) > 0:
            # test all directions
            for direction in directions:
                # the next direction is in dictionary
                if line.startswith(direction):
                    # getting move vector
                    move = directions[direction]
                    # changing our location based on direction
                    x, y = x + move[0], y + move[1]
                    # remove the direction we just used
                    line = line[len(direction):]
                    # break out of direction checking
                    break
        # flipping the tile
        if (x,y) in blacks:
            blacks.remove((x,y))
        else:
            blacks.add((x,y))
    # amount of black tiles
    print(f"Part 1 solution - {len(blacks)}")
    part_2(blacks)


def part_2(blacks):
    for _ in range(100):
        # two lists to simultaneously change the tiles
        new_blacks = []
        remove_blacks = []
        # go through blacks
        for x, y in blacks:
            neighbours = 0
            # go through neighbours
            for move in directions.values():
                testx, testy = x + move[0], y + move[1]
                if (testx, testy) in blacks:
                    neighbours += 1
                else:
                    # its a white tile so we
                    # need to check if it has 2 neighbours which are black
                    count = 0
                    for direc in directions.values():
                        tx, ty = testx + direc[0], testy + direc[1]
                        if (tx, ty) in blacks:
                            count += 1
                    # black is created
                    if count == 2:
                        new_blacks.append((testx, testy))
            # black is removed
            if neighbours == 0 or neighbours > 2:
                remove_blacks.append((x, y))
        # remove or add needed
        for black in new_blacks:
            blacks.add(black)
        for black in remove_blacks:
            blacks.remove(black)
    # amount of black tiles
    print(f"Part 2 solution - {len(blacks)}")
                

with open("Day24.txt") as file:
    lines = file.read().split("\n")
    part_1(lines)
