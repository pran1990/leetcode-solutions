class Solution(object):
    def isMatch(self, s, p):
        # sanity
        if s and p and p[-1] not in ['*', '.'] and s[-1] != p[-1]:
            return False
        return self.isMatchHelper(s, p)

    def isMatchHelper(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        if not s:
            if len(p) >= 2 and p[1] == '*':
                return self.isMatchHelper(s, p[2:])
            return False

        if len(p) >1 and p[1] == '*':
            if not s:
                return True
            if s[0] == p[0] or p[0] == '.':
                return self.isMatchHelper(s[1:], p[2:]) or self.isMatchHelper(s[1:], p) or self.isMatchHelper(s, p[2:])
            return self.isMatchHelper(s, p[2:])

        if p[0] == '.':
            return True and self.isMatchHelper(s[1:], p[1:])
        return s[0] == p[0] and self.isMatchHelper(s[1:], p[1:])
        
x = Solution()
print x.isMatch("aa","a") 
print x.isMatch("aa","aa")
print x.isMatch("aaa","aa")
print x.isMatch("aa", "a*")
print x.isMatch("aa", ".*")
print x.isMatch("ab", ".*")
print x.isMatch("aab", "c*a*b")
print x.isMatch("a", "ab*")
print x.isMatch("ab", ".*c")
print x.isMatch("bbbba", ".*a*a")
print x.isMatch("a", "a*a")
