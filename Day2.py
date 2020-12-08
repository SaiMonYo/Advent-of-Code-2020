#part1 = 410
#part2 = 694

import re

#opening file and striping it of "\n"
lines = open("Day2.txt").readlines()
for x in range(len(lines)):
    lines[x] = lines[x].strip()

#part 1
    
#init counter variable
count = 0
#going through passwords
for line in lines:
    #splitting the line into seperate components
    mininum, maximum, c, password = re.split('-| |: ', line)
    #checking if number of characters (c) is between the two points (e.g. 2-9)
    if int(mininum) <= password.count(c) and password.count(c) <= int(maximum):
        #adding one to counter variable
        count += 1

#outputting part 2
print(f"part one: {count}")

#part 2

#init counter variable
count = 0
#going through the lines
for line in lines:
    #splitting the line into seperate components
    pos_one, pos_two, c, password = re.split('-| |: ', line)
    #checking if at one position and not the other
    if (password[int(pos_one)-1] == c and password[int(pos_two)-1] != c) or (password[int(pos_one)-1] != c and password[int(pos_two)-1] == c):
        #adding one to conter variable
        count += 1

#outputting part 2
print(f"part Two: {count}")
