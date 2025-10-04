"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):

        """
        :type node: Node
        :rtype: Node
        """
        new={}

        def dfs(node):
            if node in new:
                return new[node]

            copy=Node(node.val)
            new[node]=copy

            for nei in node.neigbhors:
                copy.neighbhors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
