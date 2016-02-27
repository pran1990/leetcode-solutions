class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        cur_seen = {}
        
        cur, max = 0, 0
        leftb = 0
        print "i, char, leftb, cur, max"
        for i, char in enumerate(s):
            if cur_seen.get(char, -2) >= leftb:
                last_seen = cur_seen[char]
                cur_seen[char] = i
                leftb = last_seen + 1
                cur = i - leftb + 1
                if cur > max:
                    max = cur
            else:
                cur += 1
                cur_seen[char] = i
                if cur > max:
                    max = cur    

            #print i, char, leftb, cur, max
        return max


x = Solution()
print x.lengthOfLongestSubstring("bbtablud")
