
def main():
    contents = []
    with open("day5.data",'r') as fs:
        contents = list(map(lambda line: line.strip(), fs.readlines()))
    
    part1 = get_highest_seat_id(contents)
    print(part1)
      

def get_highest_seat_id(input):
    highest_seat_id = -1
    for row in input:
        row_identifier = row[:7]        # The first 7 elements in the array
        column_identifier = row[-3:]    # The last 3 elements in the array
        row = binary_counter(row_identifier, "F", "B")
        column = binary_counter(column_identifier, "L", "R")
        seat_id = get_seat_id(row, column)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
                
    return highest_seat_id



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