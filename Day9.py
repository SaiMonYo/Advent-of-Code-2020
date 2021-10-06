def part_1(lines):
    previous = []
    for line in lines:
        # starting the list of 25
        if len(previous) < 25:
            previous.append(line)
        else:
            found = False
            # checking if two numbers add to make current
            for number in previous:
                if line - number in previous:
                    found = True
                    break
            if not found:
                return line
            # moving list over one
            previous.pop(0)
            previous.append(line)


def part_2(lines):
    goal = part_1(lines)
    for i in range(len(lines)-1):
        # quicker to have total than use sum()
        total = lines[i]
        tally = [total]
        for j in range(i+1, len(lines)):
            tally.append(lines[j])
            total = total + lines[j]
            # we have atleast 2 in a row
            if total == goal:
                return min(tally) + max(tally)
            # stopping O(n^2) run time
            # more like O(nlogn) I think
            elif total > goal:
                break
    return "hmm not working"

# input processing
with open("Day9.txt") as file:
    lines = file.read().split("\n")
    lines = [int(line) for line in lines]

print(f"Part 1 Solution - {part_1(lines)}")
print(f"Part 2 Solution - {part_2(lines)}")
