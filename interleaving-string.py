class Solution(object):
    def isInterleave(self, s1, s2, s3):
        self.table = [[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        return self.isInterleaveHelper(s1, s2, s3)

    def isInterleaveHelper(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1 and not s2:
            if not s3:
                return True
            return False

        if not s1:
            self.table[0][len(s2)] = (s2 == s3)
            return s2 == s3
        if not s2:
            self.table[len(s1)][0] = (s1 == s3)
            return s1 == s3

        if self.table[len(s1)][len(s2)] != -1:
            return self.table[len(s1)][len(s2)] 
        lanswer, ranswer = False, False
        if s1[0] == s3[0]:
            lanswer = self.isInterleaveHelper(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]:
            ranswer = self.isInterleaveHelper(s1, s2[1:], s3[1:])
        self.table[len(s1)][len(s2)] = lanswer or ranswer
        return lanswer or ranswer


x = Solution()
print x.isInterleave("aabcc",  "dbbca", "aadbbcbcac")
print x.isInterleave("aabcc",  "dbbca", "aadbbbaccc")
