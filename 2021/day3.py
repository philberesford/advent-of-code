from read_input import read_input
from typing import List, Any

def app():
        input = read_input("day3.data")
        transposed = transpose(input)
        ints = [list(map(int, list_of_strings)) for list_of_strings in transposed]
        most_common = [most_common_bit(int_list) for int_list in ints]
        least_common = [least_common_bit(int_list) for int_list in ints]

        gamma = binary_list_to_int(most_common)
        epsilon = binary_list_to_int(least_common)
        part1 = gamma * epsilon
        print(part1)


def binary_list_to_int(list_of_ints):
    return int("".join(list(map(str, list_of_ints))), 2)


def most_common_bit(list_of_ints):
    count_of_ones = sum(list_of_ints)
    count_of_zeros = len(list_of_ints) - count_of_ones
    return 1 if count_of_ones > count_of_zeros else 0


def least_common_bit(list_of_ints):
    return 0 if most_common_bit(list_of_ints) == 1 else 1

def transpose(list_of_lists: List[Any]):
    return [list(i) for i in zip(*list_of_lists)]

if __name__ == "__main__":
   app()