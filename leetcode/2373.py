class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        ll = len(grid[0])

        tm = [0 for _ in xrange(ll)]
        ret = [[0 for _ in xrange(ll-2)] for _ in xrange(ll-2)]

        for i in xrange(ll-2):
            for j in xrange(ll):
                tm[j] = max(grid[i][j], grid[i+1][j], grid[i+2][j])
                if j >= 2:
                    ret[i][j-2] = max(tm[j-2], tm[j-1], tm[j])
        return ret
