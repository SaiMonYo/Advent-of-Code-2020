#part1 = 539851
#part2 = 212481360

#getting numbers from input and turning them to integers
numbers = open("Day1.txt").readlines()
for x in range(len(numbers)):
    numbers[x] = int(numbers[x])

#getting length of the input to avoid exessive len()
length = len(numbers)


#sorts list so we can divide and conquer
#quicker than linear search
numbers.sort()

#Part 1

#going through numbers
for num in numbers:
    #checking if two numbers sum to 2020
    if 2020 - num in numbers:
        #outputing product of the 2 numbers
        print(f"{num * (2020 - num)} - part 1")
        #breaking once found to avoid double output
        break

#Part 2

#init found to be false so we can change it once found to break out of loop
found = False
#going through numbers
for num in numbers:
    #going through numbers again in order to determine the 3 numbers
    for number in numbers:
        #checking if the total 2020 - num - number is in the list numbers
        #in other words if 3 numbers sum to 2020
        if (2020 - num - number) in numbers:
            #outputting product
            print(f"{num * number * (2020 - num - number)} - part 2")
            #changing found to break out of the containing loop
            found = True
            #breaking out of this loop
            break
    #breaking out of first loop if the three numbers are found
    if found:
        break
