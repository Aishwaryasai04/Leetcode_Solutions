class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        path = set()
        visited = set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            path.remove(course)
            visited.add(course)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

        
