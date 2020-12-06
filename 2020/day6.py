def main():
    fs = open("day6.data",'r')  
    contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    person_delimiter = "|"
    part1 = sum(map(lambda group: get_unique_question_count(person_delimiter, group), get_all_groups(contents, person_delimiter)))
    print(part1)

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
            group += person_delimiter + row # Add a marker to indicate a separate person's answers

        row_count += 1 
    groups.append(group)
    return groups

def get_unique_question_count(person_delimiter, group):
    return len(set(group.replace(person_delimiter, "")))

main()