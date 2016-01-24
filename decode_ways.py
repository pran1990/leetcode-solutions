import string
import sys

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = string.lowercase
        self.alphabet = {str(i+1): letters[i] for i in range(len(letters))}
        self.known_answers = {'': 1}
        return self.decodingsHelper(s) if s else 0

    def decodingsHelper(self, s):
        # determine  if first two chars can form a string
        if s in self.known_answers:
            return self.known_answers[s]
        if s[0] == "0":
            self.known_answers[s] = 0
        elif len(s) == 1:
            if s == "0":
                self.known_answers[s] = 0
            else:
                self.known_answers[s] = 1
        if s in self.known_answers:
            #print 'Returning', self.known_answers[s], 'for', s, 'precalculated'
            return self.known_answers[s]
        answer = 0
        if s[:2] in self.alphabet:
            #print s[:2], 'is in alphabet, calling', s[2:]
            answer += self.decodingsHelper(s[2:])
        #print 'Now calling', s[1:]
        answer += self.decodingsHelper(s[1:])
        self.known_answers[s] = answer
        #print 'Returning', self.known_answers[s], 'for', s
        return self.known_answers[s]


def main():
    x = Solution()
    problems = ["", "12", "121", "1234", "0", "10", "21", "01"]
    for n in problems:
        print n, ' : ', x.numDecodings(n)


if __name__ == '__main__':
    sys.exit(main())
