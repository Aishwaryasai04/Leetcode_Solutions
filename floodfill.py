class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original_color = image[sr][sc]
        if original_color == color:
            return image

        # Define DFS function inside floodFill
        def dfs(r, c):
            # Check if (r, c) is out of bounds or not matching original color
            if (r < 0 or r >= len(image) or
                c < 0 or c >= len(image[0]) or
                image[r][c] != original_color):
                return
            # Fill the current pixel
            image[r][c] = color
            # Visit all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Start the DFS from the starting point
        dfs(sr, sc)

        return image
