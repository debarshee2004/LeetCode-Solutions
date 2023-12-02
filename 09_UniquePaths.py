class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Handle edge cases: empty grid or start cell has an obstacle
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize two 1D arrays to keep track of the number of paths
        previous = [0] * n
        current = [0] * n
        
        # The top-left corner has only one way to be reached (start point)
        previous[0] = 1
        
        # Loop through each row of the grid
        for i in range(m):
            # If there's an obstacle at the beginning of the row, no way to get there
            # Otherwise, it inherits the path count from the previous row
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
            
            # Loop through the remaining cells in the current row
            for j in range(1, n):
                # If there's an obstacle, no paths to this cell
                if obstacleGrid[i][j] == 1:
                    current[j] = 0
                else:
                    # Number of paths is the sum of paths from the top and the left
                    current[j] = current[j-1] + previous[j]
            
            # Update previous array for the next iteration
            previous[:] = current
        
        # Return the number of paths to the bottom-right corner
        return previous[n-1]