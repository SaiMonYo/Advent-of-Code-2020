#part1 = 6506
#part2 = 3243

#my favourite day so far initially did it with jsut sets then remembered it could be easier with sets

#creates an alphabet was in rush - only remembered uppercase A-Z so i did .lower() to turn to lower
alphabet = []
for x in range(65,91):
    alphabet.append(chr(x).lower())


#opening and parsing file into their groups
groups = open("Day6.txt","r").read().split("\n\n")

#part 1

#init total for part 1
totone = 0
#going through all the groups individually
for group in groups:
    #getting all the letters in the group 
    letters = ''.join(set(alphabet).intersection(set(group)))
    #adding the length of it to total for part 1 
    totone += len(letters)

#part 2

#init total for part 2
tottwo = 0
#going through groups individually again
for group in groups:
    #splitting group into individual answers per person
    seperated = group.split("\n")
    #getting letters answered by intersecting the first element by all others in one string
    letters = ''.join(set(seperated[0]).intersection(*seperated))
    #adding the length of that to total for part 2
    tottwo += len(letters)

#outputs
print(f"{totone} - part 1")
print(f"{tottwo} - part 2")

