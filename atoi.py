import sys
class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        if not string:
            return 0
        string = string.strip()
        numbers = [str(x) for x in range(10)]
        negative = False
        if string[0] not in numbers:
            if string[0] == '-':
                negative = True
                string = string[1:]
            elif string[0] == '+':
                string = string[1:]
            else:
                return sys.maxint
        
        answer = 0
        for s in string:
            if s not in numbers:
                return sys.maxint
            answer = answer * 10 + int(s)
            
        return answer if not negative else answer * -1

x = Solution()
problems = ["-1", "+1", "+-1"]
for problem in problems:
    print problem, x.myAtoi(problem)
