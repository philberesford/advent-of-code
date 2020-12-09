def main():
    with open("day9.data",'r') as fs:
        input = list(map(lambda line: line.strip(), fs.readlines()))

    part1 = get_number_that_is_not_in_preceding_pair_sums(25, input)
    print("The number is: {}".format(part1))

def get_number_that_is_not_in_preceding_pair_sums(preamble_size, input):
    numbers = list(map(int, input))
    for i in range(preamble_size, len(input)):
        num = numbers[i]
        preamble = numbers[i-preamble_size:i]           # Get the preceeding n numbers 
        if not num in create_sum_of_pairs(preamble):
            return num
    
def create_sum_of_pairs(set):
    pairs = []
    for x in set:
        for y in set:
            if x != y:
                pairs.append([x, y])
    
    pair_sums = list(map(sum, pairs))
    return pair_sums

# def create_sets_of_n_numbers(size, input):
#     numbers = list(map(int, input))
#     result = []
#     for i in range(0, len(input)-size+1):        
#         set = numbers[i:i+size]
#         result.append(set)
#     return result

main()