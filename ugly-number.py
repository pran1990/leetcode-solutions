class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if not num:
            return False
        x = num
        while not x % 2:
            x = x/2

        while not x % 3:
            x = x/3

        while not x % 5:
            x = x/5

        return x == 1


x = Solution()
print x.isUgly(6)
print x.isUgly(14)
print x.isUgly(1)
print x.isUgly(0)
