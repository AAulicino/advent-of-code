import os

ENEMY_ROCK = "A"
ENEMY_PAPER = "B"
ENEMY_SCISSORS = "C"

SELF_ROCK = "X"
SELF_PAPER = "Y"
SELF_SCISSORS = "Z"

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
        (ENEMY_ROCK, SELF_ROCK): DRAW,
        (ENEMY_ROCK, SELF_PAPER): WIN,
        (ENEMY_ROCK, SELF_SCISSORS): DEFEAT,
        (ENEMY_PAPER, SELF_ROCK): DEFEAT,
        (ENEMY_PAPER, SELF_PAPER): DRAW,
        (ENEMY_PAPER, SELF_SCISSORS): WIN,
        (ENEMY_SCISSORS, SELF_ROCK): WIN,
        (ENEMY_SCISSORS, SELF_PAPER): DEFEAT,
        (ENEMY_SCISSORS, SELF_SCISSORS): DRAW,
    }

    scoreMap = {
        SELF_ROCK: ROCK_SCORE,
        SELF_PAPER: PAPER_SCORE,
        SELF_SCISSORS: SCISSORS_SCORE,
    }

    return outcomeMap[input] + scoreMap[input[1]]


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(rock_paper_scissors(f.readlines()))
