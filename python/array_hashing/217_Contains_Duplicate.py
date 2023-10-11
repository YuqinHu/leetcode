class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prevnum = set()
        for num in nums:
            if num in prevnum:
                return True
            else:
                prevnum.add(num)
        return False
