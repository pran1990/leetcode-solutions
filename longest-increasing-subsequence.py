class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.mat = [1 for i in range(len(nums))]
        return self.LISBottomUp(nums)

    def LIS_length_helper(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            self.mat[1] = 1
            return 1

        if self.mat[len(nums)]:
            return self.mat[len(nums)]

        answers = []

        for i in range(1, len(nums)):
            candidate = self.LIS_length_helper(nums[:i])
            if nums[i-1] < nums[len(nums) - 1]:
                answers.append(candidate+1)
            else:
                answers.append(candidate)

        self.mat[len(nums)] = max(answers)
        return self.mat[len(nums)] 

    def LISBottomUp(self, nums):
        l = len(nums)
        for i in range(1,l):
            max_ = 0
            for j in range(0, i):
                if nums[j] < nums[i] and self.mat[i] < self.mat[j] + 1:
                    self.mat[i] = self.mat[j] + 1
        return max(self.mat) if self.mat else 0
        


x = Solution()
problems = [([10, 9, 2, 5, 3, 7, 101, 18], 4), ([], 0), ([-2, -1], 2)]

for i, j in problems:
    print i, j    
    assert (x.lengthOfLIS(i) == j), "No match!" 
