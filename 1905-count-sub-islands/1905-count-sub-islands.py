class Solution:
    def check_islands(self, grid1, grid2, row, col):
        
        if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]) or grid2[row][col] == 0: 
            return True
        # If one of the cells in either grid is land and the other is water, then the current cell can **not** be a sub-island.
        elif (grid1[row][col] == 0 and grid2[row][col] == 1) or (grid1[row][col] == 1 and grid2[row][col] == 0):
            return False
        # If the cell in both grids is land, we want to change the value so we don't check this same cell later.
        elif grid1[row][col] == 1 and grid2[row][col] == 1:
            grid2[row][col] = 0            
        
            left = self.check_islands(grid1, grid2, row, col - 1)
            right = self.check_islands(grid1, grid2, row, col + 1)
            top = self.check_islands(grid1, grid2, row - 1, col)
            bottom = self.check_islands(grid1, grid2, row + 1, col)
    
            
            # If all directions of a land cell in grid2 match with corresponding land cells in grid1, then a sub-island was found.
            return left and right and top and bottom
    
    
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        num_sub_islands = 0 
        
        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                # If grid2 is land, and grid2 is a sub-island of grid 1
                if grid2[row][col] == 1 and self.check_islands(grid1, grid2, row, col): 
                    num_sub_islands += 1
                        
        return num_sub_islands