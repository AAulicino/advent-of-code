class Board():
    def __init__(self, id, rows):
        self.id = id
        self.rows = list()

        for row in rows:
            r = list()
            for col in row:
                r.append((col, False))
            self.rows.append(r)

    def mark(self, value):
        for i, row in enumerate(self.rows):
            for j, (cellVal, _) in enumerate(row):
                if cellVal == value:
                    self.rows[i][j] = (cellVal, True)
                    return self.check_if_won_row(i) or self.check_if_won_column(j)

    def check_if_won_row(self, rowIndex):
        for _, match in self.rows[rowIndex]:
            if match == False:
                return False
        return True

    def check_if_won_column(self, colIndex):
        for row in self.rows:
            if row[colIndex][1] == False:
                return False
        return True

    def sum_unmarked(self):
        sum = 0
        for row in self.rows:
            for value, marked in row:
                if marked == False:
                    sum += value
        return sum


def bingo(numbers: list[int], boards: list[Board]):
    toRemove = list()
    for number in numbers:
        for board in list(boards):
            if board.mark(number) == True:
                toRemove.append(board)
                print(
                    f'Winner is at {board.id}. Score: {board.sum_unmarked() * number}')
                boards.remove(board)


with open('input.txt') as f:
    numbers = list(map(int, f.readline().rstrip('\n').split(',')))
    boards = list()

    boardValues = ''
    for line in f.read().split('\n'):
        if line == '':
            if len(boardValues) > 0:
                boards.append(Board(len(boards), boardValues))
            boardValues = list()
            continue

        boardValues.append(map(int, line.split()))

print(bingo(numbers, boards))
