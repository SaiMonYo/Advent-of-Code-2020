def part_1(recipes):
    all_items = {}
    # adds all items/ingredients that could cause
    # said allergy
    for line in recipes:
        # list unpacking
        items, allergens = line
        for allergen in allergens:
            # create new item
            if allergen not in all_items:
                all_items[allergen] = items
            # add these items to the dict
            else:
                all_items[allergen] = all_items[allergen][:] + items

    # removes duplicates
    for key in all_items:
        no_dup = list(set(all_items[key]))
        all_items[key] = no_dup

    # removes ones it cant be
    # by deleting ingredients not in all of the recipes
    # with that allergy
    for key in all_items:
        for line in recipes:
            # list unpacking
            items, allergens = line
            if key in allergens:
                for item in all_items[key]:
                    if item not in items:
                        # removing that item
                        curr = all_items[key][:]
                        curr.remove(item)
                        all_items[key] = curr

    #calling part 2 here so we dont have to parse everything again
    part_2(all_items)
    # all the ones that could cause allergies
    causes_allergy = []
    for value in all_items.values():
        causes_allergy += value
    # casting to set to increase lookup speed
    causes_allergy = set(causes_allergy)

    # counting the number of items that dont cause allergies
    count = 0
    for line in recipes:
        items, allergens = line
        for item in items:
            if item not in causes_allergy:
                count += 1
    print(f"Part 1 solution - {count}")


def sort_dict(dic):
    '''returns a dictionary sorted by length of values'''
    # sorts the keys
    keys = sorted(dic, key = lambda item: len(dic[item]))
    # creates the dictionary
    ordered = {}
    for key in keys:
        value = dic[key]
        ordered[key] = value
    return ordered
    
def part_2(causes):
    # while any of the values are not 1
    while any(len(value) != 1 for value in causes.values()):
        # sort the dict
        causes = sort_dict(causes)
        for key in causes:
            # if theres only one ingredient causing allergy
            if len(causes[key]) == 1:
                item = causes[key][0]
                # we remove that ingredient from all other recipes
                for key2 in causes:
                    # make sure were not removing from its own key
                    if key2 != key:
                        items = causes[key2]
                        # checking if its in
                        if item in items:
                            # removing
                            items.remove(item)
    
    # create the canonacolly dangerous ingredient list
    keys = sorted(causes)
    candangerous = []
    for key in keys:
        candangerous += causes[key]
    print(f"Part 2 solution - {','.join(candangerous)}")


with open("Day21.txt") as file:
    # raw data
    rdata = file.read().split("\n")
    recipes = []
    for line in rdata:
        # parsing data
        items, allergens = line.split(" (")
        items = items.split(" ")
        allergens = allergens[:-1].replace("contains ", "").split(", ")
        recipes.append((items, allergens))
    # part 2 is called in this fucntion
    part_1(recipes)


# example
'''
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
{'dairy': ['mxmxvkd'], 'fish': ['sqjhc', 'mxmxvkd'], 'soy': ['sqjhc', 'fvjkl']}
'''