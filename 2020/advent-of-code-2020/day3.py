def main():
    fs = open("day3.data",'r')  
    contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    part1 = slope_solver(contents, 3, 1)
    print(part1)
    
    r1d1 = slope_solver(contents, 1, 1)
    r3d1 = slope_solver(contents, 3, 1)
    r5d1 = slope_solver(contents, 5, 1)
    r7d1 = slope_solver(contents, 7, 1)
    r1d2 = slope_solver(contents, 1, 2, True)

    part2 = r1d1 * r3d1 * r5d1 * r7d1 * r1d2
    print(part2)

def slope_solver(input, right, down, print_rows=False):
    x = 0
    y = -1
    first = True
    trees = 0
    for row in input:
        y += 1

        process_row = y % down == 0
        if process_row:         
            if not first:
                x += right
            if x >= len(row):       # the current position is greater than the width of the map
                x = x - len(row)    # start again from the beginning of the current row
  
            if row[x] == "#":
                trees += 1

            row = replace_str_at(row, x, "O")       

        if print_rows:
            print(row)

        if first:               # It's the first time through the loop
            first = False
            
    return trees

def replace_str_at(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

main()