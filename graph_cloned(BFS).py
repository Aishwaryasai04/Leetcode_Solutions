"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):

        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        cloned={}
        queue=deque([node])

        cloned[node]=Node(node.val)

        while queue:
            cur=queue.popleft()

            for nei in cur.neighbors:
                if nei not in cloned:
                    cloned[nei]=Node(nei.val)
                    queue.append(nei)
                cloned[cur].neighbors.append(cloned[nei])

        return cloned[node]
                
