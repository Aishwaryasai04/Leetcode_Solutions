class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i,char in enumerate(s):
            if s.count(char)==1:
                return i
        return -1
