class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_list = {}
        t_list = {}
        for char in s:
            s_list[char] = s_list.get(char, 0) + 1
        for char in t:
            t_list[char] = t_list.get(char, 0) + 1
        return s_list == t_list