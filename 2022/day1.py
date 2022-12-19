from read_input import read_input
from typing import List, Any


def app():
    strings = read_input("day1.data")
    sums = []
    current_sum = 0
    for s in strings:
        if s:
            current_sum = int(s) + current_sum
        else:
            sums.append(current_sum)
            current_sum = 0

    sums.append(current_sum)
    print(max(sums))

    # part 2
    sums.sort(reverse=True)
    top_three = sums[0:3]
    print(sum(top_three))


if __name__ == "__main__":
    app()
