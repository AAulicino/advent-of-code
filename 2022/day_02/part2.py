import os

ENEMY_ROCK = "A"
ENEMY_PAPER = "B"
ENEMY_SCISSORS = "C"

LOSE = "X"
TIE = "Y"
VICTORY = "Z"

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

DEFEAT = 0
DRAW = 3
WIN = 6


def rock_paper_scissors(input):
    rounds = parse_rounds(input)
    totalScore = 0

    for round in rounds:
        totalScore += get_outcome(round)

    return totalScore


def parse_rounds(input):
    rounds = list()

    for line in input:
        rounds.append(tuple(line.rstrip().split(" ")))

    return rounds


def get_outcome(input: tuple[str, str]):
    outcomeMap = {
        (ENEMY_ROCK, TIE): ROCK_SCORE,
        (ENEMY_ROCK, VICTORY): PAPER_SCORE,
        (ENEMY_ROCK, LOSE): SCISSORS_SCORE,
        (ENEMY_PAPER, LOSE): ROCK_SCORE,
        (ENEMY_PAPER, TIE): PAPER_SCORE,
        (ENEMY_PAPER, VICTORY): SCISSORS_SCORE,
        (ENEMY_SCISSORS, VICTORY): ROCK_SCORE,
        (ENEMY_SCISSORS, LOSE): PAPER_SCORE,
        (ENEMY_SCISSORS, TIE): SCISSORS_SCORE,
    }

    scoreMap = {
        VICTORY: WIN,
        TIE: DRAW,
        LOSE: DEFEAT,
    }

    return outcomeMap[input] + scoreMap[input[1]]


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(rock_paper_scissors(f.readlines()))
