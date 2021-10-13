class Tile:
    def __init__(self, header, tile):
        self.header = header
        self.tile = tile
        self.edges = self.get_edges()
        self.neighbours = {}

    def get_edges(self):
        # top, bottom, left, right
        # doesnt matter order
        edges = [self.tile[0], self.tile[-1], ''.join([row[0] for row in self.tile]), ''.join(row[-1] for row in self.tile)]
        # get the edges when theyre flipped
        edges += [edge[::-1] for edge in edges]
        return edges

    # sub-routines needed for part 2

    def rotate(self):
        # rotate a 2d array
        self.tile = list((zip(*self.tile[::-1])))
        self.tile = [''.join(row) for row in self.tile]

    def flip(self):
        # flipping 2d array
        self.tile = self.tile[::-1]

    def spec_side(self, side):
        # get specific side
        if side == "left":
            return ''.join([row[0] for row in self.tile])
        if side == "right":
            return ''.join(row[-1] for row in self.tile)
        if side == "top":
            return self.tile[0]
        if side == "bottom":
            return self.tile[-1]

    def order(self, n):
        # all permutations
        if n == 0:
            return
        if n == 1:
            self.rotate()
            return
        if n == 2:
            self.rotate()
            return
        if n == 3:
            self.rotate()
            return
        if n == 4:
            self.flip()
            return
        if n == 5:
            self.rotate()
            return
        if n == 6:
            self.rotate()
            return
        if n == 7:
            self.rotate()
            return
        # something went bad just return and hope for best
        return



def part_1(tiles):
    for key1 in tiles:
        for key2 in tiles:
            if key1 != key2:
                # finding common joining points / borders
                common = [com for com in tiles[key1].edges if com in tiles[key2].edges]
                for com in common:
                    # add the common border to both neighbour dictionaries
                    tiles[key1].neighbours[tiles[key2].header] = com
                    tiles[key2].neighbours[tiles[key1].header] = com
    # set tot to 1 for multiplication
    tot = 1
    for key in tiles:
        # corners only have 2 neighbours
        if len(tiles[key].neighbours) == 2:
            tot *= tiles[key].header
    print(f"Part 1 solution - {tot}")


def match_monster(test, match):
    # used for part 2 to match the row
    for i in range(len(match)):
        if match[i] == "#":
            if test[i] != '#':
                return False
    return True
        
def part_2(tiles):
    # corners:
    # 3121 at index 19
    # 1889 at index 42
    # 1187 at index 50
    # 1789 at index 79
    # this wont work for you lol
    # rotating and flipping one of my edges to be top left
    tiles[3121].flip()
    tiles[3121].rotate()
    tiles[3121].rotate()
    # bft = big tile :)
    bft = [[None for i in range(12)] for j in range(12)]
    # tiles already in the bft
    done = set({3121})
    # setting top left to be the corner
    bft[0][0] = tiles[3121]
    
    # top row
    # fill in the top row
    for x in range(11):
        neighbours = bft[0][x].neighbours
        # match right side of tile already down
        match = bft[0][x].spec_side("right")
        found = False
        # go through neighbours
        for key in neighbours:
            if found:
                break
            if key in done:
                continue
            tile = tiles[key]
            for i in range(8):
                # getting all permutations
                tile.order(i)
                # get left side of tile to compare to left of other tile
                left = tile.spec_side("left")
                if left == match:
                    # add tile to bft
                    bft[0][x + 1] = tile
                    found = True
                    done.add(tile.header)
                    break

    # go down the bft filling it in
    for x in range(12):
        for y in range(0, 11):
            neighbours = bft[y][x].neighbours
            # getting match of bottom of tile already down
            match = bft[y][x].spec_side("bottom")
            found = False
            for key in neighbours:
                if found:
                    break
                if key in done:
                    continue
                tile = tiles[key]
                for i in range(8):
                    # all permutations
                    tile.order(i)
                    # getting top side to match bottom
                    top = tile.spec_side("top")
                    if top == match:
                        bft[y+1][x] = tile
                        found = True
                        done.add(tile.header)
                        break

    # remove borders
    for j in range(12):
        for i in range(12):
            bft[j][i].tile = [row[1:-1] for row in bft[j][i].tile[1:-1]]

    # combining all the tiles to make one big f tile
    new_bft = []
    for k in range(12):
        for j in range(8):
            row = ''
            for i in range(12):
                row += bft[k][i].tile[j]
            new_bft.append(row)
    # making a Tile Object with this new bft
    bft = Tile(1, new_bft)

    # rows of the monster
    monster1 = "..................#."
    monster2 = "#....##....##....###"
    monster3 = ".#..#..#..#..#..#..."
    # number of hashtags in the monster
    n = 15
    # length of one row of the monster
    length = 20
    # total number of hashtags
    total = sum([c.count("#") for c in bft.tile])
    for i in range(8):
        # all permutations of the bft
        bft.order(i)
        count = 0
        for y in range(len(bft.tile)-2):
            for x in range(len(row)-length):
                # first row match
                if match_monster(bft.tile[y][x:x+length], monster1):
                    # second row match
                    if match_monster(bft.tile[y+1][x:x+length], monster2):
                        # third row match
                        if match_monster(bft.tile[y+2][x:x+length], monster3):
                            count += 1
        # monsters only appear in one permutation
        # so if we have atleast 1 we know we have it correct
        if count != 0:
            score = total - n * count
            print(f"Part 2 solution - {score}")
            return

with open("Day20.txt") as file:
    raw_data = file.read().split("\n\n")
    tiles = {}
    for data in raw_data:
        contents = data.split("\n")
        header = int(contents[0].split(" ")[1][:-1])
        contents = contents[1:]
        tile = Tile(header, contents)
        tiles[header] = tile
    part_1(tiles)
    part_2(tiles)
    
