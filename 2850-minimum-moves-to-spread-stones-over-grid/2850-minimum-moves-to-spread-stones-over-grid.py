class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        memo = {}
        def compute_string(g):
            res = ""
            for i in range(3):
                for j in range(3):
                    res += str(g[i][j])
            return res
        def dfs(grid):
            nonlocal memo
            grid_s = compute_string(grid)
            if grid_s in memo: return memo[grid_s]

            non_zero = True
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == 0:
                        non_zero = False
            if non_zero:
                memo[grid_s] = 0
                return 0
            res = float("inf")
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == 0:
                        for x in range(3):
                            for y in range(3):
                                if grid[x][y] > 1:
                                    dist = abs(i-x) + abs(j-y)
                                    grid[i][j] += 1
                                    grid[x][y] -= 1
                                    res = min(res, dist + dfs(grid))
                                    grid[i][j] -= 1
                                    grid[x][y] += 1
            memo[grid_s] = res
            return res
        return dfs(grid)