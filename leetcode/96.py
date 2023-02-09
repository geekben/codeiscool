class Solution(object):
    d = {}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.d:
            return self.d[n]
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        ret = 0
        for h in xrange(1, n+1):
            ret += self.numTrees(h-1)*self.numTrees(n-h)
        self.d[n] = ret
        return ret
