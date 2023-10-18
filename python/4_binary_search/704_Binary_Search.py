class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = len(nums) - 1
        l = 0
        while l <= r:
            mid = (r + l) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                r = mid - 1
            else:
                l = mid + 1
        return -1