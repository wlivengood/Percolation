import union_find

class Percolation:
    def __init__(self, n):
        self.n = n
        self.grid = [[0]*n for i in range(n)]
        self._uf = union_find.UF(n*n + 2)
        self._top = n*n
        self._bottom = n*n + 1
    def _get_open_neighbors(self, i, j):
        def isValid(i, j):
            return i >= 0 and i < self.n and j >= 0 and j < self.n
        def isAdjacent(x, y, i,j):
            return (x == i) ^ (y == j)
        neighbors = [(x,y) for x in range(i-1, i+2) for y in range(j-1, j+2) if isValid(x,y) and isAdjacent(x,y,i,j)]
        return [neighbor for neighbor in neighbors if self.is_open(neighbor[0],neighbor[1])]
    def open(self, i, j):
        if self.is_open(i, j):
            return
        self.grid[i][j] = 1
        open_neighbors = self._get_open_neighbors(i, j)
        for neighbor in open_neighbors:
            self._uf.union(self._ijTo1D(i,j), self._ijTo1D(neighbor[0],neighbor[1]))
        if i == 0:
            self._uf.union(self._ijTo1D(i,j), self._top)
        if i == self.n - 1:
            self._uf.union(self._ijTo1D(i,j), self._bottom)
    def is_open(self, i, j):
        return self.grid[i][j] == 1
    def is_full(self, i, j):
        return self._uf.connected(self._ijTo1D(i, j), self._top)
    def _ijTo1D(self, i, j):
        return self.n*i + j
    def percolates(self):
        return self._uf.connected(self._top, self._bottom)
