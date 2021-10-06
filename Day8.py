def part_1(lines):
    # lookup O(1)
    visited = set()
    # current index
    index = 0
    accumulator = 0
    # already run that operation
    while index not in visited:
        visited.add(index)
        command = lines[index]
        # using it twice saves time
        space = command.index(" ")
        value = int(command[space:])
        command = command[:space]
        if command == "acc":
            accumulator = accumulator + value
            index = index + 1
        elif command == "jmp":
            index = index + value
        # could use else
        elif command == "nop":
            index = index + 1
    print(f"Part 1 solution - {accumulator}")
        

def part_2_helper(lines):
    # same as part 1 but with a return
    # if index out of range
    
    # lookup O(1)
    visited = set()
    # current index
    index = 0
    accumulator = 0
    # already run that operation
    while index not in visited:
        if index >= len(lines):
            return accumulator
        visited.add(index)
        command = lines[index]
        # using it twice saves time
        space = command.index(" ")
        value = int(command[space:])
        command = command[:space]
        if command == "acc":
            accumulator = accumulator + value
            index = index + 1
        elif command == "jmp":
            index = index + value
        # could use else
        elif command == "nop":
            index = index + 1
    # infinite loop
    return False


def part_2(lines):
    for i in range(len(lines)):
        if "jmp" in lines[i]:
            # swapping jmp to nop
            lines[i] = lines[i].replace("jmp", "nop")
            result = part_2_helper(lines)
            if result:
                print(f"Part 2 solution - {result}")
                return
            # changing back if not correct
            lines[i] = lines[i].replace("nop", "jmp")
        else:
            # swapping nop for jmp
            if "nop" in lines[i]:
                lines[i] = lines[i].replace("nop", "jmp")
                result = part_2_helper(lines)
                if result:
                    print(f"Part 2 solution - {result}")
                    return
                # swapping back if not correct
                lines[i] = lines[i].replace("jmp", "nop")


if __name__ == "__main__":
    with open("Day8.txt") as file:
        lines = file.read().split("\n")

    part_1(lines)
    part_2(lines)


