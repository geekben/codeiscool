class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        lr = len(rowSum)
        lc = len(colSum)
        ret = [[0]*lc for _ in xrange(lr)]

        last = [0]*lc
        for i in xrange(lr):
            re = rowSum[i]
            for j in xrange(lc):
                ce = colSum[j] - last[j]
                ret[i][j] = min(ce, re)
                re -= ret[i][j]
                last[j] += ret[i][j]
        return ret
