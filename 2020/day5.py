
def main():
    contents = []
    with open("day5.data",'r') as fs:
        contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    # part1 = solve_part1(contents)
    # print(part1)
    
    row = binary_counter("FBFBBFF", "F", "B")
    column = binary_counter("RLR", "L", "R")
    
    print("Row: {0}, Column: {1}".format(row, column))
    
    print(get_seat_id(row, column))

def get_seat_id(row, column):
    return row * 8 + column


def binary_counter(str, first_half_char, second_half_char):
    power_of = len(str)
    upper_bound = pow(2, power_of) - 1 # I.e. start at max - 1
    lower_bound = 0
    for index, c in enumerate(str):
        if c == first_half_char:
            upper_bound = lower_bound + (int((upper_bound - lower_bound) / 2))  # Round down for the first half
        elif c == second_half_char:
            lower_bound = lower_bound + (int((upper_bound - lower_bound) / 2)) + 1 # Round up for the second half
        else:
            raise "Unexpected character encountered: " + c
        
        if index == len(str) - 1:
            if c == first_half_char:
                return lower_bound
            return upper_bound      # There is no other option the seat has to be the upper bound
            

main()