class Solution(object):
    def minDistance(self, word1, word2):
        self.ansmap = [[-1 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            self.ansmap[i][0] = 0
        for i in range(len(word2) + 1):
            self.ansmap[0][i] = 0
        return self.minDistanceHelper(word1, word2)
        #return self.ansmap[len(word1)][len(word2)]

    def minDistanceHelper(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if self.ansmap[len(word1)][len(word2)] != -1:
            return self.ansmap[len(word1)][len(word2)]

        if word1[-1] == word2[-1]:
            answer = self.minDistanceHelper(word1[:-1], word2[:-1])
        else: 
            answer = 1 + min(self.minDistanceHelper(word1[:-1], word2),
                             self.minDistanceHelper(word1, word2[:-1]),
                             self.minDistanceHelper(word1[:-1], word2[:-1]))
        self.ansmap[len(word1)][len(word2)] = answer
        return answer
        

x = Solution()

print x.minDistance("word1", "word2")
print x.minDistance("zeil", "trials")
print x.minDistance("abcdxabcde", "abcdeabcdx")
