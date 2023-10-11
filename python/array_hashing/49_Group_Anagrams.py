class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}
        
        for word in strs:
            sortword = ''.join(sorted(word))
            if sortword in anagram:
                anagram[sortword].append(word)
            else:
                anagram[sortword ]= [word]
        return anagram.values()