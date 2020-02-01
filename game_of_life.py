import numpy as np
from random import randint

class GoLBoard:
    def __init__(self, initial_state = None):
        if not initial_state:
            self.board = np.random.randint(2, size = (randint(15, 20), randint(15, 20)))
        else:
            self.board = np.matrix(initial_state)
        self.same = False
        self.iterations = 0
        print(self.iterations)
        print(self.board)
        print()

    def update_state(self):
        next_state = np.zeros(self.board.shape, dtype = "int")

        for index, x in np.ndenumerate(self.board):
            neighbors = self.get_neighbors(index[0], index[1])
            if (x and neighbors in [2, 3]) or (not x and neighbors == 3):
                next_state[index] = 1
            else:
                next_state[index] = 0
        self.same = (self.board == next_state).all()
        self.board = next_state
        self.iterations += 1
        print(self.iterations)
        print(self.board)
        print()

    def get_neighbors(self, i, j):
        big_board = self.board
        big_board = np.insert(big_board, [0, big_board.shape[0]], 0, axis = 0)
        big_board = np.insert(big_board, [0, big_board.shape[1]], 0, axis = 1)
        window = big_board[i:i+3, j:j+3]
        window[1,1] = 0
        neighbors = np.sum(window)
        return neighbors

    def run(self):
        while not self.same:
            self.update_state()

if __name__ == "__main__":
    x = GoLBoard()
    x.run()
