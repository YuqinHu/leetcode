class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevnum = {}
        for i, num in enumerate (nums):
            diff = target - num
            if diff in prevnum:
                return [prevnum[diff], i]
            else:
                prevnum[num] = i