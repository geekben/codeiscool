class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        op = 0
        for i in xrange(k):
            if blocks[i] == 'W':
                op += 1
        if op == 0:
            return 0
        lb = len(blocks)
        minop = op
        for i in xrange(k,lb):
            ob = i - k
            ib = i
            if blocks[ob] == 'W':
                op -= 1
            if blocks[ib] == 'W':
                op += 1
            if op == 0:
                return 0
            minop = min(minop, op)
        return minop
