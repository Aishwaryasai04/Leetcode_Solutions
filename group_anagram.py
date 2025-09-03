class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups=defaultdict(list)

        for words in strs:
            key = "".join(sorted(words))
            groups[key].append(words)

        return list(groups.values())
