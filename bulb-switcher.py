import math
import sys

class Solution(object):

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
        

def main():
    x = Solution()
    problems = [1,2,3,4,5,6]
    for s in problems:
        print s, x.bulbSwitch(s)


if __name__ == '__main__':
    sys.exit(main())
