import sys

class Solution:

    def comp(self, a, b):
        if a+b > b+a:
            return 1
        elif a+b < b+a:
            return -1
        else:
            return 0

    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        strnum = [str(i) for i in num]
        strnum.sort(cmp=self.comp, reverse=True)
        return ''.join(strnum)
            
            
            




def main():
    x = Solution()
    x.largestNumber([3, 30, 34, 5, 9])


if __name__ == '__main__':
    sys.exit(main())
