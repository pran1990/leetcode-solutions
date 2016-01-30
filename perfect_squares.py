import sys
import os
import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        self.sums = {0: 0}
        x = int(math.sqrt(n))
        for i in range(x):
            self.sums[(i+1) ** 2] = 1

        return self.numSquaresHelper(n)

    def numSquaresHelper(self, n):
        if n in self.sums:
            return self.sums[n]
        x = int(math.sqrt(n))
        possibilities = []
        for i in range(x):
            possibilities.append(1 + self.numSquaresHelper(n - ((i+1) ** 2)))

        self.sums[n] = min(possibilities)
        with open(os.path.join(os.getcwd(), 'test'), 'a') as x:
            x.write(self.sums)
            x.write("\n")
        return self.sums[n]
            
            
        

x = Solution()
problems = [1, 12, 13, 132, 9732, 6255, 8285, 5238]
problems = [5238]
for n in problems:
    ans = x.numSquares(n)
    print n, ans
