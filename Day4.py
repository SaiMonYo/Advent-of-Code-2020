def isValidField(field, value):
    if field == 'byr':
        #checks if 4 digit number
        if len(value) != 4:
            #if not returns false
            return False
        
        num = int(value)
        #returns the bool of if it is within the constraints
        return 1920 <= num <= 2002

    
    if field == 'iyr':
        #same as byr just different ranges for second part
        if len(value) != 4:
            return False
        num = int(value)
        return 2010 <= num <= 2020

    
    if field == 'eyr':
        #same as previous two just different ranges again
        if len(value) != 4:
            return False
        num = int(value)
        return 2020 <= num <= 2030

    
    if field == 'hgt':
        #need two different returns and ranges for inches and cm
        #checking if the height is either cm or in to be valid
        if not value.endswith('in') and not value.endswith('cm'):
            return False
        #getting the numeric value of the height
        num = int(value[:-2])
        #return statement for cm
        if value.endswith('cm'):
            return 150 <= num <= 193
        #return statement for in
        return 59 <= num <= 76

    
    if field == 'hcl':
        #more difficult more validation needed
        #only valid if first char is a #
        if value[0] != '#':
            return False
        #characters that can be used
        validChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        #the all function only returns True if all iterable objects are True
        #so I create a list of the boolean result from going through the chars of value
        #and checking if there in the validChars
        return all([char in validChars for char in value[1:]])

    
    if field == 'ecl':
        #easiest one - return the bool of whether value is in the valid eye colours
        return value in ['amb', 'blu', "brn", 'gry', 'grn', 'hzl', 'oth']

    
    if field == 'pid':
        #another easy one attempt to int value if it doesnt work then its not a valid ID
        try:
            int(value)
            #then it has to be of length 9
            return len(value) == 9
        except:
            return False

#fields that are required cid is commented out as we ignore it
fieldsReq = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    #'cid',
    ]


#opening and splitting the input file into individual passports
passports = open("Day4.txt").read().split("\n\n")

#part 1
#init counter variable
valid = 0
#going through passports
for passport in passports:
    #init counter condition variable
    bad = False
    for field in fieldsReq:
        #if the field we are testing is not in the passport then it is invalid
        if not field in passport:
            bad = True
            break
    #adding 1 if the counter condition is met
    if not bad:
        valid += 1

print(f"{valid} -  part 1")


#part 2
#copied most code from part 1
#wont cover basic parts here look at part 1 for basic explanation
valid = 0
for passport in passports:
    #init 
    bad = False
    for field in fieldsReq:
        if not field in passport:
            bad = True
            break
        #getting the data after the field
        value = passport.split(field + ':')[1].split(' ')[0].split()[0]
        #using isValidField function to check if the passport is good
        if not isValidField(field, value):
            bad = True
            break
    if not bad:
        valid += 1
        
print(f"{valid} - part 2")
