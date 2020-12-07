#part 1 = 6506
#part 2 = 3243
alphabet = []
for x in range(65,91):
    alphabet.append(chr(x).lower())


data = open("Day6.txt","r").read()

groups = data.split("\n\n")


tot = 0
for group in groups:
    seperated = group.split("\n")
    for sep in seperated:
        letters = ''.join(set(alphabet).intersection(set(sep)))
    x = len(letters)
    tot += len(letters)

print(tot)

