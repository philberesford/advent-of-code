from read_input import read_input
from typing import List, Any
import re
MARKED = "*"

def app():
        input = read_input("day4.data")
        print(get_part1(input))

def get_part1(input: List[str]) -> int:
    called_numbers = input[0].split(",")
    boards = get_boards(input)

    for number in called_numbers:
        for board in boards:
            board = mark_number_in(number, board)
            if has_winner(board):
                total = get_total(board)
                return total * int(number)


def get_total(board: List[List[str]]) -> int:
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != MARKED:
                total += int(board[i][j])

    return total


def get_boards(input: List[str]) -> List[List[List[str]]]:
    boards = []
    counter = 2
    while counter < len(input) - 1:
        boards.append(get_board(counter, input))
        counter += 6

    return boards


def get_board(start_at: int, input: List[str]) -> List[List[str]]:
    return [re.split(r"\s+", input[line_number]) for line_number in range(start_at, start_at+5)]


def mark_number_in(number: str, board: List[List[str]]) -> List[List[str]]:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                board[i][j] = MARKED

    return board


def has_winner(board: List[List[str]]) -> bool:
    for row in board:
        if is_winning_set(row):
            return True

    for column in transpose(board):
        if is_winning_set(column):
            return True

    return False


def is_winning_set(row: List[str]):
    return all(map(lambda entry: entry == MARKED, row))


def transpose(list_of_lists: List[Any]):
    return [list(i) for i in zip(*list_of_lists)]

if __name__ == "__main__":
   app()