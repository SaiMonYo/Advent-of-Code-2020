#part1 = 268
#part2 = 3093068400

#opening the input file and reading the lines
lines = open("Day3.txt").readlines()

#function for counting
def counttrees(right, down):
    #starting position
    pos = 0
    #counting variable for trees
    trees = 0
    #count variable for down
    c = 0
    #goes through the lines
    for line in lines:
        #goes down the slope downwards gradient
        if c % down == 0:
            #stripping line
            line = line.strip()
            #checking if the location is a tree
            if line[pos] == '#':
                trees += 1
            #getting new position
            pos = (pos + right) % len(line)
        c += 1
    
    return trees

#directions of the slopes
directions = [(1,1),(5,1),(7,1),(1,2),(3,1)]

#part 1
print(f"{counttrees(3,1)} - part 1" )

#part 2
#goes through the directions for part 2
tot = 1
for d in directions:
    tot *= counttrees(d[0],d[1])
print(f"{tot} - part 2")
