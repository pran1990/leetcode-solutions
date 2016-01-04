from datetime import datetime
import sys
import math



class Solution(object):
    def __init__(self):
        self.storage = None
        self.squares = None


    def fill_squares(self, n):
        a = int(math.sqrt(n))
        self.squares = [(x+1)**2 for x in range(int(math.sqrt(n)))]

    def fill_storage(self, n):
        self.storage = [sys.maxint for i in range(n+1)]
        self.storage[0] = 0
        for i in self.squares:
            self.storage[i] = 1

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.fill_squares(n)
        self.fill_storage(n)
        self._another_squares_helper(n)
        return self.storage[n]

    def _squares_helper(self, n):
        if self.storage[n] != sys.maxint:
            return self.storage[n]

        values_to_compare = []
        for i in self.squares:
            if n-i > 0:
                values_to_compare.append(self._squares_helper(n-i))
    
        self.storage[n] = min(values_to_compare) + 1
        return self.storage[n]

    def _another_squares_helper(self, n):
        for i in range(n+1)[1:]:
            if self.storage[i] == sys.maxint:
                values_to_compare = []
                for j in self.squares:
                    if i-j > 0:
                        values_to_compare.append(self.storage[i-j])
                self.storage[i] = min(values_to_compare) + 1
                



x = Solution()
problems = [1, 12, 13, 132, 9732, 6255, 8285, 5238]
#problems = [13]
for n in problems:
    t1 = datetime.now()
    ans = x.numSquares(n)
    t2 = datetime.now()
    delta = t2 - t1
    print ans, delta.total_seconds()
