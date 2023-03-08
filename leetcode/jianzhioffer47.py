class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lm = len(grid)
        ln = len(grid[0])
        for i in xrange(lm):
            for j in xrange(ln):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i-1][j], grid[i][j-1])
        return grid[lm-1][ln-1]
