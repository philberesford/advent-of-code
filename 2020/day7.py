def main():
    with open("day7.data",'r') as fs:
        contents = list(map(lambda line: line.strip(), fs.readlines()))

    bags = get_all(contents)
    
    counter = 0
    part1 = len(find_in("shiny gold", bags))
    print(part1)

def find_in(search_for, bags, searched = []): 
    results = []

    if searched.count(search_for) > 0:
        return results
    
    searched.append(search_for)

    for key, contained_bags in bags.items():
        if contains_bag(search_for, contained_bags):
            results.append(key)

    for parent in results:
        for ancestor in find_in(parent, bags, searched):
            results.append(ancestor)

    return list(set(results))   # Only return the unique values


def contains_bag(search_for, possible_bags):
    return possible_bags.count(search_for) > 0

def get_all(input): 
    bags = {}
    for index, row in enumerate(input):        
        outer = row.split(" contain ")[0].replace("bags", "").strip()
        inner = list(map(lambda bags_string: bags_string.replace("bags", "").replace("bag", "").replace(".", "").strip(), row.split(" contain ")[1].split(","))) 
        inner = list(map(lambda bag_string: str(bag_string[1:]).strip() , inner)) # Chop off the amounts - they're not needed now.
        if inner[0] == "no other":
            inner = []

        bags[outer] = inner    
    return bags


main()