class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Map = {")": "(", "]": "[", "}": "{"}
        res = []
        for char in s:
            if char not in Map:
                res.append(char)
                continue
            if not res or res[-1] != Map[char]:
                return False
            res.pop()

        return not res