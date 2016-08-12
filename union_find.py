# weighted quick-union with path compression

class UF:
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1]*n
    def _root(self, i):
        while self._id[i] != i:
            self._id[i] = self._id[self._id[i]]
            i = self._id[i]
        return i
    def connected(self, p, q):
        return self._root(p) == self._root(q)
    def union(self, p, q):
        p_root = self._root(p)
        q_root = self._root(q)
        if p_root == q_root:
            return
        if self._sz[p_root] < self._sz[q_root]:
            self._id[p_root] = self._id[q_root]
            self._sz[q_root] += self._sz[p_root]
        else:
            self._id[q_root] = self._id[p_root]
            self._sz[p_root] += self._sz[q_root]
