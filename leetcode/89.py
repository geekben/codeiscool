class Solution(object):
    # TODO: use global var to share results among cases
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [0 for _ in xrange(1<<n) ]

        for i in xrange(n):
            l = 1 << i # slower than len()
            # l = len(ret)
            for j in xrange(l-1,-1,-1):
                ret[l+l-1-j] = ret[j] + (1<<i)

        return ret
