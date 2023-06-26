class Solution:
    def swimInWater(self, grid) -> int:
        def dfs(row: int, col: int, swim_time: int, visited) -> bool:
            if row < 0 or row >= len_grid or col < 0 or col >= len_grid:
                return False
            if (row, col) in visited:
                return False
            visited.add((row, col))
            cell_time = grid[row][col]
            if cell_time > swim_time:
                return False
            
            if row == len_grid - 1 and col == len_grid - 1:
                return True
          
            if dfs(row + 1, col, swim_time, visited):
                return True
            elif dfs( row, col + 1, swim_time, visited ):
                return True
            elif dfs( row - 1, col, swim_time, visited ):
                return True
            elif dfs(row, col - 1, swim_time, visited):
                return True
            return False

        len_grid = len(grid)
        left = grid[-1][-1]
        right = len_grid * len_grid - 1
        while left < right:
            visited = set()
            swim_time = left + (right - left) // 2
            if dfs(0, 0, swim_time, visited):
                right = swim_time
            else:
                left = swim_time + 1
        return left