def main():
    fs = open("day6.data",'r')  
    contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    person_delimiter = "|"
    all_groups = get_all_groups(contents, person_delimiter)
    part1 = sum(map(lambda group: get_unique_question_count(person_delimiter, group), all_groups))
    print(part1)

    part2 = sum(map(lambda group: get_intersection_count(person_delimiter, group), all_groups))
    print(part2)

def get_all_groups(input, person_delimiter):    
    start_new_group = True
    groups = []
    group = ""
    row_count = 0
    for row in input:
        start_new_group = row_count > 0 and row == "" # An empty row starts a new group
        if start_new_group:
            groups.append(group)
            group = row
        else:
            if group != "":                
                group += person_delimiter # Add a marker to indicate a separate person's answers
            group += row

        row_count += 1 
    groups.append(group)
    return groups

def get_unique_question_count(person_delimiter, group):
    return len(set(group.replace(person_delimiter, "")))

def intersection_of_lists(lists):
    head, *tail = map(set, lists)
    return head.intersection(*tail)
    
def get_intersection_count(person_delimiter, group):
    person_answers = group.split(person_delimiter)    # For each person, create an array of all answers    
    return len(intersection_of_lists(person_answers))

main()