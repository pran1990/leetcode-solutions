import sys

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.iterative_map = {}
        self.known_changes = []
        return self.iterativeHelper(s, t)
        #return self.isIsomorphicHelper(s, t, {})

    def isIsomorphicHelper(self, s, t, current_map=None):
        if not current_map:
            current_map = {}
        if not s and not t:
            return True
        if len(s) != len(t):
            return False

        if s[0] not in current_map:
            current_map[s[0]] = t[0]
            return self.isIsomorphicHelper(s[1:], t[1:], current_map)
        
        if s[0] == t[0] or current_map[s[0]] == t[0]:
            return self.isIsomorphicHelper(s[1:], t[1:], current_map)
        else:
            return False

    def iterativeHelper(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False

        x = len(s)
        for i in range(x):
            if s[i] not in self.iterative_map:
                if t[i] in self.known_changes:
                    return False
                self.iterative_map[s[i]] = t[i]
                self.known_changes.append(t[i])
            else:
                if self.iterative_map[s[i]] != t[i]:
                    return False

        return True
        


def main():
    x = Solution()
    problems = [("egg", "add"), ("foo", "bar"), ("paper", "title"), ("", ""), ("ab", "aa")]
    for s, t in problems:
        print s, t, x.isIsomorphic(s, t)


if __name__ == '__main__':
    sys.exit(main())
