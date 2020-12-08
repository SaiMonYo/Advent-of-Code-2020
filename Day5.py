#super easy day today
#initially thought I had to make a binary search
#then realised its just a binary number

#part 1
#getting data from the file
boardingPasses = open('Day5.txt','r').read()
#converts F and L to 0 , B and R to 1 through out the entire string of boardingPasses
binaryPasses = boardingPasses.translate(str.maketrans('FBLR', '0101'))
#creates a list of all denary lines in the boardingPasses
#it does this by going through the binaryPasses which are split into their lines
#converting the line to decimal or denary from binary - int(line,2) the 2 signifies it is in base 2 (binary)
ids = [int(line, 2) for line in binaryPasses.splitlines()]

print(f"{max(ids)} - part 1")


#part 2
for i in ids:
    #checks if the next seat is not in the the list but the one after that is in
    #in other words checks if the seat after the current id we are checking is my seat
    if i + 1 not in ids and i + 2 in ids:
        print(f"{i + 1} - part 2")
