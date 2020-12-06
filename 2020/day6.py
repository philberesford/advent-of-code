def main():
    fs = open("day6.data",'r')  
    contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    part1 = sum(map(get_unique_question_count, get_all_groups(contents)))
    print(part1)




def get_all_groups(input):    
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
            group += row

        row_count += 1 
    groups.append(group)
    return groups



def get_unique_question_count(group):
    return len(set(group))

main()