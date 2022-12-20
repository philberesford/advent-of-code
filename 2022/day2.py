from read_input import read_input
from typing import List, Any


def app():
    strings = read_input("day2.data")
    games = [string.split(" ") for string in strings]
    scores = [score(game) for game in games]

    print(scores)
    print(sum(scores))
    print(len(scores))


def score(game: List[str]):
    win_score = 6
    draw_score = 3
    lose_score = 0

    rock_score = 1
    paper_score = 2
    scissors_score = 3

    rock = "ROCK"
    paper = "PAPER"
    scissors = "SCISSORS"

    me = rock if is_rock(game[1]) else scissors if is_scissors(game[1]) else paper
    opponent = rock if is_rock(game[0]) else scissors if is_scissors(game[0]) else paper

    scores = {
        rock + rock: draw_score + rock_score,
        paper + rock: win_score + paper_score,
        scissors + rock: lose_score + scissors_score,

        rock + paper: lose_score + rock_score,
        paper + paper: draw_score + paper_score,
        scissors + paper: win_score + scissors_score,

        rock + scissors: win_score + rock_score,
        paper + scissors: lose_score + paper_score,
        scissors + scissors: draw_score + scissors_score,
    }

    return scores.get(me + opponent)


def is_rock(val: str):
    return val in ["A", "X"]


def is_paper(val: str):
    return val in ["B", "Y"]


def is_scissors(val: str):
    return val in ["C", "Z"]


if __name__ == "__main__":
    app()
