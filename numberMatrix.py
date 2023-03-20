import math
from screen import Screen


class NumberMatrix:
    def __init__(self, n):
        self.n = n
        self.m = int(math.log(n, 2) + 1)
        self.p = int(math.sqrt(int(n // 2) + 1)) + 1
        self.matrix = [[[0 for x in range(self.p)]
                        for y in range(self.p)]
                       for z in range(self.m)]
        self.available_cells = {i: [(r, c) for r in range(self.p) for c in range(self.p)]
                                for i in range(self.p * 2)}

        for i in range(1, n + 1):
            sf = bin(i)[2:]
            sr = sf[::-1]
            t = 0
            for j in sr:
                if j == "1":
                    r, c = self.available_cells[t].pop(0)
                    self.matrix[t][r][c] = i
                t += 1

    def get_numbers_in_matrix(self, result_label, i):
        numbers = []
        for j in range(len(self.matrix[i])):
            for k in range(len(self.matrix[i][j])):
                if self.matrix[i][j][k] != 0:
                    numbers.append(str(self.matrix[i][j][k]))
        return Screen.show_matrix_on_screen(result_label, self.matrix[i])
