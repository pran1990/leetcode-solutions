import sys

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        self.mapping = {}
        self.mapped_words = []
        if not pattern and not str:
            return True

        x = len(pattern)
        words = str.split(' ')
        if x != len(words):
            return False

        for i in range(x):
            if pattern[i] not in self.mapping:
                if words[i] in self.mapped_words:
                    return False
                self.mapping[pattern[i]] = words[i]
                self.mapped_words.append(words[i])
            else:
                if self.mapping[pattern[i]] != words[i]:
                    return False
        return True
        

def main():
    x = Solution()

    problems = [("abba", "dog cat cat dog" ),
    ("abba", "dog cat cat fish"),
    ("aaaa", "dog cat cat dog" ),
    ("abba", "dog dog dog dog" ),
    ]

    for s, t in problems:
        print s, t, x.wordPattern(s, t)


if __name__ == '__main__':
    sys.exit(main())
