class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new=("".join(i for i in s if i.isalnum())).lower()
        return new==new[::-1]
